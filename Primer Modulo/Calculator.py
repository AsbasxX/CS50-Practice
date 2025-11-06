import os

os.system('cls' if os.name == 'nt' else 'clear')
"""
#Tener cuidado con la concatenación de cadenas en lugar de la suma de números
# Convertir las entradas a enteros antes de sumarlas
print("Suma de dos números")


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))


x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

# Redondear el resultado a un número entero
#z = round(x + y)
z = round(x / y, 2)


Mostrar el resultado con separadores de miles
print(f"The sum is: {z:,}")

Mostrar un numero redondeado con print
print(f"The result is: {z:.2f}")

print(f"{z:,}")
"""

def main():
    x = int(input("What's x? "))
    print(f"x squared is", square(x))

#Puedo usar Pow para elevar a una potencia
def square(n):
    return n * n

main()