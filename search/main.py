from sentence_transformers import SentenceTransformer
import json
import os
import re
import yaml
import config

output_filename = "vectors.json"
# Initialize the model
# This same model should be used on the client-side to embed queries.
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_datasets_metadata():
    metadata_entries = []
    for filename in os.listdir(config.datasets_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(config.datasets_dir, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                pattern = r"^---\n(.*?)\n---\n"
                match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
                if match:
                    payload = match.group(1)  # Return captured YAML
                    payload = yaml.safe_load(payload)
                    json_payload = json.dumps(payload)
                    metadata_entries.append(json_payload)
    return metadata_entries


def embed_datasets_metadata(datasets_metadata):
    results = []
    for dataset_metadata in datasets_metadata:
        tensor = model.encode(
            dataset_metadata, convert_to_tensor=True, normalize_embeddings=True
        )
        vector_embedding = {
            "vector": tensor.cpu().detach().numpy().tolist(),
            "metadata": json.loads(dataset_metadata),
        }
        results.append(vector_embedding)

    return results


def save_vectors_to_json(data, filename=output_filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


datasets_metadata = get_datasets_metadata()
vector_embeddings = embed_datasets_metadata(datasets_metadata)
save_vectors_to_json(vector_embeddings)
print(f"Vectors saved to {output_filename}.")
