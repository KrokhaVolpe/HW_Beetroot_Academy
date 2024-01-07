#Task 1

"""
String manipulation

Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.
"""

words = ['banana', 'ma', 'z']

for item in words:
    if len(item) >=2:
        print(f"Sample String: {item}")
        print(f"Expected Result: {item[:2]+item[-2:]}")
    else:
        print(f"Sample String: {item}")
        print(f"Expected Result: Empty String")


print()
print()


#Task 2

"""
The valid phone number program.

Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.
"""

number_phone = '123456789202'

if number_phone.isdigit():
    if len(number_phone) == 10:
        print("Номер телефону вірний")
    else:
        print("Номер телефону повинен мати довжину рівно 10 символів")
else:
    print("Номер телефону повинен містити лише цифрові символи")


print()
print()


#Task 4

"""
The name check.

Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
if your input is “Anton” and the stored name is “anton”, it should return True.
"""

name = 'Katarina'
name = name.lower()

user_input = input("Введіть ваше ім`я: ")

user_input = user_input.lower()

if user_input.lower() == name:
    print("Введене ім'я співпадає зі збереженим.")
else:
    print("Введене ім'я не співпадає зі збереженим.")











