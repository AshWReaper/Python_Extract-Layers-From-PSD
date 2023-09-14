import os
from psd_tools import PSDImage

def extract_layers(group, output_dir, parent_name=''):
    for i, layer in enumerate(group):
        layer_name = f"{parent_name}_layer_{i}"
        output_filename = os.path.join(output_dir, f"{layer_name}.png")
        
        if layer.is_group():  # If the layer is a group, go deeper
            extract_layers(layer, output_dir, layer_name)
        else:  # If it's a regular layer, extract it
            print(f"Extracting {layer_name} to {output_filename}")
            image = layer.composite()
            image.save(output_filename)

# Prompt for the PSD file name
filename = input("Enter the path to the PSD file: ")

# Check if the file exists
if not os.path.exists(filename):
    print(f"File {filename} not found!")
    exit(1)

# Create the 'extracted_images' directory if it doesn't exist
output_dir = "extracted_images"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Load the PSD file
psd = PSDImage.open(filename)

# Start the extraction
extract_layers(psd, output_dir)

print("Extraction complete! Check the 'extracted_images' folder.")
