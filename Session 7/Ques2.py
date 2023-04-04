
class circle:
    center=input("Enter center: ")
    radius=input("Enter radius: ")
    def area(self):
        area=3.14*int(self.radius)*int(self.radius)
        return area
    def circumference(self):
        circumference=2*3.14*int(self.radius)
        return circumference
c=circle()
print("--------------------")
print("Center: ",circle.center)
print("Radius: ",circle.radius)
print("Area of circle :",c.area())
print("circumference of circle :",c.circumference())