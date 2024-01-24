import string

alphabet = list(string.ascii_lowercase)
print(alphabet)


def encryption(plain_text, shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Text after encryption: {cipher_text}")


def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key) % 26
            plain_text += alphabet[new_position]
        else:
            plain_text += char
    print(f"Text after encryption: {plain_text}")


flag = False

while not flag:
    while True:
        what_to_do = input("Type 'encrypt' for encryption and 'decrypt' for decryption.")
        if what_to_do in ('encrypt', 'decrypt'):
            break

    text_ = input("Type your message: \n").lower()
    shift_ = int(input("Enter shift key: \n"))

    if what_to_do == 'encrypt':
        encryption(plain_text=text_, shift_key=shift_)

    elif what_to_do == 'decrypt':
        decryption(text_, shift_)

    continue_ = input("Type 'yes' to continue, 'no' to exit.")
    if continue_ == 'no':
        flag = True
        print('Goodbye!')
