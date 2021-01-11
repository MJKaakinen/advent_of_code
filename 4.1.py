file = open("text.txt","r")

arr = []
valids = 0
fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
flow = True

while flow:
    temp = []
    while 1:
        docline = file.readline()
        if not docline:
            flow = False
            break
        elif len(docline.strip()) != 0:
            temp.append(docline)
        else:
            break
    passport = ''.join(temp)
    field_check = 0
    for code in fields:
        if code in passport:
            field_check += 1
    if field_check == len(fields):
        valids += 1
    #else:
        #print(field_check)
file.close()
print(valids)
