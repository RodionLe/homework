number = [5, 12, 24, 34, 46, 70,  90 , 110, 140, 180, 250, 333, 438, 549, 674, 890, 1000]

choice = int(input("Введите число: "))
length = len(number)
x = length // 2
p = x
def search(choice):
    global p
    if choice not in number:
        return print("Элемента в массиве нет")
    elif choice != number[p]:
        x = length // 2
        if choice > number[p]:
            p -= x
        else:
            p += x
        print("число - ",choice,"Номер в массиве - ", p)

search(choice)

