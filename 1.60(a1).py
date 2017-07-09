a=(input("ведите число a "))
b=(input("ведите число b "))
c=(input("ведите число c "))
buf = b
b = c
c = a
a = buf
print(a, b, c)
