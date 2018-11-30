import os
import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from .model.src import file_reader, search_numbers, date_filter, text_pars
from .controller import *
from .model.csv import csv_creater

directory = os.listdir('../.')

bp = Blueprint('src', __name__, url_prefix='/search')



@bp.route('/search', methods=('GET', 'POST'))                   #поисковая страница
def search():
    error = None    
    if request.method == 'POST':

        date_from = request.form['date-from']                       #присваивание даты начала
        date_to = request.form['date-to']                             #присваивание даты окончания
        number = request.form['text']                                   #присваивание номера
        
        file_reader.file_reader(directory)
        search_numbers.search_numbers(file_reader.data)
        date_filter.date_filter(search_numbers.found_numbers)
        text_pars.text_pars(date_filter.found_dates)

        if error is None:
            return redirect(url_for('src.result'))

        flash(error)

    return render_template('search/search.html', error=error)


@bp.route('/result', methods=('GET', 'POST'))                       #страница результата поиска
def result():
    error = None
    if len(text_pars.pars_result) == 0:
        error = 'не найдено'
        flash(error)

    view_res = text_pars.pars_result #class dict
    len_view_res = len(view_res)

    csv_creater.csv_creater(view_res)
    
    return render_template('search/result.html',
                                   view_res=view_res,
                                   len_view_res=len_view_res,
                                   error=error)


@bp.route('/report', methods=('GET', 'POST'))                       #страница заказа отчета
def report():
    error = None

    return render_template('report/report.html')
