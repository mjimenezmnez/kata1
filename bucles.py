# while : se repite el bloque de codigo mientras la condicion sea verdadera True 
"""
seguir = True
while seguir:
    print("esto es un While")

    fin = input("Deseas seguir con este while?: s/n")
    if fin == 'n':
        seguir = False
        #break # rompe el bucle y sale del while
        print ('Esto se acabo')
"""


# while con else 
# si no se cumple la condicion del while, entra al else siempre 
nombre = "Juana"
while nombre == "Maria":
    print("Hola", nombre)
else:
    print("No es Maria, es", nombre)

x = 0 
while x <= 3:
    print(x)
    x += 1
 # otra forma 
 
while x < 3:
    x += 1
    print(x)


# for : se repite mientras se cumple el numero de interaciones definidas
# dentro del propio for variable range(inicio, final(el numero ddo menos uno), salto), enumerate(), len()

for interacion in range(1,21):
    print(interacion)
    
