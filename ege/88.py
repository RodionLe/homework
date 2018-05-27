n = int(input())
buy = x = int(input())
sell = 0
maxp = 0
for i in range(n - 1):
    a = int(input())
    if a < buy:
        buy = a
        sell = 0
    if a > sell:
        sell = a
    if sell - buy > maxp:
        maxp = sell - buy
    print(sell, buy, maxp)
    print(maxp)

print("""n = int(input())
buy = x = int(input())

maxp = 0
for i in range(n - 1):
    a = int(input())
    if a < buy:
        buy = a
       
   
    if a - buy > maxp:
        maxp = a - buy
   
print(maxp)
""")
