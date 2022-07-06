"""
Crear un Programa que convierta Monedas de Soles a Dolares
"""
# Todo programa tiene estas 3 partes
# ENTRADA
monedaOrigen = input("Ingrese moneda origen: ")
montoDestino = 0
# PROCESO
if(monedaOrigen == "soles"):
    montoOrigen = input("Ingrese el monto en "+ monedaOrigen+" : ")
    monedaDestino = "dolares"
    montoDestino = float(montoOrigen) / 3.778
elif(monedaOrigen == "dolares"):
    montoOrigen = input("Ingrese el monto en "+ monedaOrigen+" : ")
    monedaDestino = "soles"
    montoDestino = float(montoOrigen) * 3.778
else:
    print("No se puede convertir a la moneda ingresada")
# SALIDA
if(montoDestino != 0):
    print("El monto en "+ monedaDestino +" es : " + str(montoDestino))