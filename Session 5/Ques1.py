a=["0","2","3"]
try:
    i=int(input("enter the index value: "))
    print(a[i])
except IndexError:
    print("Can't be executed..Index error")
else:
    print("no exception")
