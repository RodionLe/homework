def F(n):
    if n < 3:
        return 1
    return F(n-1) + F(n-2)

n = int(input("Каое число фибоначчи вы хотите вычеслить? "))
F(n)
print(F(n))
