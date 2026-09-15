a = 10 
b = 5 

# condicionales 
print(a > b) # True
print(a < b) # False
print(a!= b) # True
print(a == b) # False

# condicional con if 
# es una estructura que ingresa al bloque de codigo si la condicion es verdadera
if a > b:
    print("'a' es mayor que 'b'") # 'a' es mayor que 'b'
# sino el else ingresa si no es verdadera la primera condicion if 
if  a < b:
    print("'a' es mayor que 'b'") 
else:
    print("'a' es menor o igual 'b'")

dia = 'viernes'

if dia == 'Martes':
    print('Es martes')
# uso de varias condiciones con elif
elif dia == 'Miercoles':
    print('Es miercoles')
elif dia == 'Jueves':
    print('Es jueves')
# devuelve algo si no cumple ninguna de las condiciones anteriores
else:
    print('no se sabe que día')

usuario = None
password = None

usuario = input('Ingrese su usuario: ')
password = input('Ingrese su password: ')

# rolando@gmai.com y roando1234 credenciales correctas 
# uso de operadores booleanos (and, or, not)
if usuario == 'rolando@gmail.com' and password == 'roando1234':
    print('Bienvenido al sistema')
else:
    print('Credenciales no validas')

# las funciones 
