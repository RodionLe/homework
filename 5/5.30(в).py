n = int(input("Введите число от 1 до 100: "))
y = 0
for i in range(1,n + 1):
    x = i * i
    y += x
    print(y)
