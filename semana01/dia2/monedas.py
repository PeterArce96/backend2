# Programa para convertir Monedas
# Version 1.0

opcion = 0
# ENTRADAS
while(opcion != 3):
    print(
        """
        OPCIÓN 1 : Convertir de soles a dolares
        OPCIÓN 2 : Convertir de soles a dolares
        OPCIÓN 3 : Salir del programa
        """
    )
    opcion = int(input("ingrese la opción que desee: "))
    if(opcion == 1):
        montoOrigen = float(input("Ingrese monto en soles: "))
        montoDestino = montoOrigen / 3.8
        print("El monto en dolares es: "+ str(montoDestino))
    elif(opcion == 2):
        montoOrigen = float(input("Ingrese monto en dólares: "))
        montoDestino = montoOrigen * 3.8
        print("El monto en soles es: "+ str(montoDestino))
    else:
        print("--DEBE MARCAR UNA OPCIÓN VÁLIDA--")

    if(opcion == 3):
        print("ADIOS!")
# PROCESO
# SALIDA