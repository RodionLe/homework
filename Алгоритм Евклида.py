x = int(input("Введите число "))
y = int(input("Введите число "))
while x != 0 and y != 0:
    if x > y:
        x = x % y
    else:
        y = y % x
print(x + y)
    
