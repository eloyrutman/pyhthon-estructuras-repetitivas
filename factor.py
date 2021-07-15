num = 0
fact = 1

num = int(input("Numero entero: "))

for i in range (1, num + 1):
    fact *= i

print("\nEl Factorial de", num, "es:", fact)
