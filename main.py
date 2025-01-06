# Importing the logo and the character list
from art import logo
from charecters import char_list

# Displaying the program's logo
print(logo)

# Function to perform the Caesar cipher encoding or decoding
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""  # Initialize the output text

    # Reverse the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Iterate through each character in the input text
    for letter in original_text:
        # If the character is not in the character list, leave it unchanged
        if letter not in char_list:
            output_text += letter
        else:
            # Calculate the new position of the character
            shifted_position = char_list.index(letter) + shift_amount
            shifted_position %= len(char_list)  # Ensure the position wraps around the list
            output_text += char_list[shifted_position]  # Add the shifted character to the output

    # Print the result (encoded or decoded)
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main program loop to allow multiple uses
try_again = True
while try_again:
    # Prompt the user for encode/decode direction
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    # Validate the input for direction
    if direction != 'encode' and direction != 'decode':
        print("Invalid Input")  # Notify the user of invalid input
    else:
        # Get the message to process and the shift amount
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))

        # Call the Caesar cipher function with the provided inputs
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to continue
    restart = input("Do you want to continue (Y/N): ").lower()

    # If the user inputs 'n', exit the loop
    if restart == 'n':
        try_again = False
        print("Thank You!")  # Display a closing message
