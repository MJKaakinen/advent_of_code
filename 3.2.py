file = open("text.txt","r")

arr = []

while 1:
    docline = file.readline()
    if docline:
        layer = docline[:-1]*100
        print(docline)
        arr.append(layer)
    else:
        break
trees_total = 1
trees = 0
for i in range(1,len(arr)):
    if arr[i][i] == '#':
        trees+=1
print("trees: " + str(trees))
trees_total *= trees
trees = 0
for i in range(1,len(arr)):
    if arr[i][i*3] == '#':
        trees+=1
print("trees: " + str(trees))
trees_total *= trees
trees = 0
for i in range(1,len(arr)):
    if arr[i][i*5] == '#':
        trees+=1
print("trees: " + str(trees))
trees_total *= trees
trees = 0
for i in range(1,len(arr)):
    if arr[i][i*7] == '#':
        trees+=1
print("trees: " + str(trees))
trees_total *= trees
trees = 0
for i in range(0,len(arr)):
    if i % 2 == 0:
        if arr[i][int(i/2)] == '#':
            trees+=1
            print(str(i) + " - " + str(i/2) + " - " + arr[i][int(i/2)])
print("trees: " + str(trees))
trees_total *= trees
print(trees_total)
file.close()