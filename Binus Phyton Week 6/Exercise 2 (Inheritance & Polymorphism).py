# Parent Class
class Shape:
  def area (self):
    return 0
    
# Child Class 1
class Rectangle (Shape):
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def area(self):
    return self.length * self.width
    
# Child Class 2
class Circle (Shape):
  def __init__(self, radius):
    self.radius = radius
  def area(self):
    return 3.14 * self.radius ** 2

shapes = [Rectangle(5, 3), Circle(4), Rectangle(10, 2), Circle(7)]

for shape in shapes:
    print("Luas:", shape.area())