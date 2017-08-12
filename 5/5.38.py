n = int(input("Введите число"))
y = 0
z = 0
m = 0
for i in range(1,n+1):
    y = 1 / i
    x = 1 / i
    m +=x
    if i % 2 == 0:
        y = -y
    elif i % 2 !=0 or y == 1:
        y = y
    z += y
    print("Расстояние от дома до работы равно: ",z)
    print('Общий путь',m)
