import cv2 as cv

capture_obj = cv.VideoCapture('C:/Users/dalto/Desktop/Coding/computer_vision/misc/object tracking/Pysource/traffic_video1.mp4')

# Object detection from a stable camera
object_detector = cv.createBackgroundSubtractorMOG2(history=300, varThreshold=10)



# Reads the video footage and give a returned value(T/F) and the individual frame
while capture_obj.isOpened():
    ret_val, frame = capture_obj.read()
    height, width, _ = frame.shape
    print(height, width) # 1920 x 1080
    # Extract Region of Interest(ROI) 
    roi = frame[550: 1080,  600: 1920]


    # If ret_val is False, the video file has ended or error reading the frames.
    if not ret_val:
        print("Error: Unable to read video or video has ended.")
        break

    # Object detection
    detector_mask = object_detector.apply(roi)
    _, detector_mask = cv.threshold(detector_mask, 254, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(detector_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for i in contours:
        # Calculate area and remove small noise elements
        area = cv.contourArea(i)
        if area > 500:
            # cv.drawContours(roi, [i], -1, (0,0,255), 3)
            x, y, w, h = cv.boundingRect(i)
            cv.rectangle(roi, (x,y), (x + w, y + w), (0,0,255), 3)


    cv.imshow("frame", frame)
    cv.imshow("mask", detector_mask)
    cv.imshow("roi", roi)
    if cv.waitKey(int(1000/30)) == ord('q'):
        break

capture_obj.release()
cv.destroyAllWindows()