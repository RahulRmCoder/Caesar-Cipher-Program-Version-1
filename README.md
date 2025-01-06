# Caesar Cipher Program Version 1

This project implements a Caesar cipher program for encoding and decoding text. The cipher works by shifting each character in the text by a specified number of positions. The program supports lowercase and uppercase letters, digits, special characters, and spaces.

## Features

- **Encoding and Decoding**: Easily encrypt or decrypt messages.
- **Customizable Shift**: Users can specify the number of positions to shift characters.
- **Support for Extended Characters**: Handles alphabets (both cases), digits, special characters, and spaces.
- **ASCII Art Logo**: Displays an ASCII art logo on startup.
- **Robust Input Validation**: Ensures valid inputs for encoding/decoding directions.
- **Reusable Character List**: Dynamically adaptable to any updates in the character set.

## Files in the Project

### 1. `main.py`
This is the main program file that:
- Displays the logo.
- Accepts user inputs for encoding or decoding.
- Processes text using the Caesar cipher function.
- Allows the user to run the program multiple times.

### 2. `art.py`
Contains the ASCII art logo for the program.
```python
logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     Y8 a8P_____88 I8[    "" ""     Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  "Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 "Ybbd8"' "8bbdP"Y8  "Ybbd8"' "YbbdP"' "8bbdP"Y8 88
            88             88                                
           ""             88                                
                          88                                
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 "Ybbd8"' 88 88YbbdP"'  88       88  "Ybbd8"' 88
              88                                             
              88                                             
"""
```

### 3. `characters.py`
Defines the `char_list` used for encoding and decoding.
```python
char_list = [
    # Lowercase alphabets
    'a', 'b', 'c', ..., 'z',

    # Uppercase alphabets
    'A', 'B', 'C', ..., 'Z',

    # Digits
    '0', '1', ..., '9',

    # Special characters
    '!', '@', '#', ..., '/',

    # Space character
    ' '
]
```

## How the Program Works

1. **Prompt for Action**: The program prompts the user to type `encode` to encrypt or `decode` to decrypt.
2. **Input Text**: The user provides the text to be processed.
3. **Shift Value**: The user specifies the number of positions to shift the characters.
4. **Process the Text**:
   - Characters not in `char_list` remain unchanged.
   - Characters are shifted, wrapping around the list when necessary.
5. **Display the Result**: The program outputs the encoded or decoded message.
6. **Repeat or Exit**: Users can choose to run the program again or exit.

## Example Usage

### Encoding Example
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello, World!
Type the shift number:
5
Here is the encoded result: Mjqqt, Btwqi!
```

### Decoding Example
```
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
Mjqqt, Btwqi!
Type the shift number:
5
Here is the decoded result: Hello, World!
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RahulRmCoder/Caesar-Cipher-Program-Version-1.git
   ```
2. Navigate to the project directory:
   ```bash
   cd caesar-cipher-program-version-1
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Customization
- To modify the supported characters, edit the `char_list` in `characters.py`.
- You can update the ASCII art in `art.py` to personalize the logo.

## Future Improvements
- Add support for multiple languages.
- Enhance the user interface with a graphical option.
- Implement a feature to save and load encoded messages.

## License
This project is open source and available under the [MIT License](LICENSE).



