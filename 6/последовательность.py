current = int(input("Введите натуральное число "))
count = 1
maxCount = 1

while current != 0:
    prev = current
    current = int(input("Введите натуральное число "))
    if prev == current:
        count += 1
    else:
        if count > maxCount:
            maxCount = count
        count = 1
print(maxCount)
