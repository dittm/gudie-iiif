import json

with open('manifests/sequences.json', 'r') as f:
    json_data = json.load(f)

# Extract the first sequence
sequence = json_data[0]

# Extract the first 164 canvases
canvases = sequence.get("canvases", [])[258:350]

# Replace the canvases in the sequence with the first 164 canvases
sequence["canvases"] = canvases

# Ensure the output includes "sequences"
output = {"sequences": json_data}

# Write the modified sequence back to the file
with open('manifests/sequence-248-2.json', 'w') as f:
    json.dump(output, f, indent=4)