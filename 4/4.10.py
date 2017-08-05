rad = int(input("Введите радиус круга "))
side = int(input("Введите сторону квадрата "))
Sr = rad * rad * 3.14 # S круга
Ss = side * side # S квадрата
if Sr > Ss:
    print("Площадь круга больше")
else:
    print("Площадь квадрата больше")
