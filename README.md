# IIIF Manifest Splitter
This project contains a script for splitting a IIIF (International Image Interoperability Framework) manifest into multiple volumes. The script first extracts the sequences from the manifest, then splits the sequences for each volume, and finally adds context to each split sequence.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.x
* A IIIF manifest file

### Installation
Clone the repository:
git clone https://github.com/dittm/iiif-manifest-splitter.git
Navigate to the project directory:
cd iiif-manifest-splitter

## Usage
* Place your IIIF manifest file in the project directory.
* Run the script with the name of your IIIF manifest file as an argument:
python split_manifest.py your-manifest-file.json
The script will create a new JSON file for each volume in the manifests directory.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.