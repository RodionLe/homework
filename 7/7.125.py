n = 5
x = 0
a = int(input("Введите число "))
y = 1
for i in range(4):
    x = a
    a = int(input("Введите число: "))
    if x > a:
        break
    if a > x:
        y += 1
print(y)
