#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
import time
from time import sleep


#programa que recibe le nombre y extension de un archivo y devuelve su tipo MIME

Archivo = input("Ingrese el nombre del archivo con su extension: ")
extension = Archivo.split(".")[-1].lower()


if extension == "gif":
    print("image/gif")
elif extension == "jpg" or extension == "jpeg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
