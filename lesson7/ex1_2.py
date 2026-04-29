try: 
    
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))
    operat = input("Введите оператор +, -, * или /: ")
    
    if operat == "+":
        result = a + b
    elif operat == "-":
        result = a - b
    elif operat == "*":
        result = a * b
    elif operat == "/":
        result = a / b
    else: result = "\n Некорректно введен оператор"
    print(result)

except ValueError:
    print("Некорректные данные! Введите число!")