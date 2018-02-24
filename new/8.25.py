x = 0
for i in range (120, 141):
    x = 0
    for j in range (1, i + 1):
        if i / j == i // j:
            x += 1
    print(x)
