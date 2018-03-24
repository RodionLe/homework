mas = [1 , 15, -2, 100, -300, 124, -43, 33, 2121, -1234]
length = len(mas)
count = 0
for i in range (length):
    if mas[i] < 0:
        count += 1
print(count)
