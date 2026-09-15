# funciones o metodos 
# funcion sin retorno 
def saludar():
    print('Hola como estas')
# invocar metdo o funcion 
saludar() # Hola como estas
# funcion con retorno 
def ver_numero():
    return 10

a = 10 
suma = a + ver_numero() # 10 + 10 = 20
print('La suma es:', suma) # 20

# funcion con parametros
def saludoCustom(saludo):
    print(saludo)
# si se declarn argumentos hay que pasarselos 
saludoCustom('Hello') 

def getdatosCliente(nombre, apellidos, malil, telefono):
    # variable del metodo, solo se puede usar dentro del metodo
    datos_cliente = f'NOmbre: {nombre}, Apellidos: {apellidos}, Email: {malil}, Telefono: {telefono}'
    print(datos_cliente)
# variable global, se puede usar en cualquier parte del codigo
datos_clientes = True

getdatosCliente('Jorge', 'Perez', 'jp@gmail.com', '63364723')

# buena practica 
def calcula_sumatoria(num1 : float, num2 : float) -> float:
    print(num1 + num2)
    suma = num1 + num2
    # sale del bucle el return 
    return suma

calcula_sumatoria(41, 61)

def calcularCuadrado(num : int) -> int:
    return num * num   
# para controlar los errores, o mas a delante para conreolar errores de conexion a base de datos, o errores de conexion a internet, etc
try: 
    print('Respuesta: ',calcularCuadrado('True'))
except Exception as ex:
    print('Deberias de ingresar un numero', ex)

print('Fin de las pruebas')