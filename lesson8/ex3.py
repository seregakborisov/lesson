class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year

    def start(self):
        print("\n ***** \nАвтомобиль заведён")

    def stop(self):
        print("\n ***** \nАвтомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.type = car_type

    def set_color(self, color):
        self.color = color
        
color_car = input("Введите цвет: ")
type_car = input("Введите тип кузова: ")
year_car = input("Введите год выпуска: ")
status = input("Введите статус автомобиля (заведен/заглушен): ")

car = Car(color_car, type_car, year_car)

if status == "заведен":
    car.start()
elif status == "заглушен":
    car.stop()


print(car.year, car.type, car.color)
