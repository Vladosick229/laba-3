import math

x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
R = float(input("Введите радиус круга R: "))

distance = math.sqrt(x**2 + y**2)

if distance <= R:
    print("Точка находится внутри круга.")
else:
    print("Точка находится вне круга.")
