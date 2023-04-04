a=["0","2","3"]
try:
    i=int(input("enter the index value: "))
    print(a[i])
except IndexError:
    print("Can't be executed..Index error")
try:
    b=int(input("Enter number for division: "))
    print(b/int(a[i]))
except ZeroDivisionError:
    print("Division by zero is not possible")
else:
    print("no exception")
finally:
    print("Program ended")