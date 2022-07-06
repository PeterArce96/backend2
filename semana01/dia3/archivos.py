# w (write)--> escribir o borrar todo el archivo y lo vuelve a sobreescribir
# a (append)--> agrega al archivo, no lo sobreescribe
f = open('alumnos.txt', 'w')
f.write('peter arce, parce0496@gmail.com, 987654321')

print("archivo creado con exito!!!")
f.write('\nana lopez, ana@gmail.com, 123456789')
f.write('\njorge perez, jperez@gmail.com, 555555555')
f.close()
fr = open('alumnos.txt', 'r')
dataAlumnos = fr.read()
print(dataAlumnos)
fr.close()

# con a creamos otro alumno
fa = open ('alumnos.txt', 'a')
nombre = input("nombre : ")
email = input("email : ")
celular = input("celular : ")
fa.write("\n" + nombre + "," + email + "," + celular)
print("se registró el nuevo alumno")
