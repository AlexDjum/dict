fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

fresh = []
sea = []

for dict_ in fish:
    if dict_['water'] == 'fresh':
        fresh_water.append(dict_)
    if dict_['water'] == 'sea':
        sea_water.append(dict_)

for fish_sea in sea_water:
    sea.append(fish_sea["specie"])
    result_1 = ', '.join(sea)

for fish_fresh in fresh_water:
    fresh.append(fish_fresh["specie"])
    result_2 = ', '.join(fresh)

print(f'Морские: {result_1}')
print(f'Пресноводные: {result_2} ')
