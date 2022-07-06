import os;
import time;
cursos = [
    {'nombre':'matemáticas', 'profesor':'Gustavo Torres'}
    ]

opcion = 0
while(opcion != 5):
    if(opcion != 0):
        time.sleep(2)
        os.system("clear")
    print(
        """
        =======================================
            SISTEMA DE MATRÍCULA DE CURSOS
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
            [1] REGISTRO DE NUEVO CURSO
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """)
        nombre = input("NOMBRE DEL NUEVO CURSO: ")
        profesor = input("PROFESOR: ")
        dictNuevoCurso = {
            'nombre': nombre,
            'profesor' :profesor
        }
        cursos.append(dictNuevoCurso)
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~~
                CURSO REGISTRADO
            ~~~~~~~~~~~~~~~~~~~~~~~~
            """
            )
    elif(opcion == 2):
        print(
        """
        ===========================================================
                        [2]  LISTADO DE CURSO
        -----------------------------------------------------------
                |       NOMBRE        |       PROFESOR   |
        -----------------------------------------------------------
        """)
        for curso in cursos:
            print("       ",end=' ')
            for values in curso.values():
                print("     |    " + values,end='    ')
            print()
        print('        ===========================================================')

        input("presione un tecla para continuar ...")
    elif(opcion == 3):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~
            [3] ACTUALIZAR CURSOS
            ~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
        valorBusqueda = input("Ingrese el nombre del curso a actualizar: ")
        indiceCurso = -1
        for indice in range(len(cursos)):
            curso = cursos[indice]
            for clave,valor in curso.items():
                if(clave == "nombre" and valor == valorBusqueda):
                    indiceCurso = indice
                    break
        if(indiceCurso == -1):
            print("No se encontró el curso")
        else:
            print("curso a editar : " + cursos[indiceCurso].get("nombre"))
            print("NUEVOS VALORES PARA EL CURSO : ")

            nombre = input("NOMBRE ("+ cursos[indiceCurso].get("nombre") +") : ")
            if(nombre == ''):
                nombre = curso[indiceCurso].get("nombre")
            profesor = input("PROFESOR ("+ cursos[indiceCurso].get("profesor") +") : ")
            if(profesor == ''):
                profesor = cursos[indiceCurso].get("profesor")
            
            dictCursoEditar = {
                'nombre':nombre,
                'profesor':profesor
            }
            cursos[indiceCurso] = dictCursoEditar
            print("CURSO ACTUALIZADO!!!")

    elif(opcion == 4):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~
            [4] ELIMINAR CURSO
            ~~~~~~~~~~~~~~~~~~~~~
            """
        )
        valorBusqueda = input("ingrese el nombre del curso a eliminar : ")
        indiceCurso = -1
        for indice in range(len(cursos)):
            curso = cursos[indice]
            for clave,valor in curso.items():
                if(clave == "nombre" and valor == valorBusqueda):
                    indiceCurso = indice
                    break
        if(indiceCurso == -1):
            print("No se encontro el curso")
        else:
            cursos.pop(indiceCurso)
            print("CURSO ELIMINADO !!!")
    elif(opcion == 5):
        print(
            """
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            [5] SALIENDO DEL SISTEMA...
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            """
        )
    else:
        print("""
            ~~~~~~~~~~~~~~~~~~~~~~~
                OPCIÓN INVÁLIDA
            ~~~~~~~~~~~~~~~~~~~~~~~
            """
        )