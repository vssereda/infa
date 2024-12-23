import json
import yaml
#Читаем JSON файл:

with open('lab4.json', 'r', encoding='utf8') as f:
    json_data = json.load(f)
#Записываем данные YAML в файл:

with open('lab4_bibl.yaml', 'w', encoding='utf8') as f:
    f.write(yaml.dump(json_data, allow_unicode=True))