import random
mas = [[1,2,3],[4,5,6]]
length = len(mas)
x = random.randint(0, length - 1)
y = random.randint(0, 2)
n = random.randint(0, length - 1)
m = random.randint(0, 2)
Sum = mas[x][y] + mas[n][m]
print(Sum)
