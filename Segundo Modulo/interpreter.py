#al recibir una cadena del usuario del tipo: "1+1" o "1 + 1" devolver la operacion correspondiente en float
def main(): 
    Expresion = input("Expression: ").strip()

    x, y, z = Expresion.split(" ")

    x = float(x)
    z = float(z)

    EvaluarOperacion(x, y, z)


def EvaluarOperacion(Operando1, Operador, Operando2):
    match Operador:
        case "+":
            print(float(Operando1 + Operando2))
        case "-":
            print(float(Operando1 - Operando2))
        case "*":
            print(float(Operando1 * Operando2))
        case "/":
            if Operando2 != 0:
                print(float(Operando1 / Operando2))
            else:
                Expresion = "Error: Division by zero"
        case _:
            Expresion = "Error: Unknown operator"

main()
    





