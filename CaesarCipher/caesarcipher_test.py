import unittest
from caesarcipher import decrypt
from caesarcipher import encrypt


class CaesarCipherTest(unittest.TestCase):

    def test_should_encrypt_text(self):
        message = "ABC"
        key = 3
        expected_result = "DEF"
        actual_result = encrypt(message, key)

        self.assertEqual(expected_result, actual_result)

    def test_should_not_encrypt_non_alphabetic_chars(self):
        message = "123  ^%..,//"
        key = 3
        actual_result = encrypt(message, key)

        self.assertEqual(message, actual_result)

    def test_should_decrypt_text(self):
        message = "DEF"
        key = 3
        expected_result = "ABC"
        actual_result = decrypt(message, key)

        self.assertEqual(expected_result, actual_result)

    def test_should_not_decrypt_non_alphabetic_chars(self):
        message = "123  ^%..,//"
        key = 3
        actual_result = decrypt(message, key)

        self.assertEqual(message, actual_result)

    def test_decrypt_should_be_inverse_encrypt(self):
        message = "ABC"
        key = 3

        en_de = encrypt(decrypt(message, key), key)
        de_en = decrypt(encrypt(message, key), key)

        self.assertEqual(en_de, de_en)
        self.assertEqual(en_de, message)

    def test_key_is_zero(self):
        message = "ABC"
        key = 0

        self.assertEqual(message, encrypt(message, key))
        self.assertEqual(message, decrypt(message, key))

    def test_key_greater_than_26(self):
        message = "ABC"
        key = 33
        equiv_key = key % 26

        self.assertEqual(encrypt(message, key), encrypt(message, equiv_key))
        self.assertEqual(decrypt(message, key), decrypt(message, equiv_key))


if __name__ == "__main__":
    unittest.main()
