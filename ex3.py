n = int(input("Вывести кол-во чисел последовательности Фибоначчи"))

a = 1
b = 1
i = 0

while i < n:
    c = a + b
    print(a)
    a = b
    b = c
    i += 1
    