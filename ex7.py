numbers = list(map(int, input("Введите список: ").split()))
target = int(input("Что ищем: "))

left = 0
right = len(numbers) - 1

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        print("Найдено на позиции:", mid)
        break

    if numbers[left] <= numbers[mid]:
        if numbers[left] <= target < numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if numbers[mid] < target <= numbers[right]:
            left = mid + 1
        else:
            right = mid - 1