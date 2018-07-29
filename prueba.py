from builtins import print

print("Bienvenido a ... ")
print("""                                                        
                                                        
.    .      .--.               .-.                    . 
|\  /|      |   )             (   )           o       | 
| \/ |.  .  |--'.--..-. .  .   `-.  .-.  .-.  .  .-.  | 
|    ||  |  |   |  (   )|  |  (   )(   )(     | (   ) | 
'    '`--|  '   '   `-' `--|   `-'  `-'  `-'-' `-`-'`-`-
         ;                 ;                            
      `-'               `-'                             

""")
"""dispp = 25
distancia = 23
tiempo = 10
a = distancia/(tiempo/3600)
b = (distancia*1000)/tiempo
resultado = "La velocidad es " + str(a) + " Km/h o " + str(b) + " m/s"
print(resultado)"""
def prueba(n):
    a = sorted(str(n))
    long = len(a)
    cont = 0
    b = []
    long_b = len(b)
    aux = 0
    aux_primo = int(n%1000)

    for i in range(long-1):
        if (a[i]=='0' and aux!=1):
            b.append(str(a[0]))
            aux = 1
        elif a[i] == a[i+1]:
            #b.append(str(a[i+1]))
            cont = cont + 1
        else:
            b.append(str(a[i+1]))
            long_b = len(b)
    if long_b<10:
        return False
    for j in range(10):
        if b[j] != str(j):
            return False

    if (aux_primo < 2):
        return False
    elif (aux_primo == 2):
        return True
    else:
        for i in range(2, aux_primo):
            if (aux_primo % i) == 0:
                return False
    return True


print(prueba(81244657003947))