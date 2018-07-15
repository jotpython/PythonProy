from builtins import print

print("Bienvenido a ... ")
print("""                                                        
(       )|\     /|(  ____ )(  ____ \(  __  \ 
| () () |( \   / )| (    )|| (    \/| (  \  )
| || || | \ (_) / | (____)|| (__    | |   ) |
| |(_)| |  \   /  |     __)|  __)   | |   | |
| |   | |   ) (   | (\ (   | (      | |   ) |
| )   ( |   | |   | ) \ \__| (____/\| (__/  )
|/     \|   \_/   |/   \__/(_______/(______/                                                             
""")

print("Solo para conocernos un poco mejor")
print("Entre los datos que necesitamos a continuacion")
nombre = input("Escriba su nombre")
fn = input("Anno de Nacimiento")

def cal_edad(a):
    edad = 2018 - int(a)
    print(edad)

cal_edad(fn)

print("Entre la informacion siguiente")
print("Entre la informacion si es casado")
casado = input("Es casado")
#este es un if de prueba con elif and if
"""Comentario en python"""
if (casado == "si"):
    print("tienes mucha suerte")

elif (casado == "no"):
    print("Deberias casarte")

elif (casado == ""):\
    print("Deberias decir algo al respecto")

