for i in range(2,50):
    j=1
    count=0
    while j<=i/2:
        if i%j==0:
            count=count+1
        j=j+1
    if count<2:
        print(i)
