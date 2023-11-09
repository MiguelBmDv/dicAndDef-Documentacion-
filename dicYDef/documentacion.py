"""
Sentencias, funcionalidades, palabras claves o metodos a destacar:

DICCIONARIO

-Palabra clave o reservada dict = Se utiliza para declarar un diccionario dentro de una variable como en el ejemplo
-Un diccionario se puede hacer de forma mas eficaz dandole nombre seguido de un igual y dos llaves y dentro de ellas se declaran las claves y sus valores.
-Con el metodo de update podemos actualizar un diccionario ya existente con otro nuevo diccionario, agregando asi mas elementos, otros metodos a destacar en los diccionarios es el Get, con el cual podemos obtener el valor de una clave.
-La funcion items() se utiliza para sacar clave y valor
-La funcion keys() se utiliza para sacar solo las claves
-La funcion values() se utiliza para sacar solo los valores
-La funcion del() se utiliza para eliminar un elemento del diccionario
-El .format(Trae el valor de una variable) se ve mucho en los procesos de iteraciones donde el valor cambia.
-El zip se utiliza para juntar dos o mas diccionarios en uno.
-El reversed se utiliza para invertir el orden de los elementos de un diccionario.

ADICIONAL:
-El metodo popitem elimina el ultimo elemento del diccionario
"""

diccionario = dict()
# Diccionario vacío inicializado con llaves

diccionario= {}
# Diccionario inicializado con valores
Diccionario = {'nombre':'Sandra' , 'edad': 44}

calificaciones = {"Juan": 4.5, "Ana": 3.8}
# Actualiza el diccionario calificaciones con dos nuevos elementos
calificaciones.update({"Rosa": 3.7, "German": 4.8})


#Iterar un diccionario:
calificaciones = {'Sandra': 5.0,'Adriana':5.0,'Mauricio':4.5,'Jose':2.5}
for i, j in calificaciones.items():
  print(i,j)

print("Técnicas por clave")
for i in calificaciones.keys():
  print(i)  

print("Iterar por valor")
for j in calificaciones.values():
  print(j)
  
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']
for n, e in zip(nombres, edades):  
  print('Tú nombre es {0} y tu edad {1}.'.format(n, e))

# Crea un diccionario con claves y valores aleatorios
dicaleatorio={x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)

#IMPRIMIR NÚMEROS EN REVERSA
print("Números en reversa")
for i in reversed(range(1, 10, 2)):
  print(i)

#BORRAR UN ELEMENTO DEL DICCIONARIO
del(calificaciones['Rosa'])
for i, j in calificaciones.items():
  print(i,j)

""" 
FUNCIONES

-Las funciones son bloques de código que se pueden llamar en alguna parte del programa principal, esto con el objetivo de repetir muchas veces una estructura de codigo sin tener que reescribir, al declarar una funcion se pueden de dos formas, la clasica con la palabra reservada DEF o de una forma "anonima" con lambda, algo asi como en javascript que se hace una funcion de flecha.
-Despues de declarar una funcion esta puede ser llamada en cualquier parte del programa principal, y para hacerlo debe ir el nombre de la funcion seguida de unos parentesis.
-Dentro de los parentesis en una funcion a la hora de definirla se conoce como parametros, que son usados para el funcionamiento del programa, es informacion que se almacenara y sera de utilidad.
-Dentro de los parentesis en una funcion a la hora de llamarlas se conoce como argumentos, es la informacion que se envia desde el programa principal, estos lo toma la funcion como los valores de los parametros establecidos, para seguir con el curso del programa.
-En las funciones hay dos formas de mostrar valores, con un clasico print o con un return, que hara una funcion similar, solo que el valor que devolvera, se almacenara en el programa principal.
-En las funciones los parametros pueden variar, como viene siendo:
Posicionales: Estos al llamar a una funcion, los argumentos se almacenaran en el orden de posicion de cada parametro.

Nominales: En estos a la hora de llamar, se especifica el parametro seguido de su valor.

Defecto: Estos van de la mano con los posicionales, se puede establecer un valor inicial a un parametro por defecto, y al llamarse se pueden agregar valores en forma de argumentos siguiendo el orden de los parametros.

  ADICIONAL:
  Tambien existen parametros obligatorios y opcionales 

-Luego siguen los parametros mutables, estos tienden a cambiar como la palabra lo dice, en el transcurso del programa se pueden ver cambios.

Dentro de los ejercicios solo se vieron dos palabras a destacar:

Is none (Para determinar si esta vacio o no hay nada)
Lambda (Hace referencia a la realizacion de una funcion sin definirla, esta es anonima y puede recibir muchos paramtetros)
"""

#Definir una función
def saludar():
  print("saludo")

def retornarnumero():
  return 1

#Al llamar a saludar se imprime un saludo, y en el caso de retornarnumero se imprime 1 pero devolviendo un valor a la parte principal (main) del programa

saludar()
retornarnumero()

#como el valor de la funcion es agregada al programa principal, se puede hacer uso de este
if retornarnumero()==1:
  print("devolvió un uno")

else:
  print("No devolvió un uno")


#Funciones con Parámetros
def raiz(value):
  return value ** (1/2)
print(f'La raiz cuadrada es: {raiz(4)}')

def validarsiexiste(obj):
  if obj:
    print(f"{obj} is True")
  else:
    print(f"{obj} is False")

validarsiexiste(1)

#Funciones con Parámetros Posicionales
def compra(marca,cantidad,valor):
  return dict(marca=marca,cantidad=cantidad,valor=valor*cantidad)
print(f' lo comprado fue:{compra("AMD",3,2500000)}')

#Funciones con Parámetros Nominales
def compra2(marca,cantidad,valor):  
  return dict(marca=marca,cantidad=cantidad,valor=valor*cantidad)
print(f' lo comprado fue:{compra2(marca="AMD",cantidad=3,valor=2500000)}')

#Parámetros por defecto
def compra3(marca,cantidad,valor=2500000):
  return dict(marca=marca,cantidad=cantidad,valor=valor*cantidad)
print(f' lo comprado fue:{compra3("AMD",3)}')

#Modificando parámetros mutables
def lista(arg, result=[]):
  result.append(arg)
  print(result)
lista('domingo', [])

#Modificando parámetros mutables
def listalimpia(arg, result=None):
  if result is None:  
    result = []
    result.append(arg)
    print(result)

listalimpia("a")
listalimpia("b")

#Funciones anónimas «lambda»
numero_palabras = lambda t: len(t.strip().split())
print(numero_palabras("hola, esto es una prueba con lambda"))

operadorand = lambda x, y: x & y
for i in range(2):
  for j in range(2):
    print(f"{i} & {j} = {operadorand(i, j)}")
