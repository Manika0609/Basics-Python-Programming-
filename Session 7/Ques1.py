
class rectangle:
    length=5
    breadth=6
    def area(self):
        area=int(self.length)*int(self.breadth)
        return area
    def perimeter(self):
        perimeter=2*(int(self.length)+int(self.breadth))
        return perimeter
rec=rectangle()
print("--------------------")
print("Length: ",rectangle.length)
print("breadth: ",rectangle.breadth)
print("Area of rectangle :",rec.area())
print("Perimeter of rectangle :",rec.perimeter())