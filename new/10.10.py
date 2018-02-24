import math
summ = 0
a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))
d = float(input("Введите число: "))
e = float(input("Введите число: "))
f = float(input("Введите число: "))
g = float(input("Введите число: "))
def area(a,b,c):
    global summ
    P = (a + b + c) / 2
    summ += math.sqrt(P*(P-a)*(P - b)*(P - c))
    return summ
area(a,b,c)
area(g,f,c)
area(e,f,d)
print(summ)
