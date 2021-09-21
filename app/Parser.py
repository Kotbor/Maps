import json
import openpyxl
import logging

logging.basicConfig(filename='app.log',
                    format='%(name)s - %(levelname)s - %(message)s') #Конфигурация логов

def GetJsonList(FileName):
    data = [] #Результат
    start = False  # Начинаем парсинг
    address = '' #Адрес
    try:
        FileReader = openpyxl.load_workbook(FileName) #Читаем файл
        sheet = FileReader.active
        for row in sheet.rows:
            string = ''
            # Формируем строку для обработки #
            for cell in row:
                string = string + str(cell.value) + '|'
            # Сформировали строку #
            if ('День недели' in string):
                start = True  #Запускаем парсинг, далее идут нужные нам строки
                continue
            if (start):
                line = string.split('|')   #Делим строку по разделителю
                if not (line[0] == 'None') and not (' всего' in line[0]):
                    if not (line[0] == 'Итого'):
                        dw = line[0] #День
                if not (line[1] == 'None'):
                    if not ('всего' in line[1]):
                        time = line[1] #Время
                if not (line[2] == 'None'):
                    address = line[2].replace(" всего", "")   #Адрес; Иногда в строку появляется " всего", просто убираем его
                # Пропускаем заказы с самовывозом
                if ('Самовывоз' in line[3]):
                    continue   #Пропускаем самовывоз
                data.append({"address": address, "dw": dw.split(' ')[1], "hour": int(time)})
        data = data[:-3]  #Убираем 3 лишние строки из массива
       # data = json.dumps(data, ensure_ascii=False)
        return data  #Возвращаем готовый массив
    except Exception as err:
        logging.error(err)
        return 'Exception; Check log file'