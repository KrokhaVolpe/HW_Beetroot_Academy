#Task 4

"""
The math quiz program.

Write a program that asks the answer for a mathematical expression, 
checks whether the user is right or wrong, and then responds with a message accordingly.
"""

import random


while True:  
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    math_symbols = random.choice(['-', '/', '*', '+'])
    
    print(f"Скільки буде {number_1} {math_symbols} {number_2}")
    
    answer_user = input("Введіть відповідь або stop для завершення програми: ")
    
    if answer_user.lower() == 'stop':
        break
    
    try:
        answer_user = float(answer_user)
    except ValueError:
        print("Невірне значення. Спробуйте знову...")
        continue
    
    result = eval(f"{number_1} {math_symbols} {number_2}")
    result = round(result, 2)

    if answer_user == result:
        print("Ваша відповідь вірна")
    else:
        print("Ваша відповідь не вірна. Правильна відповідь:", result)
