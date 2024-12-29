from PIL import Image
import base64
import os

def convert_to_bitmap(image_path):
    """
    Converts the input image to a black and white bitmap format.
    Returns the converted image.
    """
    try:
        image = Image.open(image_path).convert('1')  # Convert to 1-bit bitmap (black and white)
        print(f"Image successfully converted to bitmap: {image_path}")
        return image
    except Exception as e:
        print(f"Failed to convert image to bitmap: {e}")
        raise

def image_to_binary_string(bitmap):
    """
    Converts a bitmap image into a binary string where 0 represents black and 1 represents white.
    """
    binary_string = ''.join(['0' if pixel == 0 else '1' for pixel in bitmap.getdata()])
    print("Image successfully converted to binary string.")
    return binary_string

def binary_to_base64(binary_string):
    """
    Converts a binary string to its decimal equivalent and encodes it in base64.
    """
    decimal_representation = int(binary_string, 2)  # Convert binary string to decimal
    base64_encoded = base64.b64encode(decimal_representation.to_bytes((decimal_representation.bit_length() + 7) // 8, 'big')).decode('utf-8')
    print("Binary string successfully encoded to base64.")
    return base64_encoded

def save_or_print_result(base64_string, output_path=None):
    """
    Outputs the base64 string either to a file or prints it.
    """
    if output_path:
        try:
            with open(output_path, 'w') as f:
                f.write(base64_string)
            print(f"Base64 string saved to file: {output_path}")
        except Exception as e:
            print(f"Failed to save base64 string to file: {e}")
            raise
    else:
        print(base64_string)
        print("Base64 string printed to console.")

def main(image_path, output_path=None):
    """
    Main function to handle the conversion process.
    
    Usage:
    python NumberMyImage.py <image_path> [--output <output_path>]

    Arguments:
    image_path: Path to the input image file (required).
    --output: Optional path to save the base64 encoded output. If not provided, the result is printed to the console.
    """
    try:
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"Input file not found: {image_path}")

        bitmap = convert_to_bitmap(image_path)
        binary_string = image_to_binary_string(bitmap)
        base64_string = binary_to_base64(binary_string)
        save_or_print_result(base64_string, output_path)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert a black and white bitmap image to a base64 string.")
    parser.add_argument('image_path', type=str, help="Path to the input image file.")
    parser.add_argument('--output', type=str, default=None, help="Path to save the base64 output (optional).")

    args = parser.parse_args()
    main(args.image_path, args.output)
