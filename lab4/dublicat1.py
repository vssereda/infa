import json

# Загрузить JSON-файл
with open('lab4.json', 'r', encoding='utf-8') as f:
    timetable = json.load(f)


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


# Преобразовать JSON-объект
json_string = json.dumps(timetable, ensure_ascii=False, indent=4)

# Разбиваем файл на строки по \n
lst = json_string.split('\n')
for i in range(len(lst)):
    # удаление ненужных для yaml объектов json
    lst[i] = lst[i].replace('{', '')
    lst[i] = lst[i].replace('}', '')
    lst[i] = lst[i].replace('[', '')
    lst[i] = lst[i].replace(']', '')
    # удалим ненужные yaml
    line = lst[i].split('"')
    for elem in line:
        if is_time(elem):
            # изменение кавычек у времени
            line[line.index(elem)] = "'" + elem + "'"
        if elem.replace(' ', '') == ',':
            # удаление всех запятых, которые не стоят в кавычках с текстом
            line[line.index(elem)] = ''
        if ' ' * 20 in elem:
            line[line.index(elem)] = line[line.index(elem)].replace(' ', '', 4)
        if elem == 'type-lesson':
            line[line.index(elem) - 1] = line[line.index(elem) - 1].replace(' ', '', 2)
            line[line.index(elem)] = "- " + elem
    # удаление лишних пробелов
    lst[i] = ''.join(line).replace(' ', '', 4)

# удаление пустых строк
for line in lst:
    if all(elem.isspace() for elem in line):
        lst.remove(line)
# Вывести строку
#print('\n'.join(lst))

with open('lab4_ruk.yaml', 'w', encoding='utf-8') as file:
    file.write('\n'.join(lst))

