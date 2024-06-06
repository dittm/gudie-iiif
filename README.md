
# IIIF Manifest Splitter

This project provides a set of scripts for splitting a IIIF (International Image Interoperability Framework) manifest into multiple individual segments or volumes. It is designed to first extract the sequences from a given manifest file, then split these sequences as required, and finally restructure them with the necessary context for each split segment as per the IIIF specifications.

  

## Getting Started

The instructions below will guide you through setting up the project on your local machine for development and experimentation purposes.

  

### Prerequisites

* Python 3.x installed on your machine

* A valid IIIF manifest file

  

### Installation

To get started with the IIIF Manifest Splitter, clone the repository and navigate to the project directory using the following commands:

Clone the repository:

```git clone https://github.com/[your-username]/iiif-manifest-splitter.git```

Navigate to the project directory:

```cd iiif-manifest-splitter```

Please make sure to replace [your-username] with your GitHub user name.

  

## Usage

Follow these steps to use the script:

* Move your IIIF manifest file into the manifests directory of the project.

* Open a terminal and navigate to the project directory.

* Run the script by providing the path to your IIIF manifest file. For example:

```python extract_sequences.py manifests/your-manifest-file.json```

Replace your-manifest-file.json with the actual file name of your IIIF manifest.

* Subsequently, execute the script that splits the manifest into volumes:

```python split_manifest.py manifests/your-manifest-file.json```

After successful execution, the script will generate a new JSON file for each volume, which will be saved in the manifests directory.

  

## Contributing

Contributions to this project are welcome! If you are interested in contributing, please fork the repository, make your changes, and submit a pull request. Feel free to open an issue with the tag "enhancement" if you have suggestions for improvement.

  

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.