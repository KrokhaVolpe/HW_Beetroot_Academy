import random

#Task 1
"""
The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
The result should be sent back to the user via a print statement.
"""

num = random.randint(1, 10)
answer_user = int(input("Please, enter a number in range 1...10: "))
if answer_user != num:
   print(f"Sorry, the number is {num}.")
else:
    print(f"Congratulations! You've won!")

print()
print()


#Task 2
"""
The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:
“Hello <name>, on your next birthday you’ll be <age+1> years”
"""

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello {user_name}, on your next birthday you’ll be {user_age + 1} years")

print()
print()


#Task 3
"""
Words combination

Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 
'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
Tips: Use random module to get random char from string)
"""

input_string = input(": ")
n = len(input_string)

for _ in range(5):
    words = ''
    for _ in range(n):
        char = random.choice(input_string)
        words += char
    print(words)








