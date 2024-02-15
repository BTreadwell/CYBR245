def xor(char1, char2):
    # Get numeric values for each character
    char1_val = ord(char1)
    char2_val = ord(char2)

    # xor the two values
    xor_result = char1_val ^ char2_val

    # return the result
    return xor_result
