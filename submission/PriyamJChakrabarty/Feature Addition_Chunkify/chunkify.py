import os
import sys

def chunkify_file(input_file, num_chunks):
    """
    Splits a given file into smaller chunks and saves them with specific naming and header formatting.

    Parameters:
    input_file (str): Path to the input file to be chunked.
    num_chunks (int): Number of chunks to split the file into.

    """
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file):
            print("Error: File does not exist.")
            return

        # Get file size and calculate chunk size
        file_size = os.path.getsize(input_file)
        if num_chunks <= 0:
            raise ValueError("Number of chunks must be a positive integer.")

        chunk_size = file_size // num_chunks
        if file_size % num_chunks != 0:
            chunk_size += 1  # Ensure all data is included

        # Extract file name and extension
        input_file_name, input_file_extension = os.path.splitext(os.path.basename(input_file))
        input_file_extension = input_file_extension[1:] if input_file_extension else "none"

        # Create output directory
        output_dir = f"{input_file_name} - TYSM"
        os.makedirs(output_dir, exist_ok=True)

        # Initialize variables
        chunk_counter = 0
        header_written = False

        # Open the input file for reading
        with open(input_file, 'rb') as infile:
            while chunk_counter < num_chunks:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break  # End of file

                # Define chunk file name
                chunk_name = os.path.join(output_dir, f"{chunk_counter}.tysm")

                # Write chunk with header if first chunk
                with open(chunk_name, 'wb') as outfile:
                    if not header_written:
                        header = f'<tysm>"{input_file_extension}","{num_chunks}"</tysm>\n'.encode()
                        outfile.write(header)
                        header_written = True

                    outfile.write(chunk)

                chunk_counter += 1

        print(f"File successfully split into {chunk_counter} chunks.")
        print(f"Chunks saved in directory: {output_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Entry point for the script when executed from the command line.

    Usage:
    python chunkify.py <input_file> <num_chunks>
    """
    if len(sys.argv) != 3:
        print("Usage: python chunkify.py <input_file> <num_chunks>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        num_chunks = int(sys.argv[2])
        if num_chunks <= 0:
            raise ValueError("Number of chunks must be a positive integer.")
        chunkify_file(input_file, num_chunks)
    except ValueError:
        print("Error: Number of chunks must be a valid positive integer.")
        sys.exit(1)
