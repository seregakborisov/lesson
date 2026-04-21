import random

M = int(input("Введите количество рядов или столбцов квадратной матрицы: "))
N = M

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
    
n = len(matrix)

main_sum = 0
second_sum = 0

for i in range(n):
    main_sum += matrix[i][i]
    second_sum += matrix[i][n - i - 1]

print("Главная диагональ:", main_sum)
print("Побочная диагональ:", second_sum)
print(matrix[1][2])