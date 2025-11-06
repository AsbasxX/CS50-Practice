#Funcion Principal que recibir un valor e imprimir una carita convertida
def main():
    Texto = input()
    print(convertir_carita(Texto))

#Funcion que convierte un texto en una carita
def convertir_carita(Texto):
    Texto = Texto.replace(":)", "🙂")
    Texto = Texto.replace(":(", "🙁")
    return Texto

main()