N = int(input("Введите количество школ"))
mas = []
Max = 0
for i in range(100):
    mas.append(0)
for i in range(N):
    A = input()
    K = A.split()[2]
    K = int(K)
    mas[K - 1] += 1
for i in range(100):
    if mas[i] > Max:
        Max = mas[i]
print(Max)
