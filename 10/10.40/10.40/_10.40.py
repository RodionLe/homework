import math
def trap():
    a1 = int(input("Введите меньшее основание первой трапеции "))
    a2 = int(input("Введите большее основание первой трапеции "))
    h1 = int(input("Введите высоту первой трапеции "))
    S1 = (a1 + a2)//2 * h1
    x = (a2 - a1)//2 # часть основания 
    side1 = math.sqrt((x * x) + (h1 * h1))
    P1 = a1 + a2 + side1 * 2
    
    b1 = int(input("Введите меньшее основание второй трапеции "))
    b2 = int(input("Введите большее основание второй трапеции "))
    h2 = int(input("Введите высоту второй трапеции "))
    S2 = (b1 + b2)//2 * h2
    x = (b2 - b1)//2 # часть основания 
    side2 = math.sqrt((x * x) + (h2 * h2))
    P2 = b1 + b2 + side2 * 2
    return print("Сумма площедей равна: ", S1 + S2, "Сумма периметров равна: ", P1 + P2)
trap()