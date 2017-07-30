x = int(input("Введите число "))
y = int(input("Введите число "))
while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
print(x)

