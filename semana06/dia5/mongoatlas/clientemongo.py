from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

cliente = MongoClient(os.getenv('MONGO_URI'))

db_codigo = cliente['db_codigo']

colAlumno = db_codigo['alumno']

# dicNuevoAlumno = {
#     "id":2,
#     "nombre":"carlos paredes",
#     "email":"carlosparedes@gmail.com",
#     "celular":"23322323",
#     "github":"https://www.github.com/cparedes"
# }

# dicNuevoAlumno = {
#     "id":3,
#     "nombre":"pedro castillo",
#     "email":"pedrocastillo@gmail.com",
#     "celular":"987654321",
#     "github":"https://www.github.com/pcastillo"
# }
# nuevoAlumnoId = colAlumno.insert_one(dicNuevoAlumno)
# print("nuevo alumno" + str(nuevoAlumnoId))


for alumno in colAlumno.find():
    print(alumno['nombre'] + ' - ' + alumno['email'] + ' - ' + alumno['celular'])