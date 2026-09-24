// Client access to the Netlify query function. The base URL is empty when the
// site itself is served by Netlify; set site.netlify_api_base in _config.yml
// when the site is hosted elsewhere (e.g. GitHub Pages).
const API_BASE =
  typeof window !== "undefined" && window.RDL_API_BASE
    ? String(window.RDL_API_BASE).replace(/\/+$/, "")
    : "";

export async function queryApi(payload) {
  const response = await fetch(`${API_BASE}/.netlify/functions/query`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    const detail = await response.text().catch(() => "");
    throw new Error(
      `Dataset query failed (${response.status}) ${detail.slice(0, 200)}`,
    );
  }

  return response.json();
}