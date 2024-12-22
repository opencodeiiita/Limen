import os
import math
import logging
from pathlib import Path
import argparse

class Chunkify:
    def __init__(self, chunk_size_mb=10):
        self.chunk_size_mb = chunk_size_mb * 1024 * 1024
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def _validate_input_file(self, input_file):
        input_path = Path(input_file)
        if not input_path.exists():
            raise FileNotFoundError(f"Input file {input_file} does not exist.")

        if input_path.stat().st_size == 0:
            raise ValueError("Input file is empty.")

        return input_path

    def _get_file_extension(self, input_path):
        return input_path.suffix[1:] if input_path.suffix else ''

    def _create_output_directory(self, input_path):
        output_dir = input_path.parent / f"{input_path.stem} -> TYSM"
        output_dir.mkdir(exist_ok=True)
        return output_dir

    def chunkify(self, input_file):
        try:
            input_path = self._validate_input_file(input_file)
            output_dir = self._create_output_directory(input_path)
            file_extension = self._get_file_extension(input_path)
            file_size = input_path.stat().st_size
            total_chunks = math.ceil(file_size / self.chunk_size_mb)
            header_info = f'<tysm>"{file_extension}","{total_chunks}"</tysm>\n'
            chunks = []
            with open(input_path, 'rb') as f:
                first_chunk_path = output_dir / '0.tysm'
                with open(first_chunk_path, 'wb') as chunk_file:
                    chunk_file.write(header_info.encode())
                    first_chunk_data = f.read(self.chunk_size_mb - len(header_info))
                    chunk_file.write(first_chunk_data)
                chunks.append(first_chunk_path)
                chunk_counter = 1
                while True:
                    chunk_data = f.read(self.chunk_size_mb)
                    if not chunk_data:
                        break

                    chunk_path = output_dir / f'{chunk_counter}.tysm'
                    with open(chunk_path, 'wb') as chunk_file:
                        chunk_file.write(chunk_data)

                    chunks.append(chunk_path)
                    chunk_counter += 1

            self.logger.info(f"File split into {total_chunks} chunks successfully.")
            return chunks

        except Exception as e:
            self.logger.error(f"Chunkify failed: {e}")
            raise

def main():
    parser = argparse.ArgumentParser(description="Split a file into smaller chunks.")
    parser.add_argument(
        "input_file_path",
        type=str,
        help="Path to the input file that needs to be chunkified."
    )
    parser.add_argument(
        "--chunk_size_mb",
        type=int,
        default=10,
        help="Size of each chunk in MB (default: 10 MB)."
    )
    args = parser.parse_args()

    chunkifier = Chunkify(chunk_size_mb=args.chunk_size_mb)
    try:
        chunks = chunkifier.chunkify(args.input_file_path)
        print(f"Chunks created at: {chunks}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()