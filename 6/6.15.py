a = float(input("Введите число "))
f0 = 1
f1 = 1 + 1 / 2
f = 1 + 1 / 3
tries = 0
while f < a:
    print("f0= ",f0,"f1=",f1,"f=",f)
    f = f0 +f1
    f0 = f1
    f1 = f
    tries += 1
    
