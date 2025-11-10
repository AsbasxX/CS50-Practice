dinero_faltante = 50
MONEDA_ACEPTADA = [5,10,25]
ZERO = 0


while dinero_faltante > ZERO:
    moneda_ingresada = int(input("Insert Coin: "))
    if moneda_ingresada == MONEDA_ACEPTADA[0] or moneda_ingresada == MONEDA_ACEPTADA[1] or moneda_ingresada == MONEDA_ACEPTADA[2]:
        dinero_faltante -= moneda_ingresada
        if dinero_faltante > ZERO:
            print(f"Amount due: {dinero_faltante}")
        else:
            cambio = abs(dinero_faltante)
            print(f"Change Owed: {cambio}")
    else:
        print(f"Amount due: {dinero_faltante}")

