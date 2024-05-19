with open('en-ru.txt', 'r', encoding='utf-8') as f:
    en_ru_dict = {}
    for line in f:
        en_word, ru_word = line.strip().split(' - ')
        en_ru_dict[en_word] = ru_word

ru_en_dict = {}
for en_word, ru_word in en_ru_dict.items():
    if ru_word not in ru_en_dict:
        ru_en_dict[ru_word] = []
    ru_en_dict[ru_word].append(en_word)

sorted_ru_en_dict = dict(sorted(ru_en_dict.items()))

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for ru_word, en_words in sorted_ru_en_dict.items():
        f.write(f'{ru_word} - {", ".join(en_words)}n')
