from mas import encrypt_perm


def main():
    message = input("Enter a message: ")
    selection = input("Would you like to encrypt or decrypt? Please enter e or d: ").lower()
    key = get_key()

    if selection == "e":
        print("This is your encrypted message: ", encrypt_perm(message, key))

    elif selection == "d":
        print("not available for this assignment")

    else:
        print("Invalid input")


def validate_key(key: str) -> bool:
    if len(key) != 26:
        return False

    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char not in key:
            return False

    return True


def get_key() -> str:
    key = input("Enter a key (a permutation of the alphabet A-Z): ").upper()
    while not validate_key(key):
        print("Invalid key. Example key: THEQUICKBROWNFXJMPSVLAZYDG")
        key = input("Enter a key (a permutation of the alphabet A-Z): ").upper()

    return key


if __name__ == "__main__":
    main()
