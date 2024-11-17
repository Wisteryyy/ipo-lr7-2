import json # json

with open("dump.json", "r", encoding="utf-8") as file: # открываем в режиме чтения
    a = json.load(file) # считываем в переменную a

q = input("Введите номер квалификации: ") # вводим q

b = False # переменная b булевая ложная
for i in a: # перебераем ключи в a
    if i['fields']['code'] == q: # если равны
        b = True # то b становится тру
        print("=============== Найдено ===============") # выводим
        print(f"{i['fields']['code']} >> Специальность \"{i['fields']['title']}\", {i['fields']['c_type']}") # выводим по ключам
if not b: # если b не тру
    print("=============== Не найдено ===============") # выводим
