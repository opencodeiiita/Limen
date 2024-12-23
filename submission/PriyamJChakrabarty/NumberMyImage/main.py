import base64
import os
from PIL import Image

def convert_image_to_bitmap(image_path):
    """
    Converts an image to bitmap format (black and white).
    Returns the bitmap image object.
    """
    try:
        image = Image.open(image_path)
        bitmap = image.convert("1")  # Convert to black and white
        return bitmap
    except Exception as e:
        raise ValueError(f"Error converting image to bitmap: {e}")

def bitmap_to_binary_string(bitmap):
    """
    Converts a bitmap image to a binary string based on pixel values.
    """
    binary_string = ""
    width, height = bitmap.size

    for y in range(height):
        for x in range(width):
            pixel = bitmap.getpixel((x, y))
            binary_string += "0" if pixel == 0 else "1"  # 0 for black, 1 for white

    return binary_string

def binary_to_base64(binary_string):
    """
    Converts a binary string to a base64 encoded string.
    """
    decimal_value = int(binary_string, 2)  # Convert binary to decimal
    decimal_bytes = decimal_value.to_bytes((decimal_value.bit_length() + 7) // 8, byteorder="big")
    base64_encoded = base64.b64encode(decimal_bytes).decode("utf-8")
    return base64_encoded

def number_my_image(image_path, output_path=None):
    """
    Converts a black and white bitmap image to its base64 representation.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError("The specified image file does not exist.")

    try:
        # Convert to bitmap
        bitmap = convert_image_to_bitmap(image_path)

        # Convert bitmap to binary string
        binary_string = bitmap_to_binary_string(bitmap)

        # Convert binary string to base64
        base64_string = binary_to_base64(binary_string)

        # Output the result
        if output_path:
            with open(output_path, "w") as f:
                f.write(base64_string)
        else:
            print("Base64 representation:", base64_string)

        return base64_string

    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert a black and white image to its base64 numerical representation.")
    parser.add_argument("image_path", type=str, help="Path to the input image.")
    parser.add_argument("--output", type=str, default=None, help="Path to save the output base64 string.")

    args = parser.parse_args()

    try:
        number_my_image(args.image_path, args.output)
    except Exception as e:
        print(f"Error: {e}")
