import random 

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.onions = None
        self.bacon = None

    def __str__(self):
        return f"Пицца (Размер - {self.size}. Добавки: {self.cheese}{self.pepperoni}{self.mushrooms}{self.onions}{self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        random_number = random.randint(0, 1)        
        if random_number == 0:
                self.pizza.cheese = "Сыр. "
        else:
            self.pizza.cheese = ""
        return self

    def add_pepperoni(self):
        random_number = random.randint(0, 1)        
        if random_number == 0:
            self.pizza.pepperoni = "Пепперони. "
        else: 
            self.pizza.pepperoni = ""
        return self

    def add_mushrooms(self):
        random_number = random.randint(0, 1)       
        if random_number == 0:
            self.pizza.mushrooms = "Грибы. "
        else:
            self.pizza.mushrooms = ""
        return self

    def add_onions(self):
        random_number = random.randint(0, 1)
        if random_number == 0:
            self.pizza.onions = "Лук. "
        else:
            self.pizza.onions = ""
        return self

    def add_bacon(self):
        random_number = random.randint(0, 1)        
        if random_number == 0:
            self.pizza.bacon = "Бекон."
        else:
            self.pizza.bacon = ""
        return self

    def build(self):
        return self.pizza


class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .set_size("Маленькая")
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .add_onions()
                .add_mushrooms()
                .build())
        
    def make_pizza2(self):
        return (self.builder
                .set_size("Средняя")
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .add_onions()
                .add_mushrooms()
                .build())
        
    def make_pizza3(self):
        return (self.builder
                .set_size("Большая")
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .add_onions()
                .add_mushrooms()
                .build())


builder = PizzaBuilder()
director = PizzaDirector(builder)

pizza = director.make_pizza()
print(pizza)

pizza2 = director.make_pizza2()
print(pizza2)

pizza3 = pizza = director.make_pizza3()
print(pizza3)

