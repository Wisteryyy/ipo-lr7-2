import json # библиотека для работы с JSON-файлами

with open("dump.json", 'r', encoding='utf-8') as file: # открываем файл "dump.json" для чтения в кодировке UTF-8
    qualifications_data = json.load(file) # загружаем содержимое файла в переменную qualifications_data

while True: # запускаем бесконечный цикл
    status = False # инициализируем переменную status  False, чтобы отслеживать, найдена ли квалификация
    find = input("Введите номер квалификации: ") # запрашиваем ввод номера квалификации

    for qualification in qualifications_data: # проходим через каждый элемент
        if qualification['model'] == 'data.skill': # проверяем, является ли модель объекта квалификацией
            if qualification["fields"]['code'] == find: # если они равны
                for specialty in qualifications_data: # проходим по всем специальностям
                    if specialty['model'] == 'data.specialty': # проверяем, является ли модель объекта специальностью 
                        if specialty['pk'] == qualification['fields']['specialty']: # сравниваем изначальный ключ специальности с полем specialty в квалификации
                            print("=============== Найдено ===============") # выводим если найдена
                            print( # выводим
                                f'{specialty["fields"]["code"]} >> Специальность'
                                f' {specialty["fields"]["title"]}, {specialty["fields"]["c_type"]}')
                            print(f"{qualification['fields']['code']} >> Квалификация {qualification['fields']['title']}")
                            status = True # устанавливаем статус True, так как квалификация найдена

    if not status: # если после завершения цикла ничего не найдено, выводим сообщение об этом
        print("=============== Не найдено ===============")  
