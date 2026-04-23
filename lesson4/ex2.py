
n = input("Ваши числа: ")

#num = [-4, -3, -2, 2, 3, 4]

num = list(map(int, n.split()))

result = list(filter(lambda x: x > 0, num))

print("Положительные числа:", result)