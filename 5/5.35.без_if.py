n = int(input("Введите числo: "))
z = 0
x = 1 
for i in range (1, n+1):
    y = 1 / i * x
    x = x * -1
    print(y)
    
