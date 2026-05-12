class Math:
    def addition(self, a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
        return result
    
    def subtraction(self, a, b):
        result = a - b
        print(f"{a} - {b} = {result}")
        return result
    
    def multiplication(self, a, b):
        result = a * b
        print(f"{a} * {b} = {result}")
        return result
    
    def division(self, a, b):
        try:                       
            result = a / b
            print(f"{a} / {b} = {result}")
        except:
            print("Деление на ноль невозможно! ")
                
        

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

math = Math()

math.addition(a, b)     
math.subtraction(a, b)     
math.multiplication(a, b)  
math.division(a, b)        
 