import json # библиотека для работы с JSON-файлами

with open("dump.json", "r", encoding="utf-8") as file: # открываем файл dump.json в режиме чтения с кодировкой UTF-8
    qualifications_data = json.load(file) # загружаем содержимое JSON-файла в переменную qualifications_data

while True: # запускаем бесконечный цикл
    qualification_code = input("Введите номер квалификации: ") # запрашиваем у пользователя код квалификации

    status = False # инициализируем статус как False (квалификация не найдена)
    for item in qualifications_data: # проходим по каждому элементу списка данных
        if item['model'] == 'data.skill': # проверяем, является ли элемент квалификацией
            if item['fields']['code'] == qualification_code: # проверяем, совпадает ли код квалификации с введённым
                status = True # устанавливаем статус в True (квалификация найдена)
                print("=============== Найдено ===============") # выводим
                
                specialty_code = item['fields']['specialty'] # получаем код специальности из полей квалификации
                specialty_title = None # инициализируем переменную для названия специальности
                c_type = None # инициализируем переменную для типа специальности
                
                for spec in qualifications_data: # ищем специальность по её коду в данных
                    if spec['model'] == 'data.specialty' and spec['pk'] == specialty_code:
                        specialty_title = spec['fields']['title'] # получаем название специальности
                        c_type = spec['fields']['c_type'] # получаем тип специальности
                        print(f"{specialty_code} >> Специальность \"{specialty_title}\", {c_type}") # выводим

                qualification_title = item['fields']['title'] # получаем название квалификации
                print(f"{qualification_code} >> Квалификация \"{qualification_title}\"") # выводим
                break # завершаем текущий цикл, так как квалификация найдена

    if not status: # если статус всё ещё False (квалификация не найдена)
        print("=============== Не найдено ===============") # выводим
