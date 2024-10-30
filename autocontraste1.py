import cv2
import os
from PIL import Image, ImageEnhance

# Define the input and output folders
input_folder = 'entrada'
output_folder = 'salida'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Function to enhance contrast and color
def enhance_frame(frame):
    # Convert the frame from OpenCV format to PIL format
    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
    # Enhance contrast
    enhancer_contrast = ImageEnhance.Contrast(pil_image)
    pil_image = enhancer_contrast.enhance(1.5)  # Adjust the factor as needed
    
    # Enhance color
    enhancer_color = ImageEnhance.Color(pil_image)
    pil_image = enhancer_color.enhance(1.2)  # Adjust the factor as needed

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

            # Enhance frame
            enhanced_frame = enhance_frame(frame)

            # Write the enhanced frame to the output video
            out.write(enhanced_frame)

        # Release resources
        cap.release()
        out.release()

print("Processing complete. Enhanced videos saved to:", output_folder)
