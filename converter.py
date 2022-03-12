order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for name in order:
    count = int(name['skolko'])
    specie = name['poroda'].title()
    size = int(name['sred_razmer'] / 10)
    order_converted.append({'count': count, 'specie': specie, 'avg_size': size})

# print(order_converted)
