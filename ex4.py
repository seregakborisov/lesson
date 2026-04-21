x = list(input("Введите список чисел: ").split())

i = 0
s = 0
num_min = int(x[0])
num_max = int(x[0])

while i < len(x):
    num = int(x[i])
    s += num
    if num < num_min:
        num_min = num
    if num > num_max:
        num_max = num
    i += 1

print(s)
print(num_min)
print(num_max)