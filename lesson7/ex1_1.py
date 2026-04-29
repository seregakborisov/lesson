

try:
    weight = float(input("Введите свой вес, кг: "))
    height = float(input("Введите свой рост, м: "))

    bmi = weight / (height * height)
    
    if bmi < 16 and bmi > 0:
        result = "\n Выраженный дефицит массы тела \n"
    elif bmi >= 16 and bmi < 18.5:
        result = "\n Недостаточная масса тела \n"
    elif bmi >= 18.5 and bmi < 25:
        result = "\n ИМТ в норме \n" 
    elif bmi >= 25 and bmi < 30:
        result = "\n Предожирение"
    elif bmi >= 30 and bmi < 35:
        result = "\n Ожирение 1-й степени\n"
    elif bmi >= 35 and bmi < 40:
        result = "\n Ожирение 2-й степени \n"
    elif bmi >= 40:
        result = "\n Ожирение 3-й степени \n"
    elif bmi <= 0:
        result = "\n Масса тела не может быть меньше либо равна нулю! \n"
        bmi = "..."
        
    print(result)
    print(f" Индекс массы тела = {bmi} \n") 
    
except ValueError:
    print("\n !!! Введены некорректные данные!!! \n")
    
except ZeroDivisionError:
    print("\n Рост или масса не может быть равен нулю! \n")