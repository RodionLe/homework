a = []
n = 8
j = 0
k = 0
for i in range (0,n):
    a.append(int(input()))
for i in range(n - 1):
    if j < a[i] + a[i + 1]:
        j = a[i] + a[i + 1]
for i in range(n):
    if a[i] % 3 == 0:
        a[i] = j
for i in range(0,n // 2):
    k = a[i]
    a[i] = a[n - i - 1]
    a[n - i - 1] = k
print(a)
