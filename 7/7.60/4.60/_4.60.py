flat = int(input("Введите количество квартир: "))
prev = 0
a = int(input("Введите количество жильцов: "))
num = 1
for i in range (1, flat):
    prev = a
    a = int(input("Введите количество жильцов: ")
    if prev > a:
        a = prev
     
print("В квартире под номером",num,"больше всего жильцов","количество жильцов =",a)
        