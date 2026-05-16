def infinity(n):
    cycle = [1, 2, 3]
    i = 0
    z = 0
    while z < n:
       yield cycle[i]
       i += 1
       z += 1
       if i == 3:
           i = 0
       
n = int(input("Введите кол-во чисел из цикла"))

for result in infinity(n):
    print(result, end = ", ") 