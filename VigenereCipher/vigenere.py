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


def decrypt(message: str, keyword: str) -> str:
    """
    Decrypts message which was encrypted with Vigenere Cipher using the provided keyword
    :param message: str
    :param keyword: str, upper-case English letters
    :return: str
    """
    return ""


def apply_vigenere(is_encrypt: bool, message: str, key: str) -> str:
    """
    just a helper method
    """
    return encrypt(message, key) if is_encrypt else decrypt(message, key)


def get_inverse_key(keyword: str) -> str:
    """
    computes the inverse key
    :param keyword: str, upper-case English letters
    :return: str
    """
    inverse_key = ""
    for char in keyword:
        inverse_key += chr((26 - (ord(char) - 65)) % 26 + 65)

    return inverse_key
