country_cap = {"Россия": "Москва",
               "Франция": "Париж",
               "США": "Вашингтон",
               "Великобритания": "Лондон",
               "Италия": "Рим",
}
print("Все страны и их столицы: ")
for country in country_cap:
    print(f"{country}-{country_cap[country]}")
country_to = "Россия"
if country_to in country_cap:
    print(f"Столица страны {country_to}: {country_cap[country_to]}")
else:
    print("Такой страны нет в списке")
sorted_key = sorted(country_cap.keys())
print("Содержимое словоря отсортированное")
for country in sorted_key:
    print(f"{country} - {country_cap[country]}")