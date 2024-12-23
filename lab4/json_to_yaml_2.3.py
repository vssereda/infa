import json
import re
from datetime import datetime

# Загрузить JSON-файл
with open('Iab4.json', 'r', encoding='utf-8') as f:
    timetable = json.load(f)

# Преобразовать JSON-объект
json_string = json.dumps(timetable, ensure_ascii=False, indent=4)

# Разбиваем файл на строки по \n
lst = json_string.split('\n')


def is_time(string):
    # Проверка: является ли строка временем.
    try:
        hours, minutes = string.split(':')
        hours = int(hours)
        minutes = int(minutes)
        if hours < 0 or hours > 23:
            return False
        if minutes < 0 or minutes > 59:
            return False
        return True
    except ValueError:
        return False


flag = 0
delite = []
for i in range(len(lst)):
    lst[i] = re.sub(r"    ", "", lst[i], count=1)
    lst[i] = re.sub(r"[\'\",\}]", '', lst[i])
    data = lst[i].split(': ')
    if is_time(data[-1]):
        lst[i] = data[0] + ": " + "'" + data[-1] + "'"
    if ']' in lst[i]:
        flag = 0
    if flag == 1:
        if '{' in lst[i]:
            lst[i] = re.sub(r"  {", "- " + re.sub(r"\s+", '', re.sub(r"[\'\",\}]", '', lst[i + 1]), count=1), lst[i],
                            count=1)
            delite.append(i + 1)
        else:
            lst[i] = re.sub(r"    ", "", lst[i], count=1)
    if '[' in lst[i]:
        flag = 1
    lst[i] = re.sub(r"[\{\[\]]", '', lst[i])
# Сортировать индексы в обратном порядке
delite.sort(reverse=True)


# Удалять элементы по индексам в обратном порядке
for index in delite:
    lst.pop(index)

# удаление пустых строк
for line in lst:
    if all(elem.isspace() for elem in line):
        lst.remove(line)

# Вывести строку
# print('\n'.join(lst))

with open('lab4_pars.yaml', 'w', encoding='utf-8') as file:
    file.write('\n'.join(lst))
