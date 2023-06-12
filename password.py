import random

print("Welcome to password Generator!")
# Password will be generated from this:
uppercase_letters = "ABCDEFGHIJKLMNAOPQRSTUVXYZ"
lowercase_letters = uppercase_letters.lower()
numbers = "1234567890"
symbols = "~!@#$%^&*()"

# The password will be generated based on the given options:
include_uppercase_letters = "false"
include_lowercase_letters = "false"
include_numbers = "false"
include_symbols = "false"

# User input:
print("Enter 'true' or 'false' as answers! ")
include_uppercase_letters = input("Do you want 'UPPERCASE' letters in your password?: ")
include_lowercase_letters = input("Do you want 'lowercase' letters in your password?: ")
include_symbols_letters = input("Do you want 'symbols' letters in your password?: ")
include_numbers_letters = input("Do you want 'numbers' letters in your password?: ")

# Password generating logic:
length_of_password = int(input("Enter your password length: "))
password = ""
for i in range(0,length_of_password):
    if include_uppercase_letters == "true" : password += uppercase_letters[int(random.random() * len(uppercase_letters))]
    if include_lowercase_letters == "true" : password += lowercase_letters[int(random.random() * len(lowercase_letters))]
    if include_numbers_letters == "true"   : password += numbers[int(random.random() * len(numbers))]
    if include_symbols_letters == "true"   : password += symbols[int(random.random() * len(symbols))]

# Lenght of password asking from user
print(password[0:length_of_password])