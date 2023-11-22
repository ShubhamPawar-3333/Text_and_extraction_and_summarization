from PIL import Image
import pytesseract

def ocr_image(image_path):
    try:
        # open image using Pillow(PIL)
        with Image.open(image_path) as img:
            # Use pytesseract to perform OCR
            text = pytesseract.image_to_string(img)
            return text
        
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None