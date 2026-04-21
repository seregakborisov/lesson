"""def prime(n):
    if n <= 1:
        return False
    
    if n > 1:
        z = 1  
        for i in range(1, n):
            while z > 1:
                if n % 1 == 0:
                    z += 1
        if z > 1:
            return False
        else:
            return True
                #???????????
    
n = int(input("Введите число: "))
result = prime(n)

print(result)"""

def prime(n):
    d = 2
    if n > 1:
        while n % d != 0:
            d += 1
    return d == n

n = int(input("Введите число: "))
result = prime(n)

print(result)