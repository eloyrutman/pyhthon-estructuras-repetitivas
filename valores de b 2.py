resp = "s"
cant = 0
valor = 0
porc = 0.0
cont = 0
b = 0

b = int(input("Valor de B: "))


while resp.upper() == "S":
    valor = int(input("Valor entero: "))
    cant += 1
    if valor < b :
        cont += 1
    resp = input("Seguir --> S; Parar --> N")

porc = cont/cant*100

print("\nPorcentaje = ", porc)
