"""
Aplicación CRUD
C - CREATE
R - READ
U - UPDATE
D - DELETE
"""
# Para este caso usaremos Alumnos
"""
[
    {'nombre':'', 'email':'', 'celular':''},
    {'nombre':'', 'email':'', 'celular':''}
]
"""
import os
import time
from tabulate import tabulate
from libCrud import *

def crudAlumnos():
    
    if(os.path.isfile('alumnos.csv')):
        f = open('alumnos.csv','r')
        strAlumnos = f.read()
        alumnos = cargarAlumnos(strAlumnos)
        f.close()

    opcion = "0"
    while(opcion != "5"):
        if(opcion != "0"):
            time.sleep(1)
            os.system("clear")
        menu()
        opcion = input("INGRESE LA OPCIÓN A EJECUTAR : ")
        os.system("clear")
        if(opcion == "1"):
            print(
            """
            ============================
            [1] REGISTRO DE NUEVO ALUMNO
            ============================
            """)
            insertarAlumno(alumnos)
            print(
            """
            ================================
                ALUMNO REGISTRADO !!!
            ================================
            """)
        elif(opcion == "2"):
            columnas = ["nombre","email","celular"]
            tablaAlumnos = [alumno.values() for alumno in alumnos]
            print(tabulate(tablaAlumnos,headers=columnas,tablefmt="grid"))

            input("presione Enter para continuar ...")
            
        elif(opcion == "3"):
            print(
            """
            ========================
            [3]  ACTUALIZAR UN ALUMNO
            ========================
            """)
            valorBusqueda = input("ingrese el email del alumno a actualizar : ")
            
            indiceAlumno = buscarAlumno(valorBusqueda,alumnos)
            
            if(indiceAlumno == -1):
                print("No se encontro el alumno")
            else:
                actualizarAlumno(indiceAlumno,alumnos)
                print("ALUMNO ACTUALIZADO!!!")
        elif(opcion == "4"):
            print(
            """
            ========================
            [4]  ELIMINAR ALUMNO
            ========================
            """)
            valorBusqueda = input("ingrese el email del alumno a eliminar : ")
            
            indiceAlumno = buscarAlumno(valorBusqueda,alumnos)

            if(indiceAlumno == -1):
                print("No se encontro el alumno")
            else:
                alumnos.pop(indiceAlumno)
                print("ALUMNO ELIMINADO !!!")
        elif(opcion == "5"):
            print(
            """
            ===========================
            EL SISTEMA SE ESTA CERRANDO
            ===========================
            """)
            strAlumnos = grabarAlumnos(alumnos)
            fw = open('alumnos.csv','w')
            fw.write(strAlumnos)
            fw.close()
        else:
            print(
            """
            ===========================
                OPCIÓN INCORRECTA!!!
            ===========================
            """)

# Código para saber que es lo que se va ejecutar
if __name__ == "__main__":
    crudAlumnos()