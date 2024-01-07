number_phone = '123456789202'

if number_phone.isdigit():
    if len(number_phone) == 10:
        print("Номер телефону вірний")
    else:
        print("Номер телефону повинен мати довжину рівно 10 символів")
else:
    print("Номер телефону повинен містити лише цифрові символи")
 
