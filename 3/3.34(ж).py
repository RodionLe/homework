import math
a = int(input("Введите чило по вертикали от 1 до 8 "))
b = int(input("Введите чило по горизонтали от 1 до 8 "))
c = int(input("Введите чило по вертикали от 1 до 8 "))
d = int(input("Введите чило по горизонтали от 1 до 8 "))
x = math.fabs(a - c) # смещение по x
y = math.fabs(b - d) # смещение по y
if x == 2 and y == 1:
    print("угрожает")
elif x == 1 and y == 2:
    print("угрожает")
else:
    print("не угрожает")
