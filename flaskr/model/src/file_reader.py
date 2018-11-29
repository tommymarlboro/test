from flask import Flask, request
import os
from datetime import datetime
import re

data = []
pars_result = {}

directory = os.listdir('../../../')
file_path = os.path.dirname(__file__)
log_path = re.sub('sms_parser.flaskr.model.src', '' , str(file_path))

def file_reader(directory):
    """ Ищет файлы .log в каталоге передаваемом из directory.
        Принимает значения из формы, конвертирует их в даты и сравнивает
        с файлами из директории. Если файл попадает в временые рамки
        введенных дат, то данные, пройдя регулярные выражения добавляются
        в data, иначе - выводит название файла + is not log file.
    """
    error = None

    data.clear()
    
    date_from = request.form['date-from'] #присваивание даты начала
    date_from = datetime.strptime(date_from, '%d.%m.%Y') #из строки в datetime.datetime
    date_to = request.form['date-to'] #присваивание даты конца
    date_to = datetime.strptime(date_to, '%d.%m.%Y') #из строки в datetime.datetime
            
    for i in directory:
        if re.findall(r'sms-\d{4}', i):
            name = datetime.strptime(i[4:11], '%Y.%m')
            if name >= date_from and name <= date_to:
                with open(log_path + i, encoding='utf-8') as log_file:
                    print(i + ' - +++ find +++')
                    for line in log_file:
                        if '}' in line:
                          data.append(line)
                        else:
                           line = line + next(log_file)
                           data.append(line)
    for line in data:
        line = re.sub('\n', '+', line)

    return data, error
