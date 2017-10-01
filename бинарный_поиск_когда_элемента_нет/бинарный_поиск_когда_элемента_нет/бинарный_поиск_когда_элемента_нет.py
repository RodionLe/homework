number = [5, 12, 24, 34, 46, 70,  90 , 110, 140, 180, 250, 333, 438, 549, 674, 890, 1000]
choice = int(input("Введите число: "))
length = len(number)
x = length // 2
p = x
while choice != number[p]:
    if choice not in number:
        p = "элемента нет в масиве"
        break
    x //= 2
    if x == 0:
        x = 1
    if choice > number[p]:
        p += x
    elif choice < number[p]:
        p -= x
    else:
        print("номер числа:",p)
print(p)

