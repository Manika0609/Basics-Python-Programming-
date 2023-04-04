class rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    def area(self):
        area=int(self.length)*int(self.breadth)
        return area
class square(rectangle):
    def __init__(self,s):
        self.side = s
    def area(self):
        area=int(self.side)*int(self.side)
        return area
sq1=square(5)
rec1=rectangle(2,6)
print("Area of square :",sq1.area())
print("Area of rectangle :",rec1.area())
print("enter the figure:\nSquare or Rectangle")
x=input()
if(x=='square'):
    print("enter dimensions")
    s=int(input())
    sq=square(s)
    print("---------------------")
    print("Area of square :",sq.area())
elif(x=='rectangle'):
    print("enter dimensions")
    l=int(input())
    b=int(input())
    rec=rectangle(l,b)
    print("--------------------")
    print("Area of rectangle :",rec.area())
else:
    print("WRONG CHOICE!!!!")
