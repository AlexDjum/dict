employees = [
    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семеновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнев Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for people in employees:
    if people['vaccinated'] == True:
        vaccinated.append(people['fio'])
    else:
        not_vaccinated.append(people['fio'])

print('Вакцинированные:')
for vacin in vaccinated:
    print(vacin)

print('Остальные:')
for not_vacin in not_vaccinated:
    print(not_vacin)
