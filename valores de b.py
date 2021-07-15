cant = 0
valor = 0
porc = 0.0
b = 0
cont = 0

cant = int(input("Indique cuantos valores seran leidos: "))
b = int(input("Indique b: "))

for i in range(1, cant+1):
    valor = int(input("Valor entero: "))
    if valor < b :
        cont += 1
porc = cont/cant*100

print("\nPorcentaje = ", porc)
