class MyError(Exception):
    pass

def divide(x, y):
    try:
        if y==0:
            raise MyError
    except MyError:
        print("Cannot Divide by ZERO! ")
    else:
        print("Answer: ", x/y)
divide(12, 6)
divide(7, 0)