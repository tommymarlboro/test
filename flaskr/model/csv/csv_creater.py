import csv
import os
import re

test = {'key':'value', 'key2':'value'}

file_path = os.path.dirname(__file__)
csv_path = re.sub('.model.csv', '/static/files/', file_path)

def csv_creater(view_res):
    
    with open(csv_path + 'csv_order.csv', 'w', newline='') as csv_file:
        columns = ['MSISDN', 'Дата и время', 'Сообщение']
        csv_writer = csv.DictWriter(csv_file, dialect='excel', delimiter=';', fieldnames=columns)
        csv_writer.writeheader()
        for val in view_res.values():
            csv_writer.writerow(val)

