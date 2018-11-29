from flask import Flask, request, render_template
from flask_wtf import Form
from datetime import datetime
import re

found_dates = []

def date_filter(found_numbers):
    """ Принимает 2 значения из формы ввода и переводит в дату.
        Выполняется поиск регулярного выражения по списку. Найденные
        переводятся в дату и сравниваются с принятыми значениями, если
        в рамках значений, то строка добавляется список.
    """
    found_dates.clear()
    
    date_from = request.form['date-from']
    date_to = request.form['date-to'] #присваивание даты начала
    date_from  = datetime.strptime(date_from, '%d.%m.%Y')
    date_to = datetime.strptime(date_to, '%d.%m.%Y')
    for line in found_numbers:
        if re.findall(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}', line):
            date_time = datetime.strptime(line[1:11], '%d-%m-%Y')
            if date_from <= date_time <= date_to:
                found_dates.append(line)
    return found_dates
