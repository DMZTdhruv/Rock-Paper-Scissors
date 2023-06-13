import random

print("Welcome to password Generator!")
name = input("Enter your name please: ")

upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
lower_case_letters = upper_case_letters.lower();
symbols = "`~!@#$%^&*()"
numbers = "0123456789"

print("Enter the following questions to generate your password: ")
include_uppercase_letters = "N"
include_lowercase_letters = "N"
include_symbols = "N"
include_numbers = "N"


password = [];
include_uppercase_letters = input("Do you want Uppercase characters in your password Y or N: ")
if include_uppercase_letters == "Y": 
    length = int(input("How many uppercase Letters do you want: "))
    for i in range(length):
        password += upper_case_letters[int(random.random() * len(upper_case_letters))]

include_lowercase_letters = input("Do you want Lowercase characters in your password Y or N: ")
if include_lowercase_letters == "Y":
    length = int(input("How many Lowercase Letters  do you want: "))
    for i in range(length):
        password += lower_case_letters[int(random.random() * len(lower_case_letters))]

include_numbers = input("Do you want Numbers in your password Y or N: ")
if include_numbers == "Y":
    length = int(input("How many Numbers do you want: "))
    for i in range(length):
        password += numbers[int(random.random() * len(numbers))]

include_symbols = input("Do you want symbols in your password Y or N: ")
if include_symbols == "Y":
    length = int(input("How many Symbols do you want: "))
    for i in range(length):
        password += symbols[int(random.random() * len(symbols))]


print(f"{name} based on what you selected we have made this password for you: ")
random.shuffle(password);
real_password = ''.join(password);
print(real_password);

if len(password) > 10:
    print("That's a strong password!")
elif len(password) > 8:
    print("That's a good password!");
else:
    print("That's a very easy password")