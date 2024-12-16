import os
import math

def split_file(input_file, chunk_size):
    """
    Splits the input file into smaller chunks with specified naming and formatting.
    Args:input_file (str): Path to the input file, chunk_size (int): Number of lines per chunk (excluding the header).
    """
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Get input file details
    input_filename = os.path.basename(input_file)
    input_file_extension = os.path.splitext(input_filename)[1][1:]  # Exclude the dot
    if not input_file_extension:
        input_file_extension = "unknown"

    output_dir = f"{os.path.splitext(input_filename)[0]} --) TYSM"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Initialize variables for chunking
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"Error: Unable to read the file '{input_file}'. {str(e)}")
        return

    if not lines:
        print(f"Error: The file '{input_file}' is empty.")
        return

    # Separate the header and the content
    header = lines[0]
    content = lines[1:]

    # Calculate the number of chunks
    total_lines = len(content)
    number_of_chunks = math.ceil(total_lines / chunk_size) + 1  # Including header chunk

    try:
        # Create 0.tysm with the header data
        header_chunk_name = os.path.join(output_dir, "0.tysm")
        with open(header_chunk_name, 'w') as header_chunk:
            header_chunk.write(f"<tysm>\"{input_file_extension}\",\"{number_of_chunks}\"</tysm>\n")
            header_chunk.write(header)

        # Create content chunks
        for i in range(0, total_lines, chunk_size):
            chunk_number = (i // chunk_size) + 1
            chunk_name = os.path.join(output_dir, f"{chunk_number}.tysm")
            with open(chunk_name, 'w') as chunk_file:
                chunk_file.writelines(content[i:i + chunk_size])

        print(f"File split into {number_of_chunks} chunks and stored in '{output_dir}'.")

    except Exception as e:
        print(f"Error: An error occurred while writing chunks. {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        input_file_path = input("Enter the path of the input file: ").strip()
        chunk_size = int(input("Enter the number of lines per chunk: ").strip())
        if chunk_size <= 0:
            print("Error: Chunk size must be a positive integer.")
        else:
            split_file(input_file_path, chunk_size)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number for the chunk size.")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
