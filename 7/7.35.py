n = int(input("Введите количество чисел: "))
num = 0
x = 0
y = 0
a = int(input("Введите число "))
for i in range(n - 1):
    x = a
    a = int(input("Введите число "))
    if x == a:
        y += 1
print(y)
