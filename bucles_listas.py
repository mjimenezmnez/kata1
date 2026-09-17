# Contenerdor, lista, array 
# len() <- longitud de una lista 
# lista[1] <- que hay en el puesto numero 2 
# lista[len(lista) - 1] <- valor de la ultima posición de lista 

lista_all = ['María', 10, True, 3.99, [1,2,3]]

print(len(lista_all))  # sera 5 
print(lista_all[0]) # que hay en la primera posicion 
print(lista_all[len(lista_all) - 1]) # que hay en la ultima posicion 

for i in lista_all:
    print(i)

for i in range(0, len(lista_all)):
    print(lista_all[i])

# como acceder al 2 de la lista 
print(lista_all[len(lista_all)- 1][1])
