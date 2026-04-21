import math

x = int(input("Введите х: "))
n = int(input("Введите число n:"))

s = 0
n_start = 0

while n_start <= n:
    result = ((-1) ** n_start) * (x ** (2 * n_start)) / math.factorial(2 * n_start)
    s += result
    n_start += 1

print("Сумма всех =", s, "~~", "cos(x) = ", math.cos(x))

