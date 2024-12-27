import base64
from PIL import Image
import os
import logging
import sys

# Configure logging for debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def convert_image_to_base64(image_path: str) -> str:
    """
    Converts a black-and-white bitmap image to a numerical representation and encodes it in base64.

    Parameters:
        image_path (str): Path to the input image.

    Returns:
        str: Base64-encoded representation of the image.
    """
    try:
        # Check if the file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")

        # Open the image
        logging.info("Opening image...")
        img = Image.open(image_path)

        # Convert to bitmap (mode "1" for black-and-white)
        logging.info("Converting image to black-and-white bitmap...")
        img = img.convert("1")

        # Get pixel data
        logging.info("Extracting pixel data...")
        pixels = list(img.getdata())
        
        # Create a binary string where black = 0, white = 1
        logging.info("Converting pixel data to binary...")
        binary_string = "".join("0" if pixel == 0 else "1" for pixel in pixels)

        # Split the binary string into manageable chunks
        chunk_size = 4000
        logging.info(f"Splitting binary string into chunks of size {chunk_size}...")
        decimal_chunks = [int(binary_string[i:i + chunk_size], 2) for i in range(0, len(binary_string), chunk_size)]

        # Encode each chunk to base64 and combine them
        logging.info("Encoding chunks to base64...")
        base64_chunks = [base64.b64encode(str(chunk).encode()).decode() for chunk in decimal_chunks]
        base64_string = "".join(base64_chunks)

        logging.info("Conversion successful!")
        return base64_string

    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
        return "Error: File not found."
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return f"Error: {e}"


def save_base64_to_file(base64_string: str, output_file: str):
    """
    Saves the base64 string to a file.

    Parameters:
        base64_string (str): Base64-encoded string.
        output_file (str): Path to the output file.
    """
    try:
        logging.info(f"Saving base64 string to {output_file}...")
        with open(output_file, "w") as f:
            f.write(base64_string)
        logging.info("Base64 string saved successfully!")
    except Exception as e:
        logging.error(f"Failed to save base64 string: {e}")


if __name__ == "__main__":
    # Input image file path
    input_image_path = input("Enter the path to the image file: ")

    # Output file to save the base64 string
    output_file_path = input("Enter the path to save the base64 string (e.g., output.txt): ")

    # Increase integer string conversion limit for large images
    sys.set_int_max_str_digits(100000)

    # Convert image to base64
    base64_result = convert_image_to_base64(input_image_path)

    if "Error" not in base64_result:
        # Save the result to a file
        save_base64_to_file(base64_result, output_file_path)
        print(f"Base64 string saved to {output_file_path}.")
    else:
        # Print the error
        print(base64_result)
