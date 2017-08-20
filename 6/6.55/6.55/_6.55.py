a = input("Введите число: ")
length = len(a)
i = 0

while i + 1 < length:
    y = a[i]
    z = a[i + 1]

    i += 1
    if y > z:
        break

print("Цифры числа упорядочены по возрастанию:", i == length - 1)
