import os
import argparse
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def load_images_from_folder(folder):
    """Loads all images from a given folder."""
    images = []
    for filename in os.listdir(folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            img_path = os.path.join(folder, filename)
            img = Image.open(img_path).convert("RGB")
            images.append(np.array(img))
    return images

def stack_images(images):
    """Stacks images to create a star trails effect."""
    # Initialize an array to hold the maximum pixel values
    stacked_image = np.zeros_like(images[0], dtype=np.float32)
    
    for img in images:
        stacked_image = np.maximum(stacked_image, img)
    
    # Convert back to 8-bit image
    stacked_image = np.clip(stacked_image, 0, 255).astype(np.uint8)
    return stacked_image

def save_image(image_array, output_path):
    """Saves the numpy image array to a file."""
    img = Image.fromarray(image_array)
    img.save(output_path)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Create star trails from night sky images.")
    parser.add_argument('--images_folder_path', type=str, required=True,
                        help='Path to the folder containing night sky images')
    parser.add_argument('--output_file', type=str, default='star_trails.jpg',
                        help='Name of the output file (default: star_trails.jpg)')
    args = parser.parse_args()

    # Load images
    images = load_images_from_folder(args.images_folder_path)
    
    if not images:
        print("No images found in the specified folder.")
        return

    # Stack images
    star_trails_image = stack_images(images)
    
    # Save the result
    save_image(star_trails_image, args.output_file)
    
    # Optionally, display the image
    plt.imshow(star_trails_image)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()
