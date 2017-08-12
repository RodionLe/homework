n = int(input("Введите числo: "))
z = 0
for i in range (1, n+1):
    y = 1 / i
    if i % 2 ==0:
        y = -y
    elif i % 2 !=0 or y ==1:
        y = y
    z += y
    print(z)
