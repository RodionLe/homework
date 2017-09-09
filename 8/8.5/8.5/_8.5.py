for i in range(1, 10):   
    for j in range(1, 10):
        x = j + i
        x = str(x) + " " * (2 - len(str(x)))
        print('%s+%s=%s' % ( i, j, x ), end="  ")
    print()

