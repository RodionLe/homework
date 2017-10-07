import math
def area():
    a = float(input("Введите a "))
    b = float(input("Введите b "))
    c = float(input("Введите c "))
    d = float(input("Введите d "))
    e = float(input("Введите e "))
    f = float(input("Введите f "))
    g = float(input("Введите g "))

    S1 = (a * b) // 2 
    S2 = (e * d) // 2
    x = math.sqrt(f*f - (c*c /4)) # Высота треугольника cgf
    S3 = (c * x) / 2
    return print("Площадь пятиугольника равна: ", S1 + S2 + S3)
area()