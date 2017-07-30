y = int(input("Введите угол в градусах: "))
x = 30 #Градусы 
hours = y // 30
min = y % 30 * 2 # 30gr - 60min, 15gr - xmin => x = 15 * 60 / 30
print(min)
