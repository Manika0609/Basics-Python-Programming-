def count_letter():
    file = open("file.txt","r")
    data = file.read()
    count = 0
    for letter in data:
        if letter.isupper() or letter.islower():
            count+=1
    print(count)
count_letter()