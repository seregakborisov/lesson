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

min_val = matrix[0][0]
max_val = matrix[0][0]
    
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
            
        if matrix[x][y] < min_val:
            min_val = matrix[x][y]
            min_pos = (x, y)
                
        if matrix[x][y] > max_val:
            max_val = matrix[x][y]
            max_pos = (x, y)
        
print(f"Сумма всех элементов: {sum}")            
print(f"Минимальное число {min_val} находится на позиции {min_pos}, максимальное число {max_val} находится на позиции {max_pos}")
    
                