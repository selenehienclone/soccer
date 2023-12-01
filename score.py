import cv2
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


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
