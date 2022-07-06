class Persona:
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema

    def mostrar(self):
        print("Nombre: " + self.nombre)
        print("Email: " + self.email)

class Alumno(Persona):
    def __init__(self,nom,ema,nota):
        # Declarar método super() para contener los atributos del padre
        super().__init__(nom,ema)
        self.nota = nota

    def mostrar(self):
        # super(), atributos del método mostrar() del padre
        super().mostrar()
        print("Nota: " + str(self.nota))

class Profesor(Persona):
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp

    def mostrar(self):
        super().mostrar()
        print("Especialidad: " + self.especialidad)

alu1 = Alumno('Carlos Tello','ctello@gmail.com','20')
alu1.mostrar()

prof1 = Profesor('Gustavo Torres','gtorres@gmail.com','historia')
prof1.mostrar()