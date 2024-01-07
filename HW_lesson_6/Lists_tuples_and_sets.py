from random import randint

#Task 1
"""
The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10
Constraints: use only while loop and random module to generate numbers
"""

numbers = []

range_len = 10
i = 0

while i < range_len:
    number = randint(1, 100)
    numbers.append(number)
    i += 1

print(f"This is a list of random numbers: {numbers}")
print(f"This is the largest number from the list of random numbers: {max(numbers)}")
print()
print()


#Task 2
"""
Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
Constraints: use only while loop and random module to generate numbers
"""

lists_1 = []
lists_2 = []
lists_3 = []

range_len_2 = 10
j = 0

while j < range_len_2:
    lists_1.append(randint(1, 10))
    lists_2.append(randint(1, 10))
    j += 1
    
print(f"List 1: {lists_1}")
print(f"List 2: {lists_2}")

for a in lists_1:
    for b in lists_2:
        if a == b:
            if a in lists_3:
                None
            else:
                lists_3.append(a)

print(f"Common elements without duplicates: {lists_3}")
print()
print()


#Task 3
"""
Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
Constraint: use only while loop for iteration
"""

number = []

for n in range(1, 101):
    number.append(n)
    

numbers_divisible = []
t = 0

while t < len(number):
    num = number[t]
    if num % 7 == 0 and num % 5 != 0:
        numbers_divisible.append(num)
    t += 1
        
print(f"Numbers that are divisible by 7 but not divisible by 5: {numbers_divisible}")

    

# Create a list of integers from 1 to 100
all_numbers = list(range(1, 101))

# Find numbers divisible by 7 but not multiples of 5 using while loop
result_numbers = []
index = 0
while index < len(all_numbers):
    if all_numbers[index] % 7 == 0 and all_numbers[index] % 5 != 0:
        result_numbers.append(all_numbers[index])
    index += 1

print("Numbers divisible by 7 but not multiples of 5:", result_numbers)


        
        
