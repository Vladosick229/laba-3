import math

x = float(input("Введите значение x: "))

if x < 0:
    f_x = x ** 2
else:
    f_x = math.sqrt(x)

print(f"f({x}) = {f_x}")