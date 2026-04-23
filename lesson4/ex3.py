
s = input("Введите слова: ")

word = list(map(str, s.split()))

#word = list(map(str, input("Введите слова: ").split()))

result = list(filter(lambda x:  x == x[::-1], word))

print("Паллиндромы: ", result)