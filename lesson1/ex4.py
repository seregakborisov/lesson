str = str(input("Введите строку:"))
first = str.find('h')
last = str.rfind('h')
l = len(str)

strA = str[0:first+1]
strB = str[first+1:last]
strC = str[last:l]
strX = (strB.replace("h" , "H"))
strS = strA + strX + strC

print(strA , strX , strC) #Можно ли сделать вывод без пробелов?
print(strS)