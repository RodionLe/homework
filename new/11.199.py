massif = [2000, 1500, 1000, 500, 200, 100, 50, 25]
length = len(massif)
a = int(input("Введите число: "))
i = 0
count = 0
for i in range(0, length - 1):
    if massif[i] < a:
        count += 1
        break
if count == 1:
    print("номер числа :",i )
else:
    print("числа нет в массиве")
    
