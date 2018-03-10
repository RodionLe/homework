massif = [1700, 1780, 1990 , 3000, 2139, 2200]
length = len(massif)
Max = 0
Min = 0
for i in range(length):
    if massif[i] > Max:
        Max = massif[i]
    elif massif[i] < Min:
        Min = massif[i]
difference = Max - Min
print(difference)
