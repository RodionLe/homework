massif = [2000, 1500, 1000, 500, 200, 100, 50, 25]
length = len(massif)

a = int(input("Введите число: "))
def F(n, a):
    if n >= length :
        return -1
    
    if massif[n] < a:
        return n
    else:
        return F(n+1,a)


    
i = F(0, a)

if i > 0 :
    print(i)
else:
    print("FALSE")


    
    
