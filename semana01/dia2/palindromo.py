"""
Palíndromos:
    Atar a la rata
    radar
    oso
    ana
"""
# Retorno de un string
# palabra = "micasa"
# palabraString = palabra[::]

# Retorno de un string al revés
# palabra = "micasa"
# palabraReves = palabra[::-1]

palabraInicial = input("escribe una palabra: ")
palabraInicial = palabraInicial.replace(' ','')
palabraInicial = palabraInicial.lower()
palabraReversa = palabraInicial[::-1]
if(palabraInicial == palabraReversa):
    print("es un palíndromo")
else:
    print("No es un palíndromo")
