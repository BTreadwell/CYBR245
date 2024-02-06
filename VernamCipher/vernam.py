def encrypt(plaintext, keyword):
    # assume the plaintext and the keyword have the same length

    ciphertext = ""
    for idx in range(len(plaintext)):
        ptext_char = plaintext[idx]
        key_char = keyword[idx]

        if ptext_char.isalpha():

            is_upper = ptext_char.isupper()
            if is_upper:
                ptext_val = ord(ptext_char) - 65
            else:
                ptext_val = ord(ptext_char) - 97

            key_val = ord(key_char) - 65

            encrypted_val = ptext_val ^ key_val

            if is_upper:
                encrypted_char = chr(encrypted_val + 65)
            else:
                encrypted_char = chr(encrypted_val + 97)

            ciphertext += encrypted_char

    return ciphertext


def main():
    print(encrypt("HELLOhello", "ABCDEABCDE"))


if __name__ == "__main__":
    main()
