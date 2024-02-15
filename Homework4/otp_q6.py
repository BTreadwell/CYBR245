def encrypt_otp(message, key):
    result = ""
    for idx in range(len(message)):
        msg_char = message[idx]
        key_char = key[idx]

        # msg_val should be assigned the ASCII value of the character stored in msg_char
        msg_val = ord(msg_char)

        # key_val should be assigned the ASCII value of the character stored in key_char
        key_val = ord(key_char)

        # xor_val should be assigned the result of xor'ing msg_val and key_val
        xor_val = msg_val ^ key_val

        # xor_char should be assigned the character associated with the ASCII value of xor_val
        xor_char = chr(xor_val)

        result += xor_char

    return result