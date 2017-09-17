number = [5, 4, 2, 3]
length = len(number)
sort = []
flag = True
for i in range(length):
    x = number[i]
    sort.append(x)
    lengthSort = len(sort)
    j = 0
    for j in range(lengthSort - 2, -1, -1):
        if x < sort[j]:
            sort[j + 1] = sort[j]
        else:
            sort[j + 1] = x
            flag = False
            break
    if j == 0 and flag == True:
        sort[j] = x

print(sort)