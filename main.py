import json

try:
    with open('dump.json', 'r', encoding="utf-8") as file:
        D = json.load(file)

except FileNotFoundError:
    print("Файл не найден.")
    exit()

Q = input("Введите номер квалификации (строка): ")

found = False
for item in D['data']['skills']:
    if item['code'] == Q:
        found = True
        print("=============== Найдено ===============")
        print(f"{item['code']} >> Специальность \"{item['specialty_name']}\", ПТО")
        print(f"{item['code']}-02 >> Квалификация \"{item['qualification_name']}\"")
        break 

if not found:
    print("=============== Не найдено ===============")
