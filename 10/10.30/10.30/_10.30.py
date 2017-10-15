def sentence(a):    
    length = len(a)
    x = 0
    for i in range(length):
        if a[i] == "б" or a[i] == "Б":
            x += 1

    return (x * 100 ) // (length)

a = input("Введите предложение ")
X = sentence(a)

a = input("Введите предложение ")
Y = sentence(a)

print(X, Y);

if Y < X:
    print("В первом больше букв Б")
elif Y > X:
    print("Во втором больше букв Б")
else:
    print("Одинаково букв Б")