class addition:
    def __init__(self):
        self.a=int(input("enter a number "))
    def __add__(self,b):
        return((self.a+b.a)%8)
ob1=addition()
ob2=addition()
print(ob1+ob2)
