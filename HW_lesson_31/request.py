import requests

url = "https://en.wikipedia.org/wiki/HTTP"

session = requests.Session()
session.get(url)


requests.get(url)

resp = requests.get(url)

print("1", help(resp))

resp.status_code
if resp.status_code != 200:
    print(resp.status_code)
else:
    print("ok")

print(resp.ok)

print(resp.text)

resp.content

print("*"*25)
import requests

resp = requests.get('https://api.github.com')

# Перевірка, чи запит був успішним (код статусу 200)
if resp.status_code == 200:
    datas = resp.json()
    
    # Виведення вмісту відповіді
    print(datas)
    
    # Перевірка, чи відповідь є списком
    if isinstance(datas, list):
        # Вибір першого елементу у списку datas
        if datas:
            first_dict = datas[0]
            
            # Виведення ключів та значень першого словника
            for key, value in first_dict.items():
                print()
        else:
            print("Список порожній")
    else:
        print("Помилка: Очікувався список")
else:
    print(f"Помилка запиту. Код статусу: {resp.status_code}")



print("*"*25)


#print(resp.headers)

base_url = "https://ru.stackoverflow.com/questions"

r = requests.get(base_url)
data = r.json()
print("2", data)

