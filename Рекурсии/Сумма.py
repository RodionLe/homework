def F(n):
    if n == 0:
        return 0
    return n + F(n - 1)
n = int(input("сумму каких чисел вы хотите узнать "))
F(n)
print(F(n))
