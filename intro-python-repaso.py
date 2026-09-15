#comentarios en una sola línea 
"""
Comentarios en varios de 
varias líneas 
"""
'''
Con comilla simple 
otro tipo de comantar en varias líneas 
'''

# salida de informacion 
print('Salida de información')

# entrada de información 
nombre = input('Ingrese su nombre: ')  
# es una funcion propia de python, captura el dato ibgresado por terminal y siempre lo devuelve como str 
print("Su nombre es", nombre) # le vale con una ',' con un + o con un format 

# tipos de variable en python 
# str : 'kahdfjerje19832984' <- con comillas simples o dobles 
# int : 1000 <- numero entero 
# float: 1.00 <- numero decimal 
# bool: True o False <- valores booleanos

# ver el tipo de una variable 
variable = 'lkjadsflj'
print(type(variable)) # <class 'str'>
# con el uso de type() 

# variables sensbibilidad de mayusculas y minusculas
variable1 = 'JUAN'
vaRIABLE1 = ' Paco'
Variable1 = 'Andres'
print(variable1, vaRIABLE1, Variable1) # JUAN  Paco Andres <- cada uno lo interpreta como una variable diferente

# Null uso del None, no sabes que va a ser la variable
variable = None

def nombrar():
    pass # <- este para las funciones 

# Las variables de python son flexibles, pueden ser de cualquier tipo, es debilmente tipado 
nombre = True
print(nombre) # True
nombre = 100 
print(nombre) # 100

# Reglas de nombres de variables 
#nombres de variables y funciones van en minuscula 
variable = 10 # variable que puede cambiar su valor
CONSTANTE = 10 # variable que no puede cambiar su valor, por convención se escribe en mayúsculas
# nombres de clase van con la primera letra en mayúscula
class People:
    pass


# NO SE PUEDE HACER EN PYHTON (DECLARACIONES DE VARIABLES)
#No se puede NUMERO antes de una letra de nombre de variable 
    #10valor = 'Ana'
# Espacios en el nombre de la variable
    #mi variable = 'Ana'

# SE PUEDE 
# str y int 
valor10 = 'Ana'
# snake case o camel case
valor_10 = 'Ana' # snake case
valordDiez = 'Ana' # camel case

# Conflicto de tipos
numero1 = 100 
numero2 = '50'
suma = numero1 + numero2 # <- esto no se puede hacer, no se puede sumar un str con un int
# se puede convertir con un metodo, casting o casteo 
suma = numero1 + int(numero2) # <- esto si se puede hacer, se convierte el str a int con int()
# esto se puede convertir los tipos de todas las variables 
# str(valor), bool(aqui el valor), float(valor)







