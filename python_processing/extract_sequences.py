import json

with open('manifests/data.json', 'r') as f:
    json_data = json.load(f)
sequences = json_data.get("sequences", [])

with open('manifests/sequences.json', 'w') as f:
    json.dump(sequences, f, indent=4)