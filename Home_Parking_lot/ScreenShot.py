import cv2
import schedule
import time
from datetime import datetime
import os

# Gets video data from webcam 
webcam = cv2.VideoCapture(0)

# Set the resolution (Width)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# Set the resolution (Height)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Path to save the photos
save_path = 'parking lot photos'

# Ensure the directory exists
if not os.path.exists(save_path):
    os.makedirs(save_path)

def take_photo():
    # Read the current frame from the webcam
    ret, frame = webcam.read()
    
    # Check if frame is not empty
    if not ret:
        raise ValueError("Can't read frame")

    # Format the filename as 'YYYY-MM-DD_HH-MM-SS.png'
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = os.path.join(save_path, f'{timestamp}.png')

    # Save the image
    cv2.imwrite(filename, frame)

# Schedule the photo to be taken every 15 minutes
schedule.every(1).minutes.do(take_photo)

try:
    while True:
        # Check if scheduled job is pending to run and run them
        schedule.run_pending()
        time.sleep(1)
finally:
    # Release the webcam before exiting
    webcam.release()