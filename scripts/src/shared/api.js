// Client access to the Netlify query function. The base URL is empty when the
// site itself is served by Netlify; set site.netlify_api_base in _config.yml
// when the site is hosted elsewhere (e.g. GitHub Pages).
const API_BASE =
  typeof window !== "undefined" && window.RDL_API_BASE
    ? String(window.RDL_API_BASE).replace(/\/+$/, "")
    : "";
const ENDPOINT = `${API_BASE}/.netlify/functions/query`;

// A vector of the query does not fit in a URL.
const MAX_URL_PAYLOAD = 2000;
// Answers kept for as long as the page is open, so that going back to a page or
// removing a filter is immediate.
const MAX_ANSWERS = 100;

const answers = new Map();

function remember(key, answer) {
  answers.delete(key);
  answers.set(key, answer);
  if (answers.size > MAX_ANSWERS) answers.delete(answers.keys().next().value);
}

// The requests answered when the site was built, see scripts/initial-data.mjs.
export function rememberInitialData(initialData) {
  for (const { payload, answer } of initialData ?? []) {
    remember(JSON.stringify(payload), answer);
  }
}

// Whether queryApi answers without a request.
export function isAnswered(payload) {
  return answers.has(JSON.stringify(payload));
}

// GET requests are cached by the CDN and, unlike POST with a JSON content type,
// need no preflight request. Neither does POST as plain text.
function request(body) {
  if (body.length <= MAX_URL_PAYLOAD) {
    return fetch(`${ENDPOINT}?payload=${encodeURIComponent(body)}`);
  }
  return fetch(ENDPOINT, {
    method: "POST",
    headers: { "Content-Type": "text/plain" },
    body,
  });
}

export async function queryApi(payload) {
  const key = JSON.stringify(payload);
  if (answers.has(key)) return answers.get(key);

  const response = await request(key);
  if (!response.ok) {
    const detail = await response.text().catch(() => "");
    throw new Error(
      `Dataset query failed (${response.status}) ${detail.slice(0, 200)}`,
    );
  }

  const answer = await response.json();
  remember(key, answer);
  return answer;
}

// The payloads of the list of datasets. Filters without a value are left out, so
// that the same list always has the same payload.
function activeFilters(filters) {
  return Object.fromEntries(
    Object.entries(filters)
      .filter(([, values]) => values.length)
      .map(([type, values]) => [type, [...values].sort()]),
  );
}

export function datasetsPayload(filters, page, pageSize) {
  return { action: "datasets", filters: activeFilters(filters), page, pageSize };
}

export function searchPayload(q, vector, filters, page, pageSize) {
  return {
    action: "search",
    q,
    ...(vector ? { vector } : {}),
    filters: activeFilters(filters),
    page,
    pageSize,
  };
}

export function optionsPayload(filters) {
  return { action: "options", filters: activeFilters(filters) };
}
