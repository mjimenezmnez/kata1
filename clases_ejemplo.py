class Persona:
     def __init__(self, dni, direccion, nacionalidad):
          pass
          self.dni = dni 
          self.direccion = direccion
          self.nacionalidad = nacionalidad         

     def datos_persona(self):
          print(f'dni: {self.dni}, direccion: {self.direccion}, nacionalidad: {self.nacionalidad}')

class Profesor(Persona):
     pass


# molde 
class Heroe(Persona): # Heroe esta heredando todos los atributos y métodos de la clsae Persona, Persona es la clase  padre de Heroe o Heroe es la clase hija
     # de persona 
    
     # atributos - avariables 
     nombre = None
     poder = None
     apodo = None
     # metodo contructor son epeciales, se ejecuta automaticamente cuando la clase es invocada 
     def __init__(self, name, power, nickname, dni, direccion, nacionalidad):
          super().__init__(dni, direccion, nacionalidad)# asi hereda lo de persona 
          
          self.nombre = name
          self.poder = power
          self.apodo = nickname
          self.edad = None
          self.ataque_principal(f'{self.nombre} {self.poder}')

     # metodos de la clase 
     # tienen que tener una variable de pertenencia que suele ser self 
     def ataque_principal(self,nombre : str):
          print(f'ataque principal: {nombre}')

     def datos_heroe(self):
          print(f'Nombre: {self.nombre}, Poder: {self.poder}, Apodo: {self.apodo}, Edad: {self.edad},dni: {self.dni}, direccion: {self.direccion}, nacionalidad: {self.nacionalidad}')

     def setEdad(self, edad : int):
          self.edad = edad 

     def getEdad(self, edad : int):
          return self.edad

# invovacion de clase
# spiderman es un objeto de la calse Heroe, es una instancia de la clase Heroe 
spiderman = Heroe('Peter Parker', 'Superfuerza', 'Hombre araña', '03400004L', 'Calle Desengaño 21', 'UK') # se invova un objeto de la clase
# como invocar los atrbutos de spiderman 
#spiderman.nombre = 'Peter Parker'
#spiderman.poder = 'Super fuerza'
#spiderman.apodo = 'Hombre araña'
spiderman.setEdad(20)
spiderman.datos_heroe()
spiderman.datos_persona()

#print(spiderman.nombre)
#print(spiderman.poder)
#print(spiderman.apodo)
#spiderman.ataque_principal('telaraña')

ironman = Heroe('Tony Stark', 'Millionario', 'Hombre de acero', '09423098239', 'Pool Street', 'Estadounidesnse' )
ironman.setEdad(45)
ironman.datos_heroe()
ironman.datos_persona()
