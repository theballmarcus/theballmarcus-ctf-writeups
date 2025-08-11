"""
Each character on a newline
Tabs = 1
"""
def char_to_custom_binary(char):
    """Convert a character to custom binary with tabs and null bytes."""
    binary = format(ord(char), '08b')  # 8-bit binary
    return ''.join('\t' if bit == '1' else '\x00' for bit in binary)

def encrypt_file_to_custom_binary(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read()
        
        with open(output_file, 'wb') as f:  # Write in binary mode
            for char in text:
                encoded_line = char_to_custom_binary(char) + '\n'
                f.write(encoded_line.encode('utf-8'))  # encode to bytes
        
        print(f"Encryption successful. Output saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Change these filenames as needed
    input_filename = 'flag.txt'
    output_filename = 'output_encrypted.txt'
    
    encrypt_file_to_custom_binary(input_filename, output_filename)
