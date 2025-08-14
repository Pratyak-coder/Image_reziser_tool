import os
from PIL import Image

def resize_images(input_folder, output_folder, target_size=(800, 600), quality=85):
    """
    Resize all images in the input folder and save to output folder.
    
    Args:
        input_folder (str): Path to input folder containing images
        output_folder (str): Path to save resized images
        target_size (tuple): Desired (width, height) for resized images
        quality (int): JPEG quality (0-100)
    """
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Supported image extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif')
    
    # Iterate through all files in input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(valid_extensions):
            try:
                # Open image
                img_path = os.path.join(input_folder, filename)
                img = Image.open(img_path)
                
                # Convert to RGB if necessary (for PNG, GIF)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Resize image while maintaining aspect ratio
                img.thumbnail(target_size, Image.Resampling.LANCZOS)
                
                # Generate output path
                output_path = os.path.join(output_folder, filename)
                
                # Save resized image
                img.save(output_path, 'JPEG', quality=quality)
                print(f"Processed: {filename}")
                
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                
        else:
            print(f"Skipped: {filename} (unsupported format)")

if __name__ == "__main__":
    # Example usage
    input_dir = "input_images"
    output_dir = "output_images"
    resize_images(input_dir, output_dir)