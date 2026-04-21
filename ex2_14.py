
matrix = [
    [1, 0, 1],
    [1, 0, 0],
    [1, 1, 1]
]

for row in matrix:
    ones = sum(row)

    if ones % 2 == 0:
        row.append(0)
    else:
        row.append(1)

print(matrix) #Вывод матрицы в строку! 
