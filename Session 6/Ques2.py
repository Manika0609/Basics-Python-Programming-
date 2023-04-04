file=open("file2.txt","w")
file.write("My Name is Manika.\n live in New Delhi.\n")
file.close()
file=open("file2.txt","r")
count=0
data=file.read()
data=data.split("\n")
for i in data:
    if i:
        count+=1
print("No. Of lines in File are:",count)
file.close()