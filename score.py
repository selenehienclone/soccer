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
    top_crop = int(height * 0.2)
    top_cropped_img = img[:top_crop, :]

    # Get the middle 30% horizontally of the top 20% and save as result image
    middle_width_start = int(width * 0.35)
    middle_width_end = int(width * 0.65)
    result_img = top_cropped_img[:, middle_width_start:middle_width_end]
    cv2.imwrite(save_path_result, result_img)

# Example usage
image_path = 'field2.png'
save_path_result = 'result.png'

crop_image(image_path, save_path_result)


def extract_numbers_from_screenshot(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to RGB (required for pytesseract)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(Image.fromarray(img_rgb))

    # Process the extracted text to find two numbers from left to right
    numbers = process_extracted_text(text)

    return numbers

def process_extracted_text(text):
    # Add your logic to process the extracted text and identify two numbers
    # This example assumes the numbers are the first two integers found in the text
    numbers = [int(s) for s in text.split() if s.isdigit()][:2]
    return numbers

# Example usage
screenshot_path = 'result.png'
numbers = extract_numbers_from_screenshot(screenshot_path)

if len(numbers) == 2:
    print(f"The identified numbers from left to right are: {numbers[0]}, {numbers[1]}")
else:
    print("Two numbers not found.")
