LETRAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
PUNTOS = ["-", ".", "/", "\\", "|", "!", "?", ";", ":", "@", "$", "%", "^", "&", "*", "(", ")", "[", "]", "{", "}", "<", ">", "\"", "'", "+", "=", "_", " "]
NUMEROS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
TAMAÑO_PLACA_PERMITIDO = [4, 5, 6]

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plates):
    for char in plates:
        if char in PUNTOS:
            return False
    if len(plates) in TAMAÑO_PLACA_PERMITIDO:
        if plates[0] not in LETRAS or plates[1] not in LETRAS: 
            return False
        else:
            char = range(int(NUMEROS[2]), len(plates))
            char = char[0]
            while char < len(plates):
                if char < len(plates) - 1:
                    if plates[char] in NUMEROS[0] and plates[char + 1] in NUMEROS:
                        return False
                    elif plates[char] in NUMEROS and plates[char + 1] in LETRAS:
                        return False 
                char += 1
            return True
    else:
        return False
        
   
main()