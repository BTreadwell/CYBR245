UPPER_OFFSET = 65
LOWER_OFFSET = 97


def encrypt(message: str, keyword: str) -> str:
    """
    Encrypts a message using the Vigenere cipher with the provided keyword
    :param message: str
    :param keyword: str, upper-case English characters
    :return: str
    """

    ciphertext = ""
    for idx, char in enumerate(message):
        char_ascii = ord(char)
        shift = ord(keyword[idx % len(keyword)]) - UPPER_OFFSET

        if char.isupper():
            ciphertext += chr(((char_ascii - UPPER_OFFSET) + shift) % 26 + UPPER_OFFSET)
        elif char.islower():
            ciphertext += chr(((char_ascii - LOWER_OFFSET) + shift) % 26 + LOWER_OFFSET)
        else:
            ciphertext += char

    return ciphertext

