from flask import Flask, request
import os
import re
import csv
from datetime import datetime

directory = os.listdir('../../../../')
file_path = os.path.dirname(__file__)
log_path = re.sub('sms_parser.flaskr.model.report', '' , str(file_path))
template_path = re.sub('model.report', 'static/files/templates_sms.txt', str(file_path))
log_data = []
template_data = []

date = '01.2018'

def file_finder(date):
    """Сравнивает введеную дату и дату в названии лог-файла.
    Если дата совпадает, записывает содержимое файла в data построчно
    """

    date = datetime.strptime(date, '%m.%Y')    

    for i in directory:
        if re.findall(r'sms-\d{4}', i):
            name = datetime.strptime(i[4:11], '%Y.%m')
            if name == date:
                print('файл найден - ', i)
                with open(log_path + i, encoding='utf-8') as log_file:
                    for line in log_file:
                        if re.search('\\n', line):
                            line = re.sub('\n', '', line)
                            line = line + next(log_file)
                            log_data.append(re.findall(r'(?<=text..)\w+.+', line))
                        line = re.sub('\d{1,5}.\d{2}', '%d', line)
                        line = re.sub('\d{2}.\d{2}.\d{4}', '%w{1,5}', line)
                        line = re.sub('Ваш номер .{14}', 'Ваш номер %w{1,5}', line)
                        log_data.append(re.findall(r'(?<=text..)\w+.+', line))

 
    return log_data


def template_reader():
    """Записывает шаблоны в template_data из файла с шаблонами"""
    
    with open(template_path) as templates_file:
        for row in templates_file:
            re.sub(r'(\n)', '', row)
            template_data.append(row)
        for i in templates_file:
            if re.findall(r'\n', i):
                print('lol')
                
    return template_data

file_finder(date)
template_reader()


