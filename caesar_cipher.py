#!/usr/bin/env python3
# caesar_cipher.py

def caesar_encrypt(text, shift):
    """
    Shift each letter in `text` forward by `shift` positions.
    Non‑letters are left unchanged.  `shift` can be any integer.
    """
    shift = shift % 26
    output = ""
    for ch in text:
        code = ord(ch)
        if 65 <= code <= 90:        # uppercase A–Z
            output += chr((code - 65 + shift) % 26 + 65)
        elif 97 <= code <= 122:     # lowercase a–z
            output += chr((code - 97 + shift) % 26 + 97)
        else:
            output += ch            # other characters unchanged
    return output

def caesar_decrypt(text, shift):
    """
    Reverse of encrypt: shift letters backward by `shift`.
    """
    return caesar_encrypt(text, -shift)

def main():
    # let the user choose to encrypt or decrypt
    mode = input("Type 'e' to encrypt or 'd' to decrypt: ").strip().lower()
    text = input("Enter your text: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if mode == 'e':
        result = caesar_encrypt(text, shift)
        print("\nEncrypted text:")
    elif mode == 'd':
        result = caesar_decrypt(text, shift)
        print("\nDecrypted text:")
    else:
        print("Invalid selection; please use 'e' or 'd'.")
        return

    print(result)

if __name__ == '__main__':
    main()
