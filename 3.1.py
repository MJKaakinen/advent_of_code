file = open("text.txt","r")

arr = []

while 1:
    docline = file.readline()
    if docline:
        layer = docline[:-1]*33
        print(docline)
        arr.append(layer)
    else:
        break
clears = 0
trees = 0
for i in range(1,len(arr)):
    if arr[i][i*3] == '.':
        clears+=1
        print(str(i) + " - " + str(i*3) + " - " + arr[i][i*3])
    else:
        trees+=1
        print(str(i) + " - " + str(i*3) + " - " + arr[i][i*3])
#for i in range(0,len(arr)):
#    print(arr[i])
print(clears)
print(trees)
file.close()