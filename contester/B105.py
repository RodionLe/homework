F0 = 1
F1 = 1
F = 2
n = int(input("Введите число"))
for i in range(n):
    F0 = F1
    F1 = F
    F = F1 + F0
    print(F0)
