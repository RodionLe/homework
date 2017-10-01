number = [5, 12, 24, 34, 46, 70,  90 , 110, 140, 180, 250, 333, 438, 549, 674, 890, 1000]
choice = int(input("Введите число: "))
length = len(number)
x = length // 2
p = x
tries = 0

if choice not in number:
    p = "элемента нет в масиве"
    exit

while choice != number[p]:
    
    x //= 2
    if x == 0:
        x = 1
        
    if choice > number[p]:
        p += x
        tries += 1
    elif choice < number[p]:
        p -= x
        tries += 1
    else:
        print("номер числа:",p)
print("номер числа:",p ,"Компьютер отгадал за",tries ,"попыток")

