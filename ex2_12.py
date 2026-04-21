import random

M = int(input("Введите количество рядов: "))
N = int(input("Введите количество столбцов: "))
H = int(input("Введите искомое число: "))

matrix = list()

for i in range(M):
    matrix.append([])
    for n in range(N):
        random_number = random.randint(0, 9)
        matrix[i].append(random_number)


for row in matrix:
    for el in row:
        print(el, end=" ")
    print("")



rows = len(matrix)
cols = len(matrix[0])
found_H = None

for j in range(cols):    
    for i in range(rows):
        if matrix[i][j] == H:
            found_H = True
            break

    if found_H == True:
        print(f"Столбец {j}: есть число {H}")
    else:
        print(f"Столбец {j}: нет числа {H}")