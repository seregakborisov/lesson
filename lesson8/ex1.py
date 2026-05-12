class Soda:
    def __init__(self, taste=""):
        self.taste = taste

    def __str__(self):
        if self.taste == self.taste:
            return f"У вас газировка с {self.taste} вкусом"
        else:
            return "У вас обычная газировка"
        
first = Soda("клубничным")
second = Soda()

x = input("С каким вкусом ваша газировка? \n --->")

third = Soda(x)


print(first)
print(second)
print(third)