#Task 1
"""
Make a program that has some sentence (a string) on input and
returns a dict containing all unique words as keys and the number of occurrences as values.
"""

input_sentence = input("Введіть речення: ")

words = input_sentence.split()
counts = {}

for word in words:
    word = word.strip('.,!?"\'').lower()
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
print("-" * 25)



#Task 2
"""
Compute the total price of the stock where the total price is the sum of the price of an item multiplied by the quantity of this exact item.
The code has to return the dictionary with the sums of the prices by the goods types.
"""
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_prices = {}
for i in stock:
    total_prices[i] = stock[i] * prices[i]

print(total_prices)
print("-" * 25)


#Task 3
"""
List comprehension exercise
Use a list comprehension to make a list containing tuples (i, j) where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.
"""

result = []

for i in range(1, 11):
    j = i ** 2
    result.append((i, j))
    
    #print(f"{i} - {j}")

print(result)
print("-" * 25)


#Task 4
"""
Створити лист із днями тижня.
В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
"""

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_to_numbers = {}
numbers_to_days = {}

for i, day in enumerate(days_of_week):
    days_to_numbers[day] = i + 1

print(f"Days to Numbers: {days_to_numbers}")

for i, day in enumerate(days_of_week):
    numbers_to_days[i + 1] = day

print(f"Numbers to Days: {numbers_to_days}")





