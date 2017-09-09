import random
x = 31 # количество дней 
tries = 0
z = 0
for i in range(0, 31):
    y = random.randint(0, 1)
    print(i, ':', y)
    if y == 0:
        z += 1
   
print(z >= 10)

