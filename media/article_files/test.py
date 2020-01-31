# Дебильны калькулятор в2

what = input("Что делать? (+, -):")

a = float(input(" Введите первое число: "))
b = float(input(" Введите второе число: "))

if what == "+":
	c = a + b
	print("Результат " + str(c))
elif what == "-":
	c = a - b
	print("Результат " + str(c))
else: 
	input("Выбрана не верная операция")
input()
