flatCount = int(input("Введите количество квартир: "))

maxPeaple = -1
maxFlat = -1

flat = None
for i in range (1, flatCount + 1):
    flat = int(input("Введите количество жильцов: "))
    
    if flat > maxPeaple:
        maxPeaple = flat
        maxFlat = i
    
print("В квартире под номером", maxFlat, "больше всего жильцов","количество жильцов =", maxPeaple)
        