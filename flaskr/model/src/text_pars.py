import re

pars_result = {}
data_for_view = []


def text_pars(found_dates):
    """ Разбивает список с помощью регулярных выражений создавая
        кортежи
    """
    pars_result.clear()

    i = 1
    for line in found_dates:
        if re.search('\n', line):
            line = re.sub('\n', '', line)
        pars_result[i] = {'MSISDN': re.findall(r'\d{11}', line),
                             'Дата и время': line[1:20],
                             'Сообщение': re.findall(r'(?<=text..)\w+.+', line)}
        i += 1

    return pars_result
