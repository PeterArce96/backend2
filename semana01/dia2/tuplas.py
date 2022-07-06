# TUPLAS
# Son inmutables, no se puedne modificar
# ahorran memoria en comparación a una lista
dias = ("lunes", "martes", "miercoles")
print(dias)

# Convertir una tupla a lista para modificarla
dias = list(dias)
dias.append("jueves")

# Volver a convertir de lista a TUPLA
dias = tuple(dias)
print(dias)

print(dias[0:2])
for dia in dias:
    print(dia, end= ' - ')