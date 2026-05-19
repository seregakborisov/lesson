from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __str__(self):
        return f"Гав!"
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        pass
    
    def __str__(self):
        return f"Мяу!"
        
class AnimalFactory:
    def create_animal(self, animal_type):
        
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Неверно введено животное")


creat = AnimalFactory()

type_anim = input("Введите животное (cat или dog): ")

animal = creat.create_animal(type_anim)

print(animal)

type_anim2 = input("Введите животное (cat или dog): ")

animal2 = creat.create_animal(type_anim2)

print(animal2)


