x = 0
y = 0
i = 0
j = 0
def sentence():    
    a = input("Введите предложение ")
    b = input("Введите предложение ")
    lengthA = len(a)
    lengtgB = len(b)
    for i in range(lengthA - 1):
        if i == "б" or i == "Б":
            x += 1
    for j in range(lengtgB - 1):
         if j == "б" or j == "Б":
            y += 1
    Y = y // 100
    X = x // 100
    return print(Y, X)

sentence()