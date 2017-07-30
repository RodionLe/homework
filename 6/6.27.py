x = int(input("Введите натуральное число: "))

min = x % 10
max = x % 10

while x > 0:
    a = x % 10    
    x = x // 10

    if a < min:
        min = a
    if a > max:
        max = a

print("min =", min)
print("max =", max)
