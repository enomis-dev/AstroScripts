import cv2
import os

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

# Define folder path, output video path, and frames per second
folder_path = 'Photos'
output_path = 'video.mp4'
fps = 4

create_video_from_images(folder_path, output_path, fps)
