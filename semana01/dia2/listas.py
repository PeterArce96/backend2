dias = ["lunes", "martes", "miercoles"]
print(dias)
print(dias[1])

# AGREGAR UN ELEMENTO A LA LISTA
dias.append("jueves")
print(dias)

# ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
dias.pop()
print(dias)
# otro modo de borrar
del dias[0] 

# REEMPLAZAR UN ELEMENTO DE LA LISTA
dias[0] = "domingo"
print(dias)

for dia in dias:
    # end --> que va separar los elementos de lista
    print(dia, end=" ")

alumnos = []
totalAlumnos = int(input("Ingrese el total de alumnos a registrar: "))
for contador in range(totalAlumnos):
    nuevoAlumno = input("Nombre del alumno "+str(contador)+ " : ")
    alumnos.append(nuevoAlumno)
print("Relación de alumnos: ")
for alumno in alumnos:
    print(alumno, end= " | ")