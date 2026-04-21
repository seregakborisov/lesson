a = str(input("Введите заданную строку: "))
w = a.split()
b = len(w)
print(b)
#ИИ
c = sum(1 for x in w if x.isalpha() and len(x)>1)
print(c)