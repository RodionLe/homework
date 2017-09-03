n = int(input("Введите количество покупателей: "))
t = int(input("Введите время обслуживания ")) # время обслуживания продавцом
c = [] #Время прибывания покупателя в очереди 
num = 0  # 
min = t
x = 0
c.append(t)

for i in range(1, n):
    t = int(input("Введите время обслуживания: "))
    if t < min:
        min = t 
    num = t + c[i - 1]
    c.append(num)

for i in range(0, n):
    print(i + 1, ":",  c[i])