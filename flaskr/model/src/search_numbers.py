from flask import Flask, request, render_template
from flask_wtf import Form
import re

found_numbers = []

def search_numbers(data):
    """ Принимает введенное значение из формы в качестве строки
        и выполняет поиск с помощью регулярного выражения в списке.
        Если находит, то добавляет строку в список, иначе переходит к
        следующей строке
    """
    error = None
    found_numbers.clear()
    
    number = request.form['text']
    
    for i in data:
        if re.findall(number, i):
            found_numbers.append(i)
        
    return found_numbers, error
