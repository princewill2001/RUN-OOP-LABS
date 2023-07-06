#Lab 2: Inheritance and Polymorphism
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
       return f"Name: {self.name}, Age: {self.age}"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

def __str__(self):
    return f"Dog: {self.name}, Age: {self.age}, Breed: {self.breed}"

animal = Animal("Keegan", 6)
print(animal)

dog = Dog("Duddy", 4, "German Shepherd")
print(dog)