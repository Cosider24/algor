with open('en-ru.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
ru_en = {}
for line in lines:
    if '-' in line:
        eng_word, ru_tr = line.strip().split('-')
        for ru_word in ru_tr.split(','):
            if ru_word.strip() not in ru_en:
                ru_en[ru_word.strip()] = [eng_word]
            else:
                if eng_word not in ru_en[ru_word.strip()]:
                    ru_en[ru_word.strip()].append(eng_word)
with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for key in sorted(ru_en.keys()):
        trans = ','.join(sorted(ru_en[key]))
        file.write(f'{key}-{trans}\n')