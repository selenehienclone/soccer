import cv2
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2

def crop_image(image_path, save_path_result):
    # Read the image
    img = cv2.imread(image_path)

    # Get the height and width of the image
    height, width, _ = img.shape

    # Crop the top 20%
    top_crop = int(height * 0.10)
    top_cropped_img = img[:top_crop, :]

    # Get the middle 30% horizontally of the top 20% and save as result image

    p1_score_left = int(width * 0.40)
    p1_score_right = int(width * 0.43)
    p2_score_left = int(width * 0.55)
    p2_score_right = int(width * 0.58)
    p1_score = top_cropped_img[:, p1_score_left:p1_score_right]
    p2_score = top_cropped_img[:, p2_score_left:p2_score_right]
    cv2.imwrite('p1_score.png', p1_score)
    cv2.imwrite('p2_score.png', p2_score)

# Example usage
image_path = 'field2.png'
save_path_result = 'result.png'

crop_image(image_path, save_path_result)

import cv2
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def identify_number_in_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to RGB (required for pytesseract)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Use Tesseract to extract text
    extracted_text = pytesseract.image_to_string(Image.fromarray(img_rgb))

    # Process the extracted text to find numbers (assuming it's a single number)
    numbers = [int(s) for s in extracted_text.split() if s.isdigit()]

    # If there are numbers, identify the number
    if numbers:
        identified_number = numbers[0]
        return identified_number
    else:
        return None

# Example usage
image_path = 'p1_score.png'
identified_number = identify_number_in_image(image_path)

if identified_number is not None:
    print(f"The identified number in the image is: {identified_number}")
else:
    print("No number found in the image.")
