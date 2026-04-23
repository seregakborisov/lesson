from functools import reduce

len_kitchen = int(input("Введите длину кухни: "))
wid_kitchen = int(input("Введите ширину кухни: "))

rooms = [
    {"name": "Kitchen", "length": len_kitchen, "width": wid_kitchen},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6},
]


area_room = list(map(lambda room: room["length"] * room["width"], rooms))
total_area = reduce(lambda x, y: x + y, area_room)

print(f"Общая площадь квартиры: {total_area} кв.м")

n = int(input("Количество комнат: "))
z = n - (n-1)
area = 0
if n > 0:
    while n > 0:
        length = float(input(f"Введите длину {z} помещения: "))
        width = float(input(f"Введите ширину {z} помещения: "))
        area_room = length * width
        area = area + area_room
        n-=1
        z+=1
    print(f"Общая площадь {area} кв. м")