import time

Mensaje = input("Introduce una oración: ")
print("Oye, oye, más despacio, que no te entiendo. A ver...")
print("¿Como Resuelvo esto...?")
time.sleep(1)
print("Creo que ya lo sé, veamos si funciona...")
time.sleep(1)
MensajeLento = Mensaje.replace(" ", "...")
print(MensajeLento)
time.sleep(2)
print("¡Listo! Ahora sí lo entendí todo.")