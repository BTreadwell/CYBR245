from caesarcipher import encrypt


def get_key():
    while True:
        try:
            key = int(input("Enter a shift key (must be an int): "))
            return key
        except ValueError:
            print("Error converting shift key to an int. Try again.")


def main():
    message = input("Enter a message: ")
    key = get_key()

    print("This is your encrypted message: ", encrypt(message, key))


if __name__ == "__main__":
    main()
