
number = [5, 2, 4, 6, 1, 3]
minN = 0
length = len(number)
N = length - 1
x = 0
y = 0
j = 0
for i in range(length - 1):
    j += y
    for j in range(N + 1 - y):
        min = number[minN]
        if number[j] < min:
            minN = j

    x = number[j]
    number[j] = number[minN]
    number[minN] = x
    N -= 1
    y += 1
print(number)