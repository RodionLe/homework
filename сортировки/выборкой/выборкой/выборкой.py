number = [5, 2, 4, 6, 1, 3]

length = len(number)

for i in range(length):
    minN = i
    for j in range(i + 1, length):
        if number[j] < number[minN]:
            minN = j

    x = number[i]
    number[i] = number[minN]
    number[minN] = x
   
print(number)