a = float(input("Введите число "))
n = 2
f = 1 + 1 / n
while a < f:
    f = 1 + 1 / n
    n += 1
    print(a)
