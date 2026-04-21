import random

M = int(input("Введите количество рядов: "))
N = int(input("Введите количество столбцов: "))
sum = 0

matrix = list()

for i in range(M):
    matrix.append([])
    for n in range(N):
        random_number = random.randint(0, 99)
        matrix[i].append(random_number)


for row in matrix:
    for el in row:
        sum += el
        print(el, end=" ")
    print("")

rows = len(matrix)
cols = len(matrix[0])
    
sum = 0
sum_col = [0] * cols
    
for i in range(rows):
    for j in range(cols):
        sum += matrix[i][j]
        sum_col[j] += matrix[i][j]
        
print(f"Общая сумма: {sum}")   

for j in range(cols):
    pres = sum_col[j] / sum * 100
    print(f"Столбец {j}: сумма = {sum_col[j]}, доля = {pres:.2f}%")

                