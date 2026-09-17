# realizar un programa muestre segun la opcion +(suma), -(resta), *(Multiplicacion), /(Division)
# de dos numeros ingresados por teclado, nos pedira ingrese el primer numero y luego el segundo 
# ingrese la operacion, el programa debe ser solo si al final de la operacion escribo la palabra salir 
# usar funciones 

operations = { '+' : lambda a,b: a + b,
                '-' : lambda a,b: a - b,
                '*' : lambda a,b: a * b,
                '/' : lambda a,b: a / b}


def calcular(num1 : float, num2 : float, symbol : str)-> float:

    function = operations[symbol]
    operation = function(num1, num2)

    return operation
    
def inicializar():
    continue_loop = True 
    while continue_loop: 

        # pregunta al usuario por los números y el tipo de operacion 
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese le segundo número: '))

        symbol = input('Ingrese el tipo de operación que desea realizar: ')
        if symbol not in operations:
            symbol = input('Símbolo no válido. Ingrese +, -, * o /: ')

        print(calcular(num1, num2, symbol))

        #lógica para parar o conntinuar con la calculadora 
        answer = input('¿Quieres continuar? s/n: ')
        if answer.lower() == 'n':
            continue_loop = False 

if __name__ == '__main__':
    inicializar()