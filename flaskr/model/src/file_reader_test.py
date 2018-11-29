import os
from datetime import datetime
import re

data = []
directory = os.listdir('../../../')
file_path = os.path.dirname(__file__)
log_path = re.sub('sms_parser.flaskr.model', '' , str(file_path))


def file_reader_test(directory):
    date_from = '01.01.2018'
    date_to = '30.12.2018'
    date_from = datetime.strptime(date_from, '%d.%m.%Y')
    date_to = datetime.strptime(date_to, '%d.%m.%Y')
    for i in directory:
        print(i)
        if re.findall(r'sms-\d{4}', i):
            name = datetime.strptime(i[4:11], '%Y.%m')
            if name >= date_from and name <= date_to:                
                with open(log_path + i, encoding='utf-8') as log_file:
                    for line in log_file:
                        if '}' in line:
                            data.append(line)
                        else:
                            line = line + next(log_file)
                            data.append(line)
            


file_reader_test(directory)
