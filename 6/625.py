a = int(input("Введите натуральное число "))
y = 0
while a != 0:
    b = a
    a = int(input("Введите натуральное число "))
    if a < 0 and b > 0 or a > 0 and b < 0:
        y += 1
print("Знак меняется",y,"раза")
        
        
