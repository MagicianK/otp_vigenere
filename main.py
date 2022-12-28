def otp_vigenere_encrypt(key, plaintext):
    # Initialize the encrypted message
    encrypted = ""

    # Encrypt the plaintext using the key
    for i in range(len(plaintext)):
        # Get the ASCII value of the character
        p = ord(plaintext[i])
        k = ord(key[i % len(key)])

        # Encrypt the character using the key
        encrypted += chr((p + k) % 26 + 65)

    return encrypted

def otp_vigenere_decrypt(key, encrypted):
    # Initialize the decrypted message
    decrypted = ""

    # Decrypt the encrypted message using the key
    for i in range(len(encrypted)):
        # Get the ASCII value of the character
        e = ord(encrypted[i])

        # If the character is not a letter, leave it unchanged
        if e < 65 or e > 90:
            decrypted += encrypted[i]
            continue

        # Decrypt the character using the key
        k = ord(key[i % len(key)])
        decrypted += chr((e - k + 26) % 26 + 65)

    return decrypted

# Prompt the user for the key and plaintext
key = input('Enter the key: ')
plaintext = input('Enter the plaintext: ')

# Encrypt the plaintext using the One Time Pad Vigenère cipher
encrypted = otp_vigenere_encrypt(key, plaintext)

# Decrypt the encrypted message using the One Time Pad Vigenère cipher
decrypted = otp_vigenere_decrypt(key, encrypted)

# Print the encrypted and decrypted messages
print('Encrypted message:', encrypted)
print('Decrypted message:', decrypted)
