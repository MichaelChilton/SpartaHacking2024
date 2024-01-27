import cv2 as cv

def main():
    # Access the default camera
    cap = cv.VideoCapture(1)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Error: Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv.imshow('Camera', frame)

        # Check for the 'q' key to quit
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
