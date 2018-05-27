N = int(input())
mm = mb = maxp = int(input())

for i in range(N - 1):
    x = int(input())
    t = min(mm * x, min(mb * x, x))
    mb = max(mb * x, mm *x, x)
    maxp = max(mb, maxp)
    mm = t
print(maxp)
