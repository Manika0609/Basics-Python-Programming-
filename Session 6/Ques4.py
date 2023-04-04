file=open("file2.txt","w")
file.write("My Name is Aarushi\n  I live in Noida\n ")
for line in file:
    print(line)
file.close()

