import cv2
import numpy as np

def find_multiple_templates(template_path, image_path, num_occurrences):
    # Read the template and the image
    template = cv2.imread(template_path, 0)
    img = cv2.imread(image_path, 0)

    # Set a threshold for the matching result
    threshold = 0.8

    for _ in range(num_occurrences):
        # Perform template matching
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # Check if the match exceeds the threshold
        if max_val >= threshold:
            # Get the coordinates of the matched area
            top_left = max_loc
            h, w = template.shape

            # Draw a rectangle around the matched region
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img, top_left, bottom_right, 255, 2)

            # Exclude the matched region from further matching
            img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 0
        else:
            # Break the loop if no more occurrences are found
            break

    # Display the result
    cv2.imshow('Matching Result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
template_image_path = 'teamA.png'
main_image_path = 'team1.png'
find_multiple_templates(template_image_path, main_image_path, num_occurrences=5)
