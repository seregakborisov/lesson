str = (input("Введите строку:"))
print(str[2])
l = len(str)
print(str[l-2])
print(str[0:5])
print(str[0:l-2]) #почему один и тот же индекс дает разный результат?
print(str[::2])
print(str[1::2])
rts = str[::-1]
print(rts)
print(rts[::2])
print(l)