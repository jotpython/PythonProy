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
distancia = 23
tiempo = 10
a = distancia/(tiempo/3600)
b = (distancia*1000)/tiempo
resultado = "La velocidad es " + str(a) + " Km/h o " + str(b) + " m/s"
print(resultado)