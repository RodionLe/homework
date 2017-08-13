n = int(input("Введите число"))
y = 0
z = 0
m = 0
t = 1
for i in range(1,n+1):
    y = 1 / i    
    m += y
    z += y * t
    t = t * -1
    print("Расстояние от дома до работы равно: ",z)
    print('Общий путь',m)
