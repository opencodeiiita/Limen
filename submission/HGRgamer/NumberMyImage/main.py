import base64
from PIL import Image
import os
import sys

def convert_image_to_base64(image_path):
    try:
        with Image.open(image_path) as img:
            print(f"Loaded image: {image_path}")
            
            # Ensure the image is in '1' mode (black and white)
            if img.mode != '1':
                print(f"Converting image to bitmap (1-bit black and white).")
                img = img.convert('1')
            
            # Get image dimensions
            width, height = img.size
            print(f"Image dimensions: {width}x{height}")
            
            # Extract pixel data and construct a binary string
            binary_string = ''
            for y in range(height):
                for x in range(width):
                    pixel = img.getpixel((x, y))
                    binary_string += '1' if pixel == 255 else '0'
            
            print("Binary string constructed successfully.")
            print(binary_string)
            
            # Convert binary string to decimal
            decimal_value = int(binary_string, 2)
            print("Converted binary string to decimal.")
            print(decimal_value)
            
            # Encode decimal value to base64
            base64_string = base64.b64encode(decimal_value.to_bytes((decimal_value.bit_length() + 7) // 8, byteorder='big')).decode('utf-8')
            print("Encoded decimal value to base64.")
            
            return base64_string
    
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    sys.set_int_max_str_digits(100000)

    #path to input image
    input_image = "image.png"

    if os.path.exists(input_image):
        try:
            base64_result = convert_image_to_base64(input_image)
            print("Base64 Representation:")
            print(base64_result)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"File {input_image} does not exist.")
