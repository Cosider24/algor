import re

with open('en-ru.txt', 'r') as f:
    en_ru_dict = {}
    for line in f:
        if re.match(r'^[a-zA-Z]+\s-\s[а-яА-ЯёЁ]+$', line):
            key, value = line.split(' - ')
            en_ru_dict[key.strip()] = value.strip()

ru_en_dict = {}
for en_word, ru_translation in en_ru_dict.items():
    translations = ru_translation.split(',')
    for translation in translations:
        ru_en_dict[translation.strip()] = en_word

with open('ru-en.txt', 'w') as f:
    for ru_word, en_translation in sorted(ru_en_dict.items()):
        f.write(f'{ru_word} - {en_translation}\n')
