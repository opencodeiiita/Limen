import os
import math
import re

def chunkify(input_file, chunk_size=1024):
    try:
        if not os.path.isfile(input_file):
            print("Error: Input file does not exist.")
            return
        
        input_file_name, input_file_extension = os.path.splitext(os.path.basename(input_file))
        input_file_extension = input_file_extension.lstrip('.') or 'unknown'
        
        output_dir = re.sub(r'[<>:"/\\|?*]', '_', f"{input_file_name} -> TYSM")
        os.makedirs(output_dir, exist_ok=True)
        
        with open(input_file, 'rb') as f:
            file_data = f.read()
        
        file_size = len(file_data)
        number_of_chunks = math.ceil(file_size / chunk_size)
        
        header = f'<tysm>"{input_file_extension}","{number_of_chunks}"</tysm>\n'
        with open(os.path.join(output_dir, "0.tysm"), 'wb') as header_file:
            header_file.write(header.encode('utf-8'))
            header_file.write(file_data[:chunk_size])
        
        for i in range(1, number_of_chunks):
            chunk_data = file_data[i * chunk_size:(i + 1) * chunk_size]
            chunk_file_name = os.path.join(output_dir, f"{i}.tysm")
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk_data)
        
        print(f"File successfully split into {number_of_chunks} chunks.")
        print(f"Chunks are stored in the directory: {output_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_path = r'C:\Users\krish\Limen\krishnamohan2006\sample.txt'
    chunkify(input_file_path, chunk_size=1024)  
