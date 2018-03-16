number = [5, 12, 24, 34, 46, 70,  90 , 110, 140, 180, 250, 333, 438, 549, 674, 890, 1000]
choice = int(input("Введите число: "))
length = len(number)
y = choice
x = length // 2
p = x
def search(y, x, p):
    if y not in number:
        return print("Элемента в массиве нет")
    else:
        if y > number[p]:
            p -= x
            x //= 2
            return search(y,x,p)
        elif y < number[p]:
            p += x
            x //= 2
            return search(y,x,p)
        else:
            return print("номер числа в массиве: ",p)
search(y, x, p)
