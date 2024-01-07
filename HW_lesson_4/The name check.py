name = 'Katarina'
name = name.lower()

user_input = input("Введіть ваше ім`я: ")

user_input = user_input.lower()

if user_input.lower() == name:
    print("Введене ім'я співпадає зі збереженим.")
else:
    print("Введене ім'я не співпадає зі збереженим.")

