"""numero = int(input("Ingrese numero"))
if numero%2:
  print("Es par")

jurado1 = "P"
jurado2 = "X"
jurado3 = "X"
#if jurado1 == "X" and jurado2 == "X" and jurado3 == "X":
 #   print("ta bien")
A = 2012
if (A%4==0 and A%100 != 0) or (A%100==0 and A%400==0):
  print("Es bisiesto")

numero = int(input("Ingrese calidad del aire"))
if numero>=0 and numero<=99:
  print("Bueno")
elif numero>=100 and numero<=199:
  print("Regular")
elif numero>=200 and numero<=299:
  print("Alerta")
elif numero>=300 and numero<=499:
  print("Preemergencia")
else:
  print("Emergencia")

temp = 32
print("FARH    Cels")
while (temp <=80):
    print(temp,"    ",int((temp-32)*5/9))
    temp = temp+1"""

def es_primo(numero):
  primo = True
  if(numero<2):
    return False
  elif(numero == 2):
    return primo
  else:
    for i in range(2,numero):
      if (numero%i)==0:
        primo = False
  return primo

print(es_primo(2))