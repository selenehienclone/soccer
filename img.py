import cv2
import numpy as np

def find_template_occurrences(template_path, image_path):
    # Read the template and the image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Perform template matching
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locations = np.where(result >= threshold)

    # Get the center coordinates of the occurrences
    occurrences = []
    h, w = template.shape
    for loc in zip(*locations[::-1]):
        center = (loc[0] + w // 2, loc[1] + h // 2)
        occurrences.append(center)

    return occurrences

# Example usage
template_image_path = 'teamA.png'
main_image_path = 'team1.png'
occurrences = find_template_occurrences(template_image_path, main_image_path)

print(f"Number of occurrences found: {len(occurrences)}")
print("Center coordinates of occurrences:")
for center in occurrences:
    print(center)
