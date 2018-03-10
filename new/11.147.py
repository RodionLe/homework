massif = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
length = len(massif)
var = 0
i = 0
while i != 4:
    var = massif[i + 2]
    massif[i + 2] = massif[8 - i]
    massif[8 - i] = var
    i += 1
print(massif)
