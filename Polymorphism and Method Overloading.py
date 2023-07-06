# Lab 4: Polymorphism and Method Overloading
class Shape:
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def calculate_area(self, width, height):
        return width * height
    
class Circle(Shape):
    def calculate_area(self, radius):
        return 3.14 * radius * radius
    
# Test the Shape, Rectangle, and Circle classes
rectangle = Rectangle()
rectangle_area = rectangle.calculate_area(7, 6)
print("Rectangle Area:", rectangle_area)

circle = Circle()
circle_area = circle.calculate_area(4)
print("Circle Area:", circle_area)