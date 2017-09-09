number = [5, 3, 4, 2, 1]
maxN = 0
length = len(number)
N = length - 1
x = 0
for i in range(length - 1):
    for j in range(N+1):
        max = number[maxN]
        if number[j] > max:
            maxN = j

    x = number[N]
    number[N] = number[maxN]
    number[maxN] = x
    N -= 1


