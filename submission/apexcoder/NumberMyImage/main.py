from PIL import Image, UnidentifiedImageError
import base64
import os
import io

def convert_to_bitmap(image_path):
    """
    Convert an input image to a 1-bit black and white bitmap.

    :param image_path: Path to the input image.
    :return: 1-bit PIL Image object.
    :raises: ValueError if the image cannot be processed.
    """
    try:
        img = Image.open(image_path)
        img = img.convert('1')  # Convert to 1-bit black and white
        return img
    except UnidentifiedImageError:
        raise ValueError("Invalid image file or unsupported format.")
    except Exception as e:
        raise ValueError(f"Error during image conversion: {str(e)}")

def bitmap_to_binary_string(bitmap):
    """
    Convert a bitmap image to a binary string.

    :param bitmap: PIL Image object in 1-bit format.
    :return: Binary string representing the bitmap.
    """
    width, height = bitmap.size
    binary_string = ''.join(
        '1' if bitmap.getpixel((x, y)) else '0' 
        for y in range(height) 
        for x in range(width)
    )
    return binary_string

def binary_string_to_base64(binary_string):
    """
    Convert a binary string to its base64 representation.

    :param binary_string: Binary string to encode.
    :return: Base64 encoded string.
    """
    decimal_representation = int(binary_string, 2)
    byte_length = (decimal_representation.bit_length() + 7) // 8
    decimal_bytes = decimal_representation.to_bytes(byte_length, 'big')
    return base64.b64encode(decimal_bytes).decode('utf-8')

def process_image(image_path, output_path=None):
    """
    Process an image by converting it to bitmap, extracting binary data, and encoding to base64.

    :param image_path: Path to the input image.
    :param output_path: Path to save the base64 string (optional).
    :return: None
    """
    try:
        # Step 1: Convert image to bitmap
        bitmap = convert_to_bitmap(image_path)

        # Step 2: Extract binary string from bitmap
        binary_string = bitmap_to_binary_string(bitmap)

        # Step 3: Encode binary string to base64
        base64_string = binary_string_to_base64(binary_string)

        # Output or save result
        if output_path:
            with open(output_path, 'w') as f:
                f.write(base64_string)
            print(f"Base64 string saved to {output_path}")
        else:
            print(base64_string)
    except ValueError as e:
        print(f"[Error] {str(e)}")
    except Exception as e:
        print(f"[Unexpected Error] {str(e)}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert a black and white bitmap image to a base64 encoded string.")
    parser.add_argument('image_path', help="Path to the input image.")
    parser.add_argument('--output', help="Optional path to save the base64 string.")
    args = parser.parse_args()

    process_image(args.image_path, args.output)
