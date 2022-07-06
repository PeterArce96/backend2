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
import os;
import time;
alumnos = [
    {'nombre':'peter', 'email':'parce0496@gmail.com', 'celular':'987654321'}
    ]

opcion = 0
while(opcion != 5):
    if(opcion != 0):
        time.sleep(2)
        os.system("clear")
    print(
        """
        =======================================
            SISTEMA DE MATRÍCULA DE ALUMNOS
        =======================================
        [1] Registrar
        [2] Mostrar
        [3] Actualizar
        [4] Eliminar
        [5] Salir
        """
    )
    opcion = int(input("Ingrese la opción a ejecutar: "))
    os.system("clear")
    if(opcion == 1):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            [1] REGISTRO DE NUEVO ALUMNO
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
        nombre = input("NOMBRE : ")
        email = input("EMAIL: ")
        celular = input("CELULAR: ")
        dictNuevoAlumno = {
            'nombre': nombre,
            'email' :email,
            'celular':celular
        }
        alumnos.append(dictNuevoAlumno)
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~~
                ALUMNO REGISTRADO
            ~~~~~~~~~~~~~~~~~~~~~~~~
            """
            )
    elif(opcion == 2):
        print(
        """
        ===========================================================
                        [2]  LISTADO DE ALUMNOS
        -----------------------------------------------------------
        |       NOMBRE        |       EMAIL   |       CELULAR     |
        -----------------------------------------------------------
        """)
        for alumno in alumnos:
            print("       ",end=' ')
            for values in alumno.values():
                print("|    " + values,end='    ')
            print()
        print('        ===========================================================')

        input("presione un tecla para continuar ...")
    elif(opcion == 3):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~
            [3] ACTUALIZAR ALUMNOS
            ~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
        valorBusqueda = input("Ingrese el email del alumno a actualizar: ")
        indiceAlumno = -1
        for indice in range(len(alumnos)):
            alumno = alumnos[indice]
            for clave,valor in alumno.items():
                if(clave == "email" and valor == valorBusqueda):
                    indiceAlumno = indice
                    break
        if(indiceAlumno == -1):
            print("No se encontró el alumno")
        else:
            print("alumno a editar : " + alumnos[indiceAlumno].get("nombre"))
            print("NUEVOS VALORES PARA EL ALUMNO : ")

            nombre = input("NOMBRE ("+ alumnos[indiceAlumno].get("nombre") +") : ")
            if(nombre == ''):
                nombre = alumnos[indiceAlumno].get("nombre")
            email = input("EMAIL ("+ alumnos[indiceAlumno].get("email") +") : ")
            if(email == ''):
                email = alumnos[indiceAlumno].get("email")
            celular = input("CELULAR ("+ alumnos[indiceAlumno].get("celular") +") : ")
            if(celular == ''):
                celular = alumnos[indiceAlumno].get("celular")
            dictAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            alumnos[indiceAlumno] = dictAlumnoEditar
            print("ALUMNO ACTUALIZADO!!!")

    elif(opcion == 4):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~
            [4] ELIMINAR ALUMNOS
            ~~~~~~~~~~~~~~~~~~~~~
            """
        )
        valorBusqueda = input("ingrese el email del alumno a eliminar : ")
        indiceAlumno = -1
        for indice in range(len(alumnos)):
            alumno = alumnos[indice]
            for clave,valor in alumno.items():
                if(clave == "email" and valor == valorBusqueda):
                    indiceAlumno = indice
                    break
        if(indiceAlumno == -1):
            print("No se encontro el alumno")
        else:
            alumnos.pop(indiceAlumno)
            print("ALUMNO ELIMINADO !!!")
    elif(opcion == 5):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~~~
            [5] SALIENDO DEL SISTEMA
            ~~~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
    else:
        print("""
            ~~~~~~~~~~~~~~~~~~~~~~~
                OPCIÓN INVÁLIDA
            ~~~~~~~~~~~~~~~~~~~~~~~
            """
        )