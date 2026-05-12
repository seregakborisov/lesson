class autobus:
    def __init__(self, speed, max_places, max_speed):
        self.speed = speed
        self.max_places = max_places
        self.max_speed = max_speed
        self.passengers = []
        self.free_places = True
        self.seats = {}

        for i in range(1, max_places + 1):
            self.seats[i] = None

    def board(self, surname):
        for seat in self.seats:
            if self.seats[seat] is None:
                self.seats[seat] = surname
                self.passengers.append(surname)
                self.update_free_places()
                print(f"{surname} сел на место {seat}")
                return
        print("Свободных мест нет")

    def leave(self, surname):
        for seat in self.seats:
            if self.seats[seat] == surname:
                self.seats[seat] = None
                self.passengers.remove(surname)
                self.update_free_places()
                print(f"{surname} вышел")
                return
        print("Пассажир не найден")

    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)

    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)

    def update_free_places(self):
        self.free_places = len(self.passengers) < self.max_places

    def __contains__(self, surname):
        return surname in self.passengers

    def __iadd__(self, surname):
        self.board(surname)
        return self

    def __isub__(self, surname):
        self.leave(surname)
        return self



bus = autobus(70, 15, 120)

bus += "Иван"
bus += "Петя"
bus += "Федя"
bus += "Иннокентий"

print(bus.passengers)
print(bus.seats)

bus.increase_speed(20)
print("Скорость:", bus.speed)

bus -= "Иван"

print(bus.passengers)
print(bus.seats)
