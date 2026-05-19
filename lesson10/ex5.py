from abc import ABC, abstractmethod

class Operat(ABC):
    @abstractmethod
    def execute(self):
        pass

class Addition(Operat):
    def execute(self, a, b):
        return a + b
        
class Subtraction(Operat):
    def execute(self, a, b):
        return a - b

class Multiplication(Operat):
    def execute(self, a, b):
        return a * b

class Devision(Operat):
    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Деление на ноль невозможно")
    
class Calculator:
    def __init__(self):
        self.strategy = None
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def calculate(self, a, b):        
        return self.strategy.execute(a, b)
    
calc = Calculator()

operation = ""

try:
    a = int(input("Введите число а: "))
    b = int(input("Введите число b: "))
except ValueError:
    print("НЕОБХОДИМО ВЕСТИ ЧИСЛО! ")
    
x = input("Введите операцию: (+, -, *, /) ") 



if x == "+":
    operation = Addition()
elif x == "-":
    operation = Subtraction()
elif x == "*":
    operation = Multiplication()
elif x == "/":
    operation = Devision()
else: 
    raise ValueError("Неверный оператор!")
 
calc.set_strategy(operation)
print(calc.calculate(a, b))
