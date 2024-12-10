import json
import regex as re

# Загрузить JSON-файл
with open('lab4.json', 'r', encoding='utf-8') as f:
    timetable = json.load(f)

# Преобразовать JSON-объект
json_string = json.dumps(timetable, ensure_ascii=False, indent=4)

# Разбиваем файл на строки по \n
lst = json_string.split('\n')

for i in range(len(lst)):
    #удаление ненужных метасимволов
    lst[i] = re.sub(r"[\'\",\]\{\}\[]", '', lst[i])
    vivod = re.sub(r'(\s*)\W*\"(\w+)\"(:\s\"\w+\"\W*)', '(?1)', lst[i])
    #удаление образовавшихся лишних табуляций
    lst[i] = re.sub(r"    ", "", lst[i], count=1)
    lst[i] = re.sub(r"  type-lesson", "- type-lesson", lst[i])
# удаление пустых строк
for line in lst:
    if all(elem.isspace() for elem in line):
        lst.remove(line)
with open('lab4_reg.yaml', 'w', encoding='utf-8') as file:
    file.write('\n'.join(lst))