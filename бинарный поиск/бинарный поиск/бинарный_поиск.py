number = [5, 13, 24, 30, 999, 1000, 5000]
choice = int(input("Введите число "))
length = len(number)
x = length // 2
p = x
while choice != number[p]:
    x //= 2
    if x == 0:
        x = 1
    if choice > number[p]:
        p += x
    elif choice < number[p]:
        p -= x
    else:
        print("номер числа:", p)

    
    
