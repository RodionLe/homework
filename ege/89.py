n = int(input())
sell = 0
buy = int(input())
pay_day = 1
buy_day = 1
value = 0
for i in range(2, n + 1  ):
    x = int(input())
    if x < buy:
        buy = x
        t = i
    if x - buy > value:
        value = x - buy
        pay_day = i
        buy_day = t
    print(value, buy_day, pay_day)
