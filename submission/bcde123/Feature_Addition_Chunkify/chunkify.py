import os
import shutil

def split_file(input_file):
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    input_file_name, input_file_extension = os.path.splitext(input_file)
    input_file_extension = input_file_extension.lstrip('.')

    if not input_file_extension:
        input_file_extension = 'no_extension'

    output_dir = f"{input_file_name} -> TYSM"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r') as file:
        lines = file.readlines()

    chunk_size = 1000
    total_chunks = (len(lines) // chunk_size) + (1 if len(lines) % chunk_size != 0 else 0)

    first_chunk_name = os.path.join(output_dir, "0.tysm")
    with open(first_chunk_name, 'w') as chunk_file:
        chunk_file.write(f'<tysm>"{input_file_extension}", "{total_chunks}"</tysm>\n')
        chunk_file.writelines(lines[:chunk_size])

    for i in range(1, total_chunks):
        chunk_name = os.path.join(output_dir, f"{i}.tysm")
        with open(chunk_name, 'w') as chunk_file:
            start_line = i * chunk_size
            end_line = start_line + chunk_size
            chunk_file.writelines(lines[start_line:end_line])

    print(f"File '{input_file}' has been successfully split into {total_chunks} chunks.")
    print(f"Chunks are stored in the directory: '{output_dir}'")

if __name__ == "__main__":
    input_file = input("Enter the path of the file to split: ")
    split_file(input_file)