from string import ascii_lowercase

LOWER_OFFSET = 97
UPPER_OFFSET = 65


def encrypt(plaintext: str, key: int) -> str:
    """
    Simple, easy-to-read implementation of the Caesar Cipher
    Encrypts upper- and lower-case English letters.
    :param plaintext: str
    :param key: int
    :return: str
    """

    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            char = ord(char) - UPPER_OFFSET
            char = (char + key) % 26
            char = char + UPPER_OFFSET
            ciphertext += chr(char)
        elif char.islower():
            char = ord(char) - LOWER_OFFSET
            char = (char + key) % 26
            char = char + LOWER_OFFSET
            ciphertext += chr(char)
        else:
            ciphertext += char

    return ciphertext


def encrypt_compact(plaintext: str, key: int) -> str:
    """
    Same as 'encrypt' but doesn't break up encryption step
    :param plaintext: str
    :param key: int
    :return: str
    """

    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) - UPPER_OFFSET + key) % 26 + UPPER_OFFSET)
        elif char.islower():
            ciphertext += chr((ord(char) - LOWER_OFFSET + key) % 26 + LOWER_OFFSET)
        else:
            ciphertext += char

    return ciphertext


def encrypt_comprehension(plaintext: str, key: int) -> str:
    """
    Caesar Shift for upper case characters only using list comprehension
    :param plaintext: str
    :param key: int
    :return: str
    """

    acceptable_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(
        [chr((ord(char) - UPPER_OFFSET + key) % 26 + UPPER_OFFSET) if char in acceptable_chars else char for char in
         plaintext])


def encrypt_bitwise(plaintext: str, key: int) -> str:
    """
    Caesar Cipher implementation using byte arrays
    :param plaintext: str
    :param key: int
    :return: str
    """

    # convert to bytearrays
    message_bytes = bytearray(plaintext, encoding='ASCII')
    clear_remainders = bytearray([127] * len(plaintext))
    shift_bytes = bytearray([key] * len(plaintext))

    # convert to ints
    message_int = int.from_bytes(message_bytes, 'big')
    clear_remainders_int = int.from_bytes(clear_remainders, 'big')
    shift_int = int.from_bytes(shift_bytes, 'big')

    # perform encryption
    encrypted_int = (message_int + shift_int) & clear_remainders_int

    # convert back to str and return
    encrypted_bytes = encrypted_int.to_bytes(len(plaintext), 'big')
    return str(encrypted_bytes, encoding='ASCII')


def encrypt_index(plaintext: str, key: int) -> str:
    """
    Caesar Cipher implemented with indexed collection of english letters
    :param plaintext: str
    :param key: int
    :return: str
    """

    ciphertext = ""
    for char in plaintext:
        was_upper = char.isupper()

        initial_idx = ascii_lowercase.index(char.lower())
        shifted_idx = (initial_idx + key) % 26

        shifted_char = ascii_lowercase[shifted_idx]

        if was_upper:
            shifted_char = shifted_char.upper()

        ciphertext += shifted_char

    return ciphertext

