# CREAR UNA CLASE
class Automovil:
    # CREAR ATRIBUTOS
    def __init__(self,aa,pl,col,mar):
        self.año = aa
        self.placa = pl
        self.color = col
        self.marca = mar

    # CREAR MÉTODOS
    def encender(self):
        print('encender ' + self.marca)

    def avanzar(self):
        print('avanzar ' + self.marca)

    def acelerar(self):
        print('acelerar ' + self.marca)

    def frenar(self):
        print('frenar ' + self.marca)

# Creación de objetos
vw = Automovil(1970,'CH-1234','amarillo','Volkswagen')
print("Se creó el objeto vw con los siguientes datos : ")
print(" año: "+ str(vw.año))
print(" color: "+ vw.color)
print(" placa: "+ vw.placa)
print(" marca: "+ vw.marca)

tico = Automovil(1985,'EJ-2345','rojo','Tico')
print("Se creó el objeto tico con los siguientes datos : ")
print(" año: "+ str(tico.año))
print(" color: "+ tico.color)
print(" placa: "+ tico.placa)
print(" marca: "+ tico.marca)

lamborghini = Automovil(2018,'E7P-367','amarillo','Lamborghini')
print("Se creó el objeto lamborghini con los siguientes datos : ")
print(" año: "+ str(lamborghini.año))
print(" color: "+ lamborghini.color)
print(" placa: "+ lamborghini.placa)
print(" marca: "+ lamborghini.marca)

# ACTIVAR MÉTODO
vw.encender()