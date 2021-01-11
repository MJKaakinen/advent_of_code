file = open("2text.txt","r")

arr = []

while 1:
    docline = file.readline()
    if docline:
        count = 0
        splitted = docline.split(" ")
        thischar = splitted[1][0]
        password = splitted[2]
        for i in password:
            if i == thischar:
                count += 1
        window = splitted[0].split("-")
        if count >= int(window[0]) and count <= int(window[1]):
            arr.append(docline) 
            print(docline)
    else:
        break
print(len(arr))
file.close()