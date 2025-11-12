import os
import sys
import time

def main():
    seleccion_menu()


def seleccion_menu():
    limpiar_terminal()
    print("Bienvenido la MiniCalculadora\n")    
    print("1. Suma\n2. Resta\n3. Multiplicar\n4. Dividir\n5. Salir\n")
    try:
        operador = int(input("Escriba el numero de la opcion: "))
        match operador:
            case 1:
                limpiar_terminal()
                suma()
            case 2:
                limpiar_terminal()
                resta()
            case 3:
                limpiar_terminal()
                multiplicar()
            case 4:
                limpiar_terminal()
                dividir()
            case 5:
                salir()
            case _:
                limpiar_terminal()
                print("Opcion invalida, ingrese una operación válida\n")
                time.sleep(1)
                seleccion_menu()
    except ValueError: 
        limpiar_terminal()
        print("Opcion invalida, ingrese una operación válida\n")
        time.sleep(1)
        seleccion_menu()

def suma():
    limpiar_terminal()
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"\nEl resultado de la suma es: {num1 + num2}\n")
        repetir_operacion(suma)
    except ValueError:
        limpiar_terminal()
        print("El número ingresado no es válido, ingrese un número válido")
        time.sleep(1)
        suma()
    reiniciar()



def resta():
    limpiar_terminal()
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"\nEl resultado de la suma es: {num1 - num2}\n")
        repetir_operacion(resta)
    except ValueError:
        limpiar_terminal()
        print("El número ingresado no es válido, ingrese un número válido")
        time.sleep(1)
        resta()


def multiplicar():
    limpiar_terminal()
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"\nEl resultado de la suma es: {num1 * num2}\n")
        repetir_operacion(multiplicar)
    except ValueError:
        limpiar_terminal()
        print("El número ingresado no es válido, ingrese un número válido")
        time.sleep(1)
        multiplicar()


def dividir():
    limpiar_terminal()
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 == 0:
            limpiar_terminal()
            print("El segundo número no puede ser 0")
            time.sleep(1)
            dividir()
        else:
            print(f"\nEl resultado de la suma es: {num1 / num2}\n")
            repetir_operacion(dividir)
    except ValueError:
        limpiar_terminal()
        print("El número ingresado no es válido, ingrese un número válido")
        time.sleep(1)
        dividir()


def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def salir():
    limpiar_terminal()
    sys.exit("Gracias por usar la MiniCalculadora\n")


def reiniciar():
    limpiar_terminal()
    s = input("Desea regresar al menu principal? (s/n): ").lower()
    if s == "s":
        seleccion_menu()
    elif s == "n":
        salir()
    else:
        limpiar_terminal()
        print("Opcion invalida, ingrese una opcion válida")
        time.sleep(1)
        reiniciar()


def repetir_operacion(funcion_llamadora):
    entrada = input("Desea operar otra vez? (s/n): ").lower()
    if entrada == "s":
        return funcion_llamadora()
    elif entrada == "n":
        reiniciar()
    else:
        limpiar_terminal()
        print("Opcion invalida, ingrese una opcion válida\n")
        time.sleep(1)
        repetir_operacion(funcion_llamadora)


main()