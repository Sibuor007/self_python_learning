import string
"""
module to create a caesar's cipher
"""
# creating a list of all alphabetical characters in lowercase
alphabet = list(string.ascii_lowercase)
# printing the created alphabet letters
print(alphabet)


def encryption(plain_text, shift_key):
    """
    a function that recieves plain text and shift key
    the function iterates through the plain text and finds it's index in the list
    Args:
        plain_text (str): string
        shift_key (int): the key
    Return:
        No return value
    """
    # taking an empty string object
    cipher_text = ""
    for char in plain_text:
        # checks if the character is an alphabet
        if char in alphabet:
            position = alphabet.index(char)
            # finds a new position from where the new xchar will be obtained
            new_position = (position + shift_key) % 26
            # adding the new character from the new index to the empty string
            cipher_text += alphabet[new_position]
        else:
            # adding any other characters to the string not present in alphabet
            cipher_text += char
    # printing the final result of the encrypted text using the string.format
    print(f"Text after encryption: {cipher_text}")


def decryption(cipher_text, shift_key):
    """
    a function that recieves cipher text and shift key
    the function iterates through the cipher text and finds it's index in the list
    Args:
        cipher_text (str): string
        shift_key (int): the key
    Return:
        No return value
    """
    plain_text = ""
    for char in cipher_text:
        # iterating through every character in the encrypted text
        if char in alphabet:
            # finding the index of the letter in the list
            position = alphabet.index(char)
            # finding the new position, depending the shift key
            new_position = (position - shift_key) % 26
            # adding the new found letters to the empty string object
            plain_text += alphabet[new_position]
        else:
            # adds any other characters not present in the alphabet to the new string
            plain_text += char
    # prints the decrypted text
    print(f"Text after encryption: {plain_text}")


# a flag to break the loop when user wants to exit
flag = False

while not flag:
    # a loop to ensure only encrypt and decrypt are typed
    while True:
        what_to_do = input("Type 'encrypt' for encryption and 'decrypt' for decryption.")
        if what_to_do in ('encrypt', 'decrypt'):
            break
    # gets text and shift key from user
    text_ = input("Type your message: \n").lower()
    shift_ = int(input("Enter shift key: \n"))

    # allows user to select the action to be executed
    if what_to_do == 'encrypt':
        encryption(plain_text=text_, shift_key=shift_)

    elif what_to_do == 'decrypt':
        decryption(text_, shift_)

    # asks the user if they want to continue
    continue_ = input("Type 'yes' to continue, 'no' to exit.")
    if continue_ == 'no':
        # the loop breaks and program exits if 'no' us typed
        flag = True
        # prints a goodbye message to the user/console
        print('Goodbye!')
