# Lab 1 Introduction to Classes and Objects
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
def calculate_area(self):
    return self.length * self.width

def calculate_perimter(self):
    return 2 * (self.length + self.width)

rect = Rectangle(5, 3)
print("Area:", rect.calculate_area())
print("Perimeter:", rect.calculate_perimter())