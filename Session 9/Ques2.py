def MyGenerator():
    x=0
    while x<10:
        yield x
        x +=1
l= list(MyGenerator())
print(type(l))
for y in l:
    print(y)

