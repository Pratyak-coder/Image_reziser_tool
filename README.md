Image Resizer Tool
Overview
A Python script to batch resize and convert images to JPEG using Pillow. Processes JPG, PNG, BMP, and GIF files in a folder while maintaining aspect ratio.
Requirements

Python 3.x
Pillow (pip install Pillow)

Usage

Place images in input_images folder.
Run the script:
bashpython image_resizer.py

Resized images are saved in output_images.

Customization
Edit in image_resizer.py:

input_folder: Input folder path (default: input_images)
output_folder: Output folder path (default: output_images)
target_size: Width, height (default: (800, 600))
quality: JPEG quality (default: 85)

Supported Formats

JPG/JPEG, PNG, BMP, GIF

Notes

Skips unsupported files with feedback.
Handles errors for corrupt files.
Output folder is created automatically.

