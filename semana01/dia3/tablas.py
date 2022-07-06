
# LINEA PARA IMPORTAR LIBRERÍAS
from tabulate import tabulate

table = [
    ["peter arce", "peter@gmail.com", "132185485"],
    ["peter arce", "peter@gmail.com", "132185485"]
]
columnas = ["nombre", "email", "celular"]
print(tabulate(table, headers=columnas, tablefmt="grid"))