import random
sportS = []
for i in range(0, 8):
    row = []
    for j in range(0, 5):
        s = random.randint(1, 1000)
        row.append(s)
    sportS.append(row)


for i in range(0, 8):
    for j in range(0, 5):
       print(sportS[i][j], end=" ")
    print()
