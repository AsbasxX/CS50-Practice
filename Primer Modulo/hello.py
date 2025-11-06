"""
# Hermanoooooooooo se comenta con el numeral
name = input("¿Cual es tu nombre?\n")#Se puede unir con strip and title

#Quitar Espacion Blanco Innecesarios, no se puede eliminar el espacio de en medio, solo Izq y Der
name = name.strip()


Poner primer letra en Mayuscula, funciona para parrafos
name = name.capitalize()


#Poner Nombre en Mayusculas
name = name.title()


Separar Nombre y Apellido
Primero, Segundo = name.split(" ")


#Imprimir Saludo
print(f"Hola, {name}!")
"""
"""
def greet_user():
    name = input("¿Cual es tu nombre?\n")
    name = name.strip()
    name = name.title()
    print(f"Hola, {name}!")
greet_user()
"""
"""
def hello(to="World"):
    print(f"Hello, {to}!")code

hello()
name = input("¿Cual es tu nombre?\n")
hello(name)
"""


def main():
    name = input("¿Cual es tu nombre?\n")
    hello(name)

def hello(to="World"):
    print(f"Hello, {to}!")
main()