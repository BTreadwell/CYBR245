import vigenere


def main():
    is_encrypt = input("Would you like to encrypt (e) or decrypt (d): ").strip().upper() == 'E'

    message = input("Enter the message: ")
    key = input("Enter the encryption key: ").upper()

    while not key.isalpha():
        print("Key must contain only alphabetic characters A-Z")
        key = input("Enter the encryption key: ").upper()

    new_message = vigenere.apply_vigenere(is_encrypt, message, key)

    print("The result of applying the Vigenere Cipher with the provided parameters is:\n" + new_message)


if __name__ == "__main__":
    main()
