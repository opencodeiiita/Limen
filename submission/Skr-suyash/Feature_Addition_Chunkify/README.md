# File Chunkifier

A Python script that splits a file into a specified number of chunks and saves them in a new directory. The script calculates the appropriate chunk size based on the total file size and the desired number of chunks.

## Features

- **Splits a file** into a user-defined number of chunks.
- **Dynamically calculates chunk size** based on the file's total size and the number of chunks.
- **Handles large files** efficiently by reading and writing chunks.
- **Adds a header** to the first chunk with metadata such as the file extension and the total number of chunks.
- **Creates a new directory** to store the resulting chunks.

## Requirements

- Python 3.x
- No external libraries are required.

## Usage

To run the script, use the following command in your terminal or command prompt:

```bash
python chunkify.py <input_file> <num_chunks>
```

## Testing

```bash
python chunkify.py test.txt 10
```
