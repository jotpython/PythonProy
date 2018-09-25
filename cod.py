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

'''def es_primo(numero):
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

print(es_primo(769))'''

# Retorna el maximo comun divisor

"""def mcd(a, b):
    resto = 0

    while (b > 0):
        resto = b

        b = a % b

        a = resto

    return a


# solicitamos los dos números

num1 = int(input("Introduce el primer numero: "))

num2 = int(input("Introduce el segundo numero: "))

print("El máximo común divisor de ", num1, " y ", num2, " es ", mcd(num1, num2))"""


#funcion exponente, dado un numero, devuelve el exponente en base dos mayor para ese numero.
"""def expon(n):
  exp =0
  cal = 0
  while (cal)<=n:
    cal = 2 ** exp
    if(cal<=n):
      exp= exp + 1
    else:
      exp = exp - 1
  return exp

print(expon(65))"""

#ordenar la palabra de atras adelante
"""s = input("Ingresa una palabra: ")
resultado = ""
i = 0
while i<len(s):
  resultado= resultado + s[len(s)-i-1]
  i=i+1
print(resultado)"""

"""s = "Acaso hubo buhos aca"
t = s[2:9]+s[0:1]
print(t)

def mezclador(string_a, string_b):
  new_word = ""
  a = int(len(string_a))# aquí debes escribir el código de tu programa
  b = int(len(string_b))
  if(a<2 or b<2):
    return False
  new_word = string_a[0:2] + string_b[(b-2):(b)]
  return new_word

prueba = mezclador("k","j")
print(prueba)"""

'''def intercalar(string_a, string_b):
  new_word = ""
  a = int(len(string_a))
  i = 0
  while i!=a:
    new_word = new_word + string_a[i] + string_b
    i = i+1

  return new_word'''
#cuantas ocurrencias de 0 y 1 en un String de binarios
'''def ocurrencias(string):
  one = 0
  cero = 0
  aux_result = 0
  a = int(len(string))
  i = 0
  j = 0
  while i!=a:
    if(int(string[i])!=0 and int(string[i])!=1):
      return False
    i+=1
  while j!=a:
    if string[j]=="0":
      cero = cero + 1
      j+=1
    elif string[j]=="1":
      one = one +int(string[j])
      j+=1
  aux_result = one - cero


  return aux_result

prueba = ocurrencias("010000011111111010011")
print(prueba)'''
# esta funcion quita lo que aparezca en el string entrado segun la posicion que desee
'''def remover_enesimo(s, n):
  long_s = int(len(s))
  i=0
  new_phrase = ""
  if(long_s<n):
    return False

  while i!=long_s:
    if(i == n):
      new_phrase = new_phrase + ""
      i = i+1
    elif(i!=n):
      new_phrase = new_phrase + s[i]
      i = i+1


  return new_phrase

rem = remover_enesimo("Programación", 12)
print(rem)'''

#Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.
#Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".
'''def reemplazo(string):
  long = int(len(string))
  aux_string = string.lower()
  new_string = ""
  i = 0
  while i!= long:
    if(string[i] == aux_string[i]):
      new_string = new_string + string[i]
      i = i+1
    elif (string[i]!=aux_string[i]):
      new_string = new_string + "$"
      i=i+1
    else:
      return False
  return new_string

print(reemplazo("KetyJo1rGA"))'''


'''def escribir_archivo(nombre, edad, pais):
  archivo_usuario = open("probando.txt", "w")
  archivo_usuario.write(nombre + "\n" + str(edad) + "\n" + pais + "\n")
  archivo_usuario.close()


escribir_archivo("Jorge",18,"cuba")'''

#lista de lista

'''def ganador(votos):
  mayor = votos[0]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor'''

'''def ganador(votos):
  mayor = votos[0]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor[0]'''

'''def ganador(votos):
  mayor = votos[len(votos)-1]
  for cand in votos:
    if cand[1] >= mayor[1]:
      mayor = cand
  return mayor'''

#devuelve el menor

'''def ganador(votos):
  mayor = votos[0]
  for cand in votos:
    if cand[1] < mayor[1]:
      mayor = cand
  return mayor[0]'''
#recorrer una lista

'''tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
for i in range(3):
  for j in range(3):
    print(tablero[i][j],end=" ")
print("")

for i in range(9):
  print(tablero[i%3][i//3],end=" ")
print("")

for j in range(3):
  for i in range(3):
    print(tablero[j][i],end=" ")
print("")

for j in range(3):
  for i in range(3):
    print(tablero[i][j],end=" ")
print("")

for i in range(3):
  for j in range(3):
    print(tablero[j][i],end=" ")'''

#cuantas veces se repite un valor en la lista

'''mylist = ["pepe",2,2,2,33,3,"pepe",2]
def cuantas(elem, conjunto):
  contador = 0
  for e in conjunto:
    if e == elem:
      contador += 1
  return contador

print(cuantas(2,mylist))
print("")
def cuantas(elem, conjunto):
  contador = 0
  for k in range(len(conjunto)):
    if conjunto[k] == elem:
      contador += 1
  return contador

print(cuantas("pepe",mylist))'''
import math;
my_lista = [2,4,9,7,65,4,5,9]

def  promedio_std(lista):
    aux = len(lista)
    suma = 0

    for i in range(aux):
        suma = suma + lista[i]
    prom = suma/aux
    return prom

def obtenerVarianza(lista):
    n = len(lista)
    promedio = promedio_std(lista)
    varianza = 0
    for dato in lista:
     varianza += math.pow((dato - promedio), 2)
    return varianza / (n - 1)

def obtenerDesviacion(varianza, lista):
    if(varianza == 0):
        varianza = obtenerVarianza(lista)
        return math.sqrt(varianza)
    elif(varianza > 0):
        return math.sqrt(varianza)

varrianza = obtenerVarianza(my_lista)
desv = obtenerDesviacion(varrianza,my_lista)
print(promedio_std(my_lista),desv)