# Character list used for Caesar cipher encoding and decoding.
# Includes lowercase letters, uppercase letters, digits, special characters, and a space.

char_list = [
    # Lowercase alphabets
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    
    # Uppercase alphabets
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    
    # Digits
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    
    # Common special characters
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    
    # Additional symbols and punctuation
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ';', ':', '"', "'", '<', '>', ',', '.', '?', '/',
    
    # Space character
    ' '
]

# Documentation:
# 1. **Purpose**:
#    This `char_list` serves as the set of valid characters for the Caesar cipher program.
#    Each character's position in this list is used to calculate the shifted result during encoding or decoding.

# 2. **Categories of Characters**:
#    - Lowercase alphabets: 'a' to 'z'
#    - Uppercase alphabets: 'A' to 'Z'
#    - Digits: '0' to '9'
#    - Special characters: Includes common punctuation marks and symbols like `!`, `@`, `#`, `&`, etc.
#    - Space: Included as a character to preserve spaces in the text during encoding or decoding.

# 3. **How It Works in the Program**:
#    - During encoding/decoding, the character's position in this list is determined using `char_list.index(letter)`.
#    - The shift is applied, and the modulo operation ensures the index wraps around if it exceeds the length of the list.
#    - This ensures all characters, including uppercase letters and symbols, are processed consistently.

# 4. **Extensibility**:
#    - Additional characters can be added to the list if needed.
#    - The program dynamically adapts to any updates in `char_list`.
