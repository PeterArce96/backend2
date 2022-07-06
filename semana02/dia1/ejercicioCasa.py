"""
"ejercicio para casa"
[23:02]
incorporar un menu de opciones para el programa monedas que tenga 3 opciones 1 - convertir de soles a dolares 2 - convertir de dolares a soles 3 - salir , y que se ejecute con un ciclo while mientras la opción no sea salir, si selecciono la opción salir debe terminar el programa
[23:02]
enviar por retos el ejercicios desarrollado
"""
# opcion = 1
# while (opcion > 0):
#     opcion = int(input("ingrese una opción: "))
#     print("seleccionó la opción " + str(opcion))

# ENTRADA
opcion = 0
montoDestino = 0

# PROCESO
while(opcion != 3):
    opcion = int(input("Ingrese opción a realizar (1-2-3): "))
    if (opcion == 1):
        monedaOrigen = "soles"
        monedaDestino = "dolares"
        montoOrigen = input("Ingrese monto en "+ monedaOrigen +" a convertir: ")
        montoDestino = float(montoOrigen) / 3.778
        print("El monto en "+ monedaDestino +" es : " + str(montoDestino))
    elif(opcion == 2):
        monedaOrigen = "dolares"
        monedaDestino = "soles"
        montoOrigen = input("Ingrese monto en "+ monedaOrigen +" a convertir: ")
        montoDestino = float(montoOrigen) * 3.778
        print("El monto en "+ monedaDestino +" es : " + str(montoDestino))
    elif(opcion == 3):
        print("Usted salió del programa")
        quit()
    else:
        print("Marque una opcion correcta del 1 al 3: ")
        

