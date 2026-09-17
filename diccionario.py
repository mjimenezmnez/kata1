personas = { 'nombre' : 'Rosa', 'edad' : 30, 'ciudad' : 'Valencia'}

#se recorreria como lista y se manipularía como dicionario 
lista_personas = [{ 'nombre' : 'Edu', 'edad' : 34, 'ciudad' : 'Alicante'},
                  { 'nombre' : 'Maria', 'edad' : 19, 'ciudad' : 'Valencia'},
                  { 'nombre' : 'Juan', 'edad' : 31, 'ciudad' : 'Santa Pola'}]

print(personas)
print(len(personas))
print(personas['nombre'])# acceso a los valores

# cambiar valor 
personas['nombre'] = 'Jose'
print(personas['nombre'])
# obttener todas las claves 
print(personas.keys())
# obtener todos los valores del dict 
print(personas.values())
# obtener las claves y los valores del dict 
print(personas.items())

# para acceder a el valor por su key con get()
print(personas.get('nombre'))
# eliminar un elemento por su clave 
print(personas.pop('edad'))
# para agregar un elemento nuevo 
print(personas.update({'país' : 'España'}))

for key, value in personas.items():
    print(f'key: {key}, value : {value}')



