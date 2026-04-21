import math

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
x = int(input("Введите значение х: "))

ya = ((a ** 2) / 3) + (((a ** 2) + 4) / b) + ((((a ** 2) + 4) ** (0.5)) / 4) + ((((a ** 2) + 4) ** 3) ** (0.5)) / 4

print("Задание а) y =", ya)

yb = math.cos(x) + math.sin(x)

print("Задание b) y =", yb)

yc = (((math.cos(x ** 2) ** 2)) + ((math.sin(2*x-1) ** 2))) ** (1/3)

print("Задание c) y =", yc)

yd = 5 * x + 3 * x ** 2 * (1 + math.sin(x) ** 2)

print("Задание d) y =", yd)