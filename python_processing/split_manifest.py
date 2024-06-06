import json

# Define function to extract and save a sequence slice
def extract_and_save_sequence_slice(input_file, output_file, canvas_range):
    # Load JSON data from the input file
    with open(input_file, 'r') as f:
        json_data = json.load(f)

    # Assume the first sequence is to be extracted
    sequence = json_data[0]

    # Extract the specified range of canvases from the sequence
    sequence["canvases"] = sequence.get("canvases", [])[canvas_range[0]:canvas_range[1]]

    # Wrap the modified sequence with 'sequences' key as required by the IIIF spec
    output_data = {"sequences": [sequence]}

    # Write the modified data back to the specified output file
    with open(output_file, 'w') as f:
        json.dump(output_data, f, indent=4)

# Input file used by all function calls
input_path = 'manifests/sequences.json'

# Define canvas ranges and corresponding output files
canvas_slices_info = [
    {"range": (0, 164), "output_file": 'manifests/sequence-248-0.json'},
    {"range": (164, 258), "output_file": 'manifests/sequence-248-1.json'},
    {"range": (258, 350), "output_file": 'manifests/sequence-248-2.json'},
    {"range": (350, None), "output_file": 'manifests/sequence-248-3.json'},  # Goes to the end if None
]

# Process each range of canvases
for info in canvas_slices_info:
    extract_and_save_sequence_slice(input_path, info["output_file"], info["range"])

print("Manifest processing complete.")