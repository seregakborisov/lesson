def binar(n):
    
    b = ''

    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

n = int(input("Введите числоЖ "))

result = binar(n)

print("В двоичной системе число = ", result)