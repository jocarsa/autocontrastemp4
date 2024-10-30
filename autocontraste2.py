import cv2
import os
import numpy as np
from PIL import Image, ImageOps

# Define the input and output folders
input_folder = 'entrada'
output_folder = 'salida'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to automatically enhance contrast and color
def auto_enhance_frame(frame):
    # Convert the frame from OpenCV format to PIL format
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Automatically enhance contrast
    pil_image = ImageOps.autocontrast(pil_image)
    
    # Automatically enhance color
    pil_image = ImageOps.colorize(pil_image.convert('L'), 'black', 'white')

    # Convert the PIL image back to OpenCV format
    return cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

# Process each video file
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        video_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Capture video
        cap = cv2.VideoCapture(video_path)

        # Get video properties
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        # Define the video writer
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Automatically enhance the frame
            enhanced_frame = auto_enhance_frame(frame)

            # Write the enhanced frame to the output video
            out.write(enhanced_frame)

        # Release resources
        cap.release()
        out.release()

print("Processing complete. Enhanced videos saved to:", output_folder)
