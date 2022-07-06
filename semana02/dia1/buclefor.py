# BUCLE FOR -->siempre inicia desde el 0
# Si quiero que empiece desde el 1 poner range(1,10)--> del 1 al 9
#Si quiero que empiece en 1 y llegue hasta el 10 poner range(1,11)
# Si quiero que vaya de 2 en 2 poner range (1,11,2)
print("EJEMPLO DE BUCLE FOR: ")
for contador in range(3):
    print(contador)

nombre = input("Ingresa tu nombre: ")
print(nombre[1:3])
for contador in nombre:
    print(contador)


