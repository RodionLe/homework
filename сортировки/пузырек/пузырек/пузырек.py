number = [5, 3, 4, 2, 1]
length = len(number)
x = 0
N = length - 1
z = 0

for j in range(N):
    flag = True
    for i in range(length - 1):
        x = number[i]
        y = number[i + 1]
        if x > y: 
            z = number[i]
            number[i] = number[i + 1]
            number[i + 1] = z
            flag = False
    if flag:
        break
print(number)
       

