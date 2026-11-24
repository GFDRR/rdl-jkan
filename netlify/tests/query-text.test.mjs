import assert from "node:assert/strict";
import { test } from "node:test";
import {
  findCountry,
  matchExpression,
  parseQuery,
} from "../functions/query/query-text.mjs";

const COUNTRIES = [
  ["ken", "Kenya"],
  ["ner", "Niger"],
  ["nga", "Nigeria"],
  ["gin", "Guinea"],
  ["png", "Papua New Guinea"],
  ["tza", "Tanzania, United Republic of"],
  ["vnm", "Viet Nam"],
  ["civ", "Côte d'Ivoire"],
].map(([slug, title]) => ({ slug, title }));

const country = (q) => findCountry(q, COUNTRIES)?.slug ?? null;

test("terms match in any order", () => {
  assert.equal(matchExpression(parseQuery("flood kenya")), '"flood" AND "kenya"');
  assert.equal(matchExpression(parseQuery("kenya flood")), '"kenya" AND "flood"');
});

test("quoted text is one term", () => {
  assert.deepEqual(parseQuery('"flood hazard" nairobi'), ["flood hazard", "nairobi"]);
});

test("stop words are dropped unless there is nothing else", () => {
  assert.deepEqual(parseQuery("data for floods"), ["floods"]);
  assert.deepEqual(parseQuery("the data"), ["the", "data"]);
});

test("FTS syntax in the query is never executed", () => {
  for (const q of ['x" OR "', "NEAR(", "title:flood*", "flood AND", '"']) {
    const expression = matchExpression(parseQuery(q));
    if (expression) assert.match(expression, /^"[^"]+"( AND "[^"]+")*$/);
  }
});

test("terms too short for the trigram index are skipped", () => {
  assert.equal(matchExpression(parseQuery("a")), null);
  assert.equal(matchExpression(parseQuery("eu flood")), '"flood"');
});

test("countries are found by whole words, longest name first", () => {
  assert.equal(country("flood kenya"), "ken");
  assert.equal(country("Nigeria floods"), "nga");
  assert.equal(country("niger floods"), "ner");
  assert.equal(country("papua new guinea earthquake"), "png");
  assert.equal(country("flood hazard"), null);
});

test("countries are found by short names, aliases and without accents", () => {
  assert.equal(country("tanzania"), "tza");
  assert.equal(country("vietnam"), "vnm");
  assert.equal(country("cote d'ivoire"), "civ");
  assert.equal(country("ivory coast"), "civ");
});

test("the country's name is taken out of the remaining terms", () => {
  assert.deepEqual(
    findCountry("earthquake papua new guinea hazard", COUNTRIES).rest,
    ["earthquake", "hazard"],
  );
  assert.deepEqual(findCountry("kenya", COUNTRIES).rest, []);
});
