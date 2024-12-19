import os
import math

def chunkify(input_file):
    # input info
    input_filename, input_extension = os.path.splitext(input_file)
    input_extension = input_extension.lstrip('.')

    # Create output dir
    output_dir = f"{input_filename} -> TYSM"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        lines = file.readlines()

    chunk_size = 2000  # each chunk stores x lines, can change it
    total_lines = len(lines)
    chunks = (total_lines // chunk_size) + (1 if total_lines % chunk_size else 0)

    # first chunk header
    header = f'<tysm>"{input_extension}","{chunks}"</tysm>\n'
    
    for i in range(0, chunks):
        start_index = i * chunk_size
        end_index = min(start_index + chunk_size, total_lines)

        chunk_content = lines[start_index:end_index]
        if(i == 0):
            chunk_content = [header] + chunk_content
        
        with open(f"{output_dir}/{i}.tysm", 'w') as chunk_file:
            chunk_file.writelines(chunk_content)

    print(f"File has been split into {chunks} chunks in directory '{output_dir}'.")

input_file = "test.txt"
chunkify(input_file)
