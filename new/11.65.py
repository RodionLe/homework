February = [1, 0, 3, 4, 3, 5,0, 0]
length = len(February)
count = 0
for i in range (length):
    if February[i] == 0:
        count += 1

print("Осадков: ", count)
