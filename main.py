import json # библиотека для работы с JSON-файлами

with open("dump.json", "r", encoding="utf-8") as file: # открываем файл в режиме чтения
    qualifications_data = json.load(file) # З+загружаем содержимое файла в переменную qualifications_data

qualification_code = input("Введите номер квалификации: ") # запрашиваем у пользователя код квалификации

found = False # логическая переменная для отслеживания найденной квалификации
for qualification in qualifications_data: # перебираем записи в qualifications_data
    if qualification['fields']['code'] == qualification_code: # если код квалификации совпадает с введенным
        found = True # устанавливаем флаг в True, так как квалификация найдена
        print("=============== Найдено ===============") # выводим
        print(f"{qualification['fields']['code']} >> Специальность \"{qualification['fields']['title']}\", {qualification['fields']['c_type']}") # выводим детали
if not found: # если ни одна квалификация не была найдена
    print("=============== Не найдено ===============") # выводим
