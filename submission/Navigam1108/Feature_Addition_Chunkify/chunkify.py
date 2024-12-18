import os
import math

def chunkify(input_file, number_of_chunks):
    """
    Splits an input file into a specified number of chunks with naming and formatting.

    Args:
        input_file (str): Path to the input file.
        number_of_chunks (int): Total number of chunks to split the file into.

    Returns:
        None
    """
    try:
        # Valid input File
        if not os.path.isfile(input_file):
            print(f"Error: The file '{input_file}' does not exist.")
            return
        
        # Beacuse some people will do this
        if number_of_chunks <= 0:
            print("Invalid number of chunks. Must be positive integer")
            return

        # information Exctraxtion 
        input_file_name, input_file_extension = os.path.splitext(os.path.basename(input_file))
        if not input_file_extension:
            print("Warning: The input file has no extension.")

        # output directory needs to be changed if needed. specify ur path here
        output_dir = f'submission\\Navigam1108\\Feature_Addition_Chunkify\\output\\{input_file_name}_TYSM'

        # Output
        os.makedirs(output_dir, exist_ok=True)

        # store the content for file
        with open(input_file, 'rb') as file:
            file_content = file.read()

        total_size = len(file_content)

        if total_size == 0:
            print("Error: The input file is empty.")
            return

        chunk_size = math.ceil(total_size / number_of_chunks)

        # create the chunks 
        for i in range(number_of_chunks):
            start = i * chunk_size
            end = start + chunk_size
            chunk_data = file_content[start:end]

            # header for 0.tysm
            if i == 0:
                header = f'<tysm>"{input_file_extension[1:] if input_file_extension else "none"}","{number_of_chunks}"</tysm>\n'
                chunk_data = header.encode('utf-8') + chunk_data

            chunk_name = f"{i}.tysm"
            #output directory needs to change if to output_dir
            with open(os.path.join(output_dir, chunk_name), 'wb') as chunk_file:
                chunk_file.write(chunk_data)

        print(f"File successfully split into {number_of_chunks} chunks in directory: {output_dir}")

    except ValueError as ve:
        print(f"Error: Invalid input - {ve}")

    except Exception as e:
        print(f"Unexpected error: {e}")
