import json

with open("dump.json", "r", encoding="utf-8") as file:
    a = json.load(file)

q = input("Введите номер квалификации: ")

found = False
for item in a:
    if item['fields']['code'] == q:
        found = True
        print("=============== Найдено ===============")
        print(f"{item['fields']['code']} >> Специальность \"{item['fields']['title']}\", {item['fields']['c_type']}")
if not found:
    print("=============== Не найдено ===============")
