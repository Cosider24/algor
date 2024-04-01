stud = {'Алексей': ['Английский','Французский','Немецкий'],
'Мария': ['Испанский','Русский','Немецкий'],
'Иван': ['Китайский','Французский','Польшский'],
'Ярослав': ['Английский','Испанский','Немецкий']
}
all_languag = set()

for languag in stud.values():
    all_languag.update(languag)

sorted_languag = sorted(all_languag)
print("Отсортированный список: ", sorted_languag)

a = ""
for k in stud.keys():
    if "Китайский" in stud[k]:
        a += k + " "
print("Знающий Китайский: ", a)