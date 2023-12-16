import cv2

cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('Original', frame)

    # Break the loop with the ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()