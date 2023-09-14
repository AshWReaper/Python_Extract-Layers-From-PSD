# PSD Layer Extractor

## Description

This repository contains a Python script for extracting layers from a Photoshop `.psd` file. It also supports nested layer groups. The script uses the `psd-tools` library for reading the `.psd` files and extracting the layers.

## Installation

### Prerequisites

- Python 3.x
- pip3

### Installing Dependencies

Before running the script, you need to install the `psd-tools` package. You can install it using pip:

pip3 install psd-tools

# Usage
Clone this repository or download the extract_psd_layers.py script.

git clone https://github.com/YourUsername/psd-layer-extractor.git

Navigate to the folder containing extract_psd_layers.py.

cd path/to/script

Run the script.

python3 extract_layers.py

The script will prompt you to enter the path to the .psd file you want to extract layers from.

Upon successful execution, the layers will be extracted into a folder called extracted_images.

# How It Works
The script uses a recursive function to iterate over each layer and nested layer group in the PSD file. Each layer is composited and saved as a PNG file in the extracted_images directory.

# Contributing
Feel free to open issues or PRs if you find any problems or have suggestions for improvements.

# License
MIT License
