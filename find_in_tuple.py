fish = [

    {"specie": "Белуга", "water": "fresh"},
    {"specie": "Карась", "water": "fresh"},
    {"specie": "Красноперка", "water": "fresh"},

    {"specie": "Морской окунь", "water": "sea"},
    {"specie": "Тунец", "water": "sea"},
    {"specie": "Скумбрия", "water": "sea"},

]


def get_fish(fish_name):
    for fish_found in fish:
        if fish_name == fish_found['specie']:
            fish1 = fish_found['specie']
            water = fish_found['water']
#     return fish, water
    return fish1, water
#     # pass


# Не удаляйте код ниже, он нужен для проверки!

fish_name = input()
# fish, water = get_fish(fish_name)
fish1, water = get_fish(fish_name)
print(fish1, water)

