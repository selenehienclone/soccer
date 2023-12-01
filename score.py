import cv2
import pytesseract

# Set the path to the Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_score_from_screenshot(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding or other preprocessing techniques if needed
    # ...

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray)

    # Process the extracted text to find the score
    score = process_extracted_text(text)

    return score

def process_extracted_text(text):
    # Add your logic to process the extracted text and identify the score
    # This can include regular expressions or other text processing techniques
    # ...

    # For demonstration, assuming the score is the first number found in the text
    numbers = [int(s) for s in text.split() if s.isdigit()]
    if numbers:
        return numbers[0]
    else:
        return None

# Example usage
screenshot_path = 'path/to/your/screenshot.png'
score = extract_score_from_screenshot(screenshot_path)

if score is not None:
    print(f"The identified score is: {score}")
else:
    print("Score not found.")
