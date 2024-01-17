# first method - using a dictionary
def get_inverse_key(key: dict[str, str]) -> dict[str, str]:
    """
    reverses dictionary mapping
    @param key: dict[str, str]
    @return: dict[str, str]
    """
    inverse_key = {value: key for key, value in key.items()}
    return inverse_key

    
def encrypt(plaintext: str, key: dict[str, str]) -> str:
    """
    Encrypts a message using the monoalphabetic substitution cipher
    @param plaintext: str
    @param key: str, the key is represented as a dictionary mapping plaintext -> ciphertext
    @return: str
    """

    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += key[char]
            else:
                ciphertext += key[char.upper()].lower()

        else:
            ciphertext += char

    return ciphertext


# second method - using a permutation of the alphabet
def get_inverse_key_perm(key: str) -> str:
    """
    computes the inverse key
    :param key: str
    :return: str
    """
    inv_key = [""] * 26
    for idx, char in enumerate(key):
        inv_key[ord(char) - 65] = chr(idx + 65)
    return ''.join(inv_key)


def encrypt_perm(plaintext: str, key: str) -> str:
    """
    Encrypts a message using the monoalphabetic substitution cipher
    :param plaintext: str
    :param key: str, key is represented as a permutation of the uppercase english alphabet
    :return: str
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += key[(ord(char) - 97)].lower()
            else:
                ciphertext += key[(ord(char) - 65)]
        else:
            ciphertext += char

    return ciphertext

