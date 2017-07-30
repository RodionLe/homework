x = int(input("Введите натуральное число "))
y = int(input("Введите натуральное число "))
z = int(input("Введите натуральное число "))
while x != y:
    if x > y:
        x = x % y
    else:
        y = y % x
    x = x + y

while x != z:
    if x > z:
        x = x % z
    else:
        z = z % x
    x = x + z
print(x)
