"""
Decrypts a file encoded with the custom binary format as output by `cat -vET`:
- Each character is encoded as 8 bits (one line per character)
- Tab ('^I') = binary 1
- Null byte ('^@') = binary 0
- End of line: '$\n' (from `cat -vET`)
"""

def custom_catvET_line_to_char(line):
    # Remove end-of-line marker from `cat -vET` ('$' at end, then newline)
    line = line.rstrip('\n').rstrip('$')
    bits = []
    # Each line should have 8 symbols: ^@ or ^I
    for chunk in [line[i:i+2] for i in range(0, len(line), 2)]:
        if chunk == '^I':
            bits.append('1')
        elif chunk == '^@':
            bits.append('0')
        else:
            # Ignore unexpected characters (robustness)
            continue
    if len(bits) != 8:
        raise ValueError(f"Expected 8 bits, got {len(bits)}: {bits}")
    return chr(int(''.join(bits), 2))

def decrypt_file_from_catvET(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                char = custom_catvET_line_to_char(line)
                f.write(char)
        
        print(f"Decryption successful. Output saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Change these filenames as needed
    input_filename = 'output_encrypted.txt'
    output_filename = 'output_decrypted.txt'
    
    decrypt_file_from_catvET(input_filename, output_filename)
