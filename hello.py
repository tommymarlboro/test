from flask import Flask, request, render_template
from flask_wtf import Form
from datetime import datetime
import re
import os

filename = os.listdir(r'C:/Users/Дмитрий Игнатов/Documents/proj/test/')
data = []
res = []
result = {}
finish = []

#списки для парса
date = []
qtp = []
info = []
rmg = []
req = []
user = []
sender = []
number = []
mclass = []
coding = []
message = []



########
#поиск лог-файла по дате и запись его в data
def reader(filename):
    date_from = request.form['date-from'] #присваивание даты начала
    date_from = datetime.strptime(date_from, '%d.%m.%Y') #из строки в datetime.datetime
    date_to = request.form['date-to'] #присваивание даты конца
    date_to = datetime.strptime(date_to, '%d.%m.%Y') #из строки в datetime.datetime
    for i in filename:
        if re.findall(r'sms-\d{4}', i):
            name = datetime.strptime(i[4:11], '%Y.%m')
            if name >= date_from and name <= date_to:
                print(i + ' - read succesfull')
                with open(i, encoding = 'utf-8') as log_file:
                    for line in log_file:
                        if '}' in line:
                          data.append(line)
                        else:
                           line = line + next(log_file)
                           data.append(line)
            else:
                print(i + ' - skip')
        else:
            print(i + ' - is not log file')
    return data



#парсинг 
def pars(res):
    date_from = request.form['date-from']#присваивание даты начала
    date_from = datetime.strptime(date_from, '%d.%m.%Y')#из строки в datetime.datetime
    date_to = request.form['date-to']#присваивание даты окончания
    date_to = datetime.strptime(date_to, '%d.%m.%Y')#из строки в datetime.datetime    
    for line in res:
        if re.findall(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}.\d{3}', line):
            date_time = datetime.strptime(line[1:19], '%d-%m-%Y %H:%M:%S')
            if date_time >= date_from and date_time <= date_to:
                print('kek')
                finish.append(line)
            else:
                print('lol')
#        qtp.append(re.findall(r'\d+@\w{3}-\d+-\d{2}', line))
#        info.append(re.findall(r'[I]\w+', line))
#        rmg.append(re.findall(r'r.m.g.\w+.\w+.-.\w+', line))
#        req.append(re.findall(r'req\w+..S\w+', line))
#        user.append(re.findall(r'user..\w+.', line))
#        sender.append(re.findall(r'from..\w+.', line))
#        number.append(re.findall(r'to..\d+', line))
#        mclass.append(re.findall(r'mclass..\w+', line))
#        coding.append(re.findall(r'coding..\w+', line))
#        message.append(re.findall(r'text..\w+.+', line))

    return finish, date, qtp, info, rmg, req, user, sender, number, mclass, coding, message

def final(data):
    i = 0
    for line in finish:
        result[i] = {'MSISDN': re.findall(r'to..\d+', line),
                     'дата': line[1:20],
                     'Сообщение': re.findall(r'text..\w+.+', line),
                     '': '<br>'}
        i += 1
    return result


#ключ
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'



#маршрутизация
@app.route('/')
def my_form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    reader(filename)
    num = request.form['text'] #присваивание переменной номер
    for i in data:
        if re.findall(num, i): #поиск построчно по шаблону в списке
            res.append(i) #добавление строки в список, где поиск = истине
    pars(res)
    final(date)
  
    return str(result)
    
if __name__ == '__main__':
    app.run(debug=True)
