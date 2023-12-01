import cv2
import numpy as np

# Read the image
image = cv2.imread('team1.png')  # Replace 'your_image_path.jpg' with the path to your image

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise and help circle detection
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Use Hough Circle Transform to detect circles
circles = cv2.HoughCircles(
    blurred, 
    cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=5, maxRadius=50
)

# If circles are found, draw them on the original image
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

# Display the result
cv2.imshow('Circles Detected', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
