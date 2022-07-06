# DICCIONARIOS
capitales = {
    'Perú' : 'Lima',
    'Ecuador' : 'Quito',
    'Chile' : 'Santiago',
    'Uruguay' : 'Montevideo'
}
print(capitales)

# AGREGAR UN ELEMENTO AL DICCIONARIO
nuevaCapital = {'Brasil':'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)

# ACTUALIZAR UN ELEMENTO
capitales.update({'Ecuador':'Guayaquil'})
# Imprimir solo un elemento
print(capitales.get('Ecuador'))

# # Ingresar un país e imprimir su capital
# pais = input("Ingrese el país: ")
# capital = capitales.get(pais,'no está registrada')
# print("La capital de " + pais + " es " + capital)

# ELIMINAR UN ELEMENTO
c = capitales.pop('Chile', 'no existe')
print("eliminaste "+ c)
print(capitales)

# ITERACIÓN DE DICCIONARIOS
for capital in capitales:
    print('La capital de ' + capital +" es " + capitales[capital])
print(capitales.keys())
print(capitales.values())
print(capitales.items())

for clave in capitales.keys():
    print(clave + " => " + capitales[clave])

for clave, valor in capitales.items():
    print(clave + " -- " + valor)
