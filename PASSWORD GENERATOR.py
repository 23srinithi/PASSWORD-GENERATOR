import random
import string


def generate_password():
    print("Welcome to the Password Generator!")

    # Ask user for password length
    length = int(input("Enter desired password length: "))

    # Characters to include in password
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits  # 0-9
    symbols = string.punctuation  # special characters

    all_chars = letters + digits + symbols

    # Generate password
    password = "".join(random.choice(all_chars) for _ in range(length))

    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    generate_password()
