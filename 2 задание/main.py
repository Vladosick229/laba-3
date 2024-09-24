num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = "Числа равны" if num1 == num2 else (f"Наименьшее число: {num1}" if num1 < num2 else f"Наименьшее число: {num2}")

print(result)