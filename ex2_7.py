import random

M = int(input("Введите количество рядов: "))
N = int(input("Введите количество столбцов: "))

matrix = list()

for i in range(M):
    matrix.append([])
    for n in range(N):
        random_number = random.randint(0, 99)
        matrix[i].append(random_number)


for row in matrix:
    for el in row:
        print(el, end=" ")
    print("")


    
                