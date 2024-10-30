import os
import subprocess

# Define the input and output folders
input_folder = 'entrada'
output_folder = 'salida'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each video file
for filename in os.listdir(input_folder):
    if filename.endswith('.mp4'):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # FFmpeg command for automatic contrast and color enhancement with audio preservation
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_path,
            '-vf', 'eq=contrast=1.2:brightness=0.05:saturation=1.3:gamma=1.0',  # Auto-enhance video settings
            '-c:a', 'copy',  # Copy audio without re-encoding
            output_path
        ]
        
        # Run the command
        subprocess.run(ffmpeg_command)

print("Processing complete. Enhanced videos with original audio saved to:", output_folder)
