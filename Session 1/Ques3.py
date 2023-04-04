print("Enter marks of 5 subjects")
x=["0","0","0","0","0"]
sum=0
for i in x:
    i=int(input())
    sum=sum+i
avg=sum/5
if(avg>=91 and avg<=100):
    print("Grade:O")
elif(avg>=81 and avg<=90):
    print("Grade:A+")
elif(avg>=71 and avg<=80):
    print("Grade:A")
elif(avg>61 and avg<=70):
    print("Grade:B+")
elif(avg>51 and avg<=60):
    print("Grade:B")
elif(avg>41 and avg<=50):
    print("Grade:C+")
elif(avg>35 and avg<=50):
    print("Grade:C")
else:
    print("Fail")
