file = open("2text.txt","r")

arr = []

while 1:
    docline = file.readline()
    if docline:
        count = 0
        splitted = docline.split(" ")
        thischar = splitted[1][0]
        password = splitted[2]
        window = splitted[0].split("-")
        if password[int(window[0])-1] == thischar:
                count += 1
        if password[int(window[1])-1] == thischar:
                count += 1
        if count == 1:
            arr.append(docline) 
        else:
            print(docline + " " + str(count))
    else:
        break
print(len(arr))
file.close()