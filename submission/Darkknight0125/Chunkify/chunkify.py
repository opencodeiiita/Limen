import os

def split_file(input_file, chunk_size=1024):
    """
    Args:
        input_file (str): Path to the input file.
        chunk_size (int): Size (in bytes) of each chunk, default is 1KB.
    """

    # First error check here
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return
    
    # Extract file details
    file_name, file_extension = os.path.splitext(os.path.basename(input_file))
    file_extension = file_extension.lstrip(".") if file_extension else "none"
    output_directory = f"{file_name} -> TYSM"

    os.makedirs(output_directory, exist_ok=True)

    # Open input file and split it into chunks
    try:
        with open(input_file, "rb") as infile:

            chunk_count = 0
            
            # Write header chunk
            first_chunk_name = os.path.join(output_directory, "0.tysm")
            with open(first_chunk_name, "wb") as header_chunk:
                header_content = f'<tysm>"{file_extension}",'
                header_chunk.write(header_content.encode())

            # Write remaining chunks
            while True:
                data = infile.read(chunk_size)
                if not data:
                    break  # End of file
                chunk_count += 1
                chunk_name = os.path.join(output_directory, f"{chunk_count}.tysm")
                with open(chunk_name, "wb") as chunk_file:
                    chunk_file.write(data)

            # Update the header chunk with the total chunk count
            with open(first_chunk_name, "ab") as header_chunk:
                header_chunk.write(f'"{chunk_count}"</tysm>'.encode())

        print(f"File split successfully into {chunk_count + 1} chunks.")
        print(f"Chunks are stored in: {output_directory}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_file_path = input("Enter the input file path: ").strip()
    split_file(input_file_path, chunk_size=1024 * 1024)  # 1MB chunks
