// Embeds the text of a query for semantic search. Built as a file of its own,
// which search.js loads when a search needs it: the library and the model it
// downloads are far larger than the rest of the site.
import { env, pipeline } from "@huggingface/transformers";

// Must match the model used to generate the embeddings
// (see python/generate_vectors.py).
const EMBEDDING_MODEL = "Xenova/all-MiniLM-L6-v2";

env.allowLocalModels = false;

let embedderPromise = null;

function loadEmbedder() {
  embedderPromise ??= pipeline("feature-extraction", EMBEDDING_MODEL).catch(
    (error) => {
      // Don't keep a failed load: let a later search retry.
      embedderPromise = null;
      throw error;
    },
  );
  return embedderPromise;
}

export async function embed(text) {
  const embedder = await loadEmbedder();
  const output = await embedder(text, { pooling: "mean", normalize: true });
  return Array.from(output.data);
}
