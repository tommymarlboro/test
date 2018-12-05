from flask import Flask, request
import os
from datetime import *
import re

data = []
pars_result = {}

directory = os.listdir('../../../')
file_path = os.path.dirname(__file__)
log_path = re.sub('sms_parser.flaskr.model.src', '' , str(file_path))

error = None

def file_reader(directory):
    """ Ищет файлы .log в каталоге передаваемом из directory.
        Принимает значения из формы, конвертирует их в даты и сравнивает
        с файлами из директории. Если файл попадает в временые рамки
        введенных дат, то данные, пройдя регулярные выражения добавляются
        в data, иначе - выводит название файла + is not log file.
    """

    data.clear()
    
    date_from = request.form['date-from'] #присваивание даты начала
    date_from = datetime.date(datetime.strptime(date_from, '%d.%m.%Y')) #из строки в datetime.datetime
    date_to = request.form['date-to'] #присваивание даты конца
    date_to = datetime.date(datetime.strptime(date_to, '%d.%m.%Y')) #из строки в datetime.datetime
            
    for i in directory:
        if re.findall(r'sms-\d{4}', i):
            name = datetime.date(datetime.strptime(i[4:11], '%Y.%m'))
            if (date_from.month <= name.month <= date_to.month):
                with open(log_path + i, encoding='utf-8') as log_file:
                    for line in log_file:
                        if '}' in line:
                          data.append(line)
                        else:
                           line = line + next(log_file)
                           data.append(line)
    for line in data:
        line = re.sub('\n', '+', line)

    return data, error
