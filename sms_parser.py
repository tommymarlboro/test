import re
import os
from hello import SearchForm

filename = os.listdir(r'C:/Users/Дмитрий Игнатов/Documents/proj/test/')
date_time = r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}:\d{2}.\d{3}'
qtp = r'\d{9}@\w{3}-\d{9}-\d{2}'
info =  r'[I]\w+'
rmg = r'r.m.g.\w+.\w+.-.\w+'
request = r'req\w+..S\w+'
user = r'user..\w+.'
sender = r'from..\w+.'
number = r'to..\d+'
mclass = r'mclass..\w+'
coding = r'coding..\w+'
message = r'text..\w.+'
date = []
time = []



data = []
last_data = []
All_data = []

# запись строк в data
def writer(filename):
    for i in filename:
        if re.findall(r'sms-\d{4}', i):
            print('ok')
            with open(i, encoding = 'utf-8') as log_file:
                for line in log_file:
                    if '}' in line:
                      data.append(line)
                    else:
                       line = line + next(log_file)
                       data.append(line)
        else:
            print(i)
    return data


# удаление из data лишних '\n'
def cleaner(data):
    for data in data:
        if re.search('\n', str(data)):
            data = re.sub('\n', '', str(data))
    return data


# поиск по шаблону

def search(num):
    for i in data:
        if re.findall(r'to=\'' + num, i):
            print(i)


if __name__ == '__main__':
    cleaner(writer(filename))
