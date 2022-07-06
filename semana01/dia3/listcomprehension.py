listaNombre = []
strNombre = "cesar mayta"
for strLetra in strNombre:
    listaNombre.append(strLetra)

print(listaNombre)
listaNombre = [strLetra for strLetra in strNombre]
print(listaNombre)

listaNumeros = [num for num in range(101)]
print(listaNumeros)

print("=" * 100)

listaMultiploDeDos = []
for numero in range(101):
    if numero % 2 == 0:
        listaMultiploDeDos.append(numero)
print(listaMultiploDeDos)

# CON LIST COMPREHENSION, reduce la cantidad de líneas del for anterior
print("usando list comprehension")
listaMultiploDeDos = [numero for numero in range(50) if (numero % 2 == 0)]
print(listaMultiploDeDos)