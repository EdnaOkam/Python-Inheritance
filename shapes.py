class Shape:
    def __init__ (self, color, filled ):
        self.color = color 
        self.filled = True or False

    def display_info(self):
        print(f"Shape Color: {self.color} \nShape Filled: {self.filled}")

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"Raduis of Circle: {self.radius}")

    def area(self):
        circle_area = 3.14 * self.radius**2
        print(f"Area of Circle : {circle_area}")
    
class Rectangle(Shape):
    def __init__(self, color, filled, length, width):
        super().__init__(color, filled)
        self.length = length
        self.width = width 

    def display_info(self):
        super().display_info()
        print(f"Length of Rectangle: {self.length} \nWidth of Rectangle: {self.width}")

    def area(self):
        rectangle_area = self.length * self.width
        print(f"Area of Rectangle: {rectangle_area}")

class Triangle(Shape):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.base = base 
        self.height = height

    def display_info(self):
        super().display_info()
        print(f"Base of Triangle: {self.base} \nHeight of Triangle: {self.height}")

    def area(self):
        triangle_area = 0.5 * self.base * self.height 
        print(f"Area of Triangle: {triangle_area}")

circle1 = Circle("Yellow", False, 10)
circle1.display_info()
rectangle1 = Rectangle("Green", True ,4 , 8)
rectangle1.display_info()
triangle1 = Triangle("Red", True, 3, 9)
triangle1.display_info()