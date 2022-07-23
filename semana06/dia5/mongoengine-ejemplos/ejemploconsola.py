from mongoengine import *

connect('db_demo')
# creamos clases basadas en documentos
class Usuario(Document):
    usuario = StringField(required=True)
    password = StringField(required=True)

nuevoUsuario = Usuario()
nuevoUsuario.usuario = 'admin'
nuevoUsuario.password = 'admin'
nuevoUsuario.save()

for usu in Usuario.objects:
    print(usu.usuario)