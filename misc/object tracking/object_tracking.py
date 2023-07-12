import cv2 as cv

capture_obj = cv.VideoCapture('C:/Users/dalto/Desktop/Coding/computer_vision/misc/object tracking/traffic_video1.mp4')

while capture_obj.isOpened():
    # Reads the video footage and give a returned value(T/F) and the individual frame
    ret_val, frame = capture_obj.read()

    # If ret_val is False, the video file has ended or error reading the frames.
    if not ret_val:
        print("Error: Unable to read video or video has ended.")
        break

    cv.imshow("frame", frame)
    
    if cv.waitKey(int(1000/30)) == ord('q'):
        break

capture_obj.release()
cv.destroyAllWindows()