import unittest
from string import ascii_uppercase
from mas import encrypt, decrypt


class MASTest(unittest.TestCase):

    def setUp(self):
        DEFAULT_KEY_PERM = "THEQUICKBROWNFXJMPSVLAZYDG"
        self.DEFAULT_KEY = dict()

        def _build_default_key() -> None:
            for idx, char in enumerate(ascii_uppercase):
                self.DEFAULT_KEY[char] = DEFAULT_KEY_PERM[idx]

        _build_default_key()

    def test_should_encrypt_text(self):
        plaintext = "Hello"
        key = self.DEFAULT_KEY
        expected_result = "Kuwwx"
        actual_result = encrypt(plaintext, key)

        self.assertEqual(expected_result, actual_result)

    def test_should_decrypt_with_same_key(self):
        ciphertext = "Kuwwx"
        key = self.DEFAULT_KEY
        expected_result = "Hello"
        actual_result = decrypt(ciphertext, key)

        self.assertEqual(expected_result, actual_result)

    def test_should_not_encrypt_nonalpha_chars(self):
        plaintext = "1341*&@()%."
        key = self.DEFAULT_KEY
        result = encrypt(plaintext, key)

        self.assertEqual(plaintext, result)

    def test_decrypt_encrypt_are_inverses(self):
        plaintext = "THIS IS A MESSAGE"
        key = self.DEFAULT_KEY
        actual_result = decrypt(encrypt(plaintext, key), key)

        self.assertEqual(plaintext, actual_result)


if __name__ == "__main__":
    unittest.main()
