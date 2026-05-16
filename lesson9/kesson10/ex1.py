def fib(a, b, n):
    x = 0
    while x < n:
        yield a
        a,b = b, a + b
        x += 1

qua = int(input("Введите кол-во выводимых чисел из списка Фиббоначи: "))

for result in fib(0, 1, qua):
    print(result)