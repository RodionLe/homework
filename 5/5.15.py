n = int(input("Введите число от 1 до 9 "))
x = n * 10
for i in range (n, x, n):
    print(i, end=" ")
