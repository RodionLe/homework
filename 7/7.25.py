a = int(input("Введите количество учеников: "))
y = 0
for i in range(a):
    x = int(input("Введите оценку ученика: "))
    if x == 5:
        y += 1
print(y)
        
