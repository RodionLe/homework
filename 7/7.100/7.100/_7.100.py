n = int(input("Введите натуральное число n: "))
m = int(input("Введите число m: "))
p = int(input("Введите число p: "))
sum = 0
for i in range(n):
    d =  int(input("Введите число d: "))
    if d <= m:
        sum += d
if sum // p == sum / p:
    print("Сумма чисел 'd' кратна числу p")
else:
    print("Сумма чисел 'd' не кратна числу p")
