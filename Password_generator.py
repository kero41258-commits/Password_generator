import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

while True:
    length = int(input("How many characters should the password have? (minimum 8): "))
    if length >= 8:
        break
    print("Length must be at least 8. Please try again.")

while True:
    password = ""
    for i in range(length):
        password += random.choice(characters)

    has_symbol = any(c in string.punctuation for c in password )
    has_digit = any(c in string.digits for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password )

    if has_symbol and has_digit and has_upper:
        break

print("Your password:", password)