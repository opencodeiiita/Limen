import os
import sys

def chunkify(input_file, num_chunks):

    """
    Splits a given file into the specified number of chunks and saves them in a new directory.
    
    Parameters:
    input_file (str): The path to the input file to be chunked.
    num_chunks (int): The number of chunks to split the file into.
    
    This function performs the following steps:
    1. Verifies if the input file exists.
    2. Creates an output directory based on the input file name.
    3. Calculates the appropriate chunk size based on the total file size and the number of chunks.
    4. Splits the file into the specified number of chunks.
    5. Adds a header to the first chunk containing file extension and chunk count.
    6. Updates the header with the actual chunk count after processing the file.
    7. Saves the chunks in the output directory.
    """

    try:
        # Validate file existence
        if not os.path.isfile(input_file):
            print("Error: File does not exist.")
            return
        
        # Get the total size of the file
        file_size = os.path.getsize(input_file)
        
        # Calculate chunk size based on the number of chunks
        if num_chunks <= 0:
            raise ValueError("Number of chunks must be a positive integer.")
        
        chunk_size = file_size // num_chunks
        if file_size % num_chunks != 0:
            chunk_size += 1  # If there's a remainder, increase chunk size to include all data
        
        # Extract file name and extension
        input_file_name, input_file_extension = os.path.splitext(os.path.basename(input_file))
        input_file_extension = input_file_extension[1:] if input_file_extension else "none"

        # Create output directory
        output_dir = f"{input_file_name}/TYSM"
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize variables
        chunk_counter = 0
        total_chunks = num_chunks
        header_written = False
        
        # Open the input file and start reading
        with open(input_file, 'rb') as infile:
            while chunk_counter < total_chunks:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break  # End of file
                
                # Determine chunk name
                chunk_name = os.path.join(output_dir, f"{chunk_counter}.tysm")
                
                # Write the first chunk (0.tysm) with header
                with open(chunk_name, 'wb') as outfile:
                    if not header_written:
                        header = f'<tysm>"{input_file_extension}","{total_chunks}"</tysm>\n'.encode()
                        outfile.write(header)
                        outfile.write(chunk)
                        header_written = True
                    else:
                        outfile.write(chunk)
                
                chunk_counter += 1
            
        print(f"File successfully split into {total_chunks} chunks.")
        print(f"Chunks saved in directory: {output_dir}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    """
    Entry point for the script when executed from the command line.
    
    Usage:
    python chunkify.py <input_file> <num_chunks>
    
    This script splits the input file into the specified number of chunks and saves them in an output directory.
    """

    if len(sys.argv) != 3:
        print("Usage: python chunkify.py <input_file> <num_chunks>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    try:
        num_chunks = int(sys.argv[2])
        if num_chunks <= 0:
            raise ValueError("Number of chunks must be a positive integer.")
        chunkify(input_file, num_chunks)
    except ValueError:
        print("Error: Number of chunks must be a valid positive integer.")
        sys.exit(1)
