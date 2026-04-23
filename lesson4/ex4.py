from datetime import datetime



def timer(function):

    def count_time():
        start_time = datetime.now()
        function()
        end_time = datetime.now()

        time_delta = end_time - start_time

        print("Функция выполнилась за ", time_delta, " секунд!")
        #print(start_time)
        #print(end_time)
        #print(datetime.now())

    return count_time
    


@timer
def find_num():
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
    """x = -50000
    while x < 5000:
        x +=1
        print(x)"""

find_num()
