import cv2
import numpy as np

def find_template_occurrences(template_path, image_path):
    # Read the template and the image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Read the image in color

    # Perform template matching on the grayscale image
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    locations = np.where(result >= threshold)

    # Get the center coordinates of the occurrences
    occurrences = []
    h, w = template.shape
    for loc in zip(*locations[::-1]):
        center = (loc[0] + w // 2, loc[1] + h // 2)
        occurrences.append(center)

    return occurrences

# Function to draw green circles at the centers
def draw_circles(image, centers):
    for center in centers:
        cv2.circle(image, center, 10, (0, 255, 0), -1)  # Draw a green circle

# Example usage
template_image_path = 'teamA.png'
main_image_path = 'team1.png'
occurrences = find_template_occurrences(template_image_path, main_image_path)

# Read the main image in color for drawing circles
main_image = cv2.imread(main_image_path, cv2.IMREAD_COLOR)

# Draw circles on the main image
draw_circles(main_image, occurrences)

# Display the result
cv2.imwrite('result_image.png', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Number of occurrences found: {len(occurrences)}")
print("Center coordinates of occurrences:")
for center in occurrences:
    print(center)
