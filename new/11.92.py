mas = [170, 180, 190, 177, 188, 160, 188, 200 , 178, 183]
length = len (mas)
Sum = 0
count = 0

for i in range (length):
    Sum += mas[i]

mid = Sum // length

for i in range(length):
    if mas[i] >= mid:
        count += 1

print(count)
