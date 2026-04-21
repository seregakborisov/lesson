def search(arr, target, left, right):
    
    mid = (left + right)  // 2 
    
    if arr[mid] == target: 
        return mid  
    elif arr[mid] < target: 
        return search(arr, target, mid + 1, right)  
    else: 
        return search(arr, target, left, mid - 1)  

arr = list(map(int, input("Введите список: ").split()))
target = int(input("Введите число: "))
result = search(arr, target, 0, len(arr) - 1)

print("Индекс искомого числа:", result)