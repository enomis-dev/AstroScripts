import cv2
import os
import argparse

def create_video_from_images(folder_path, output_path, fps):
    # Get all files in the folder
    files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not files:
        print("No images found in the folder.")
        return

    # Get the first image to determine the size
    first_image_path = os.path.join(folder_path, files[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for file in files:
        image_path = os.path.join(folder_path, file)
        image = cv2.imread(image_path)
        
        if image is not None:
            video.write(image)
        else:
            print(f"Could not read {image_path}. Skipping.")

    # Release the video writer
    video.release()
    print(f"Video saved at {output_path}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Create a video from a folder of images.")
    parser.add_argument('--images_folder_path', type=str, help='Path to the folder containing images')
    parser.add_argument('--output_video_path', type=str, default='output_video.mp4',
                        help='Path to save the output video (default: output_video.mp4)')
    parser.add_argument('--fps', type=int, default=30, help='Frames per second for the video (default: 30)')

    args = parser.parse_args()

    # Call the function with command-line arguments
    create_video_from_images(args.images_folder_path, args.output_video_path, args.fps)

if __name__ == "__main__":
    main()

# Example usage:
# python .\star_video_generator.py --images_folder_path Photos
