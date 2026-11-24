// Turns the text typed in the search box into full-text search terms.

// The FTS index is made of trigrams, so shorter terms cannot match.
const MIN_TERM_LENGTH = 3;

const STOP_WORDS = new Set([
  "and", "the", "for", "from", "with", "data", "dataset", "datasets",
]);

// Common names that differ from the official ones in python/config.py.
const COUNTRY_ALIASES = {
  bol: ["bolivia"],
  civ: ["ivory coast"],
  cod: ["drc", "dr congo", "democratic republic of the congo"],
  cpv: ["cabo verde"],
  cze: ["czechia"],
  fsm: ["micronesia"],
  gbr: ["uk", "great britain"],
  kor: ["south korea"],
  lao: ["laos"],
  lby: ["libya"],
  mkd: ["north macedonia"],
  prk: ["north korea"],
  pse: ["palestine", "palestinian territories"],
  rus: ["russia"],
  swz: ["eswatini"],
  syr: ["syria"],
  tls: ["east timor"],
  tur: ["turkiye"],
  usa: ["usa", "united states of america"],
  vnm: ["vietnam"],
};

function fold(text) {
  return text
    .normalize("NFKD")
    .replace(/\p{M}/gu, "")
    .toLowerCase();
}

// Words of a text, ignoring case, accents and punctuation.
function words(text) {
  return fold(text).match(/[\p{L}\p{N}]+/gu) ?? [];
}

// Search terms: "quoted text" is one term, everything else is split in words.
export function parseQuery(q) {
  const terms = [];
  const rest = q.replace(/"([^"]+)"/g, (_, phrase) => {
    terms.push(phrase.trim());
    return " ";
  });
  // Split without folding: the index keeps accents.
  const plain = rest.match(/[\p{L}\p{N}\p{M}]+(?:[_-][\p{L}\p{N}\p{M}]+)*/gu) ?? [];
  const useful = plain.filter((word) => !STOP_WORDS.has(word.toLowerCase()));
  // A query made only of stop words is still a query.
  return [...terms, ...(useful.length || terms.length ? useful : plain)];
}

// FTS5 expression matching all the terms in any order, or null when none of
// them can match. Terms are quoted, so they are never read as FTS operators.
export function matchExpression(terms) {
  const usable = terms.filter((term) => [...term].length >= MIN_TERM_LENGTH);
  if (!usable.length) return null;
  return usable.map((term) => `"${term.replace(/"/g, '""')}"`).join(" AND ");
}

function countryNames({ slug, title }) {
  return [title, title.split(",")[0], ...(COUNTRY_ALIASES[slug] ?? [])];
}

// The country named in the query, with the terms left once its name is taken
// out, or null. Matches whole words, and the longest name wins, so "Papua New
// Guinea" is not Guinea and "Nigeria" is not Niger.
export function findCountry(q, countries) {
  const queryWords = words(q);
  let best = null;
  for (const country of countries) {
    for (const name of countryNames(country)) {
      const nameWords = words(name);
      if (!nameWords.length || (best && nameWords.length <= best.length)) continue;
      for (let at = 0; at + nameWords.length <= queryWords.length; at++) {
        if (nameWords.every((word, i) => queryWords[at + i] === word)) {
          best = { country, at, length: nameWords.length };
          break;
        }
      }
    }
  }
  if (!best) return null;
  const rest = queryWords.filter(
    (_, i) => i < best.at || i >= best.at + best.length,
  );
  return { ...best.country, rest: parseQuery(rest.join(" ")) };
}
