"""
EJERCICIO 1:
INGRESE UN TEXTO Y UN DIVISOR Y LUEGO MUESTRE EL MISMO TEXTO PERO DIVIDIDO POR EL DIVISOR

EJEMPLO:
TEXTO = ABCDEF
DIVISOR = 2
RESULTADO:
AB
CD
EF
G
"""
# ENTRADA
texto = input("Ingrese el texto: ")
divisor = int(input("Ingrese divisor: "))
# PROCESO
# texto[0:2]
# texto[2:4]
for contador in range(0,len(texto), divisor):
    # con este for el texto va ir de 2 en 2
    # SALIDA
    print(texto[contador:divisor+contador])
