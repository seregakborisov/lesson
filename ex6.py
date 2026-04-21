num = list(map(int, input("Введите список: ").split()))
x = int(input("Введите искомое число: "))


left = 0
right = len(num) - 1

while left <= right:
    mid = (left + right) // 2
    
    if num[mid] == x:
        print("Искомое число находится на позиции", mid + 1) #Выводить индекс или человеческий порядок? Если индекс, то убрать "+ 1"
        break
    
    if num[mid] < x:
        left = mid + 1
    else:
        right = mid - 1