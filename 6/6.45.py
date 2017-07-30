x = int(input("Введите натуральное число "))
y = int(input("Введите натуральное число "))
z = int(input("Введите натуральное число "))
while x != 0 and y != 0:
    if x > y:
        x = x % y
    elif y > x:
        y = y % x
x = x + y
while x != 0 and z != 0:
    if x > z:
        x = x % z
    else:
        z = z % x
    print(x + z)
