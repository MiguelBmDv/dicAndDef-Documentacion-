#Ejercicios establecidos en la guia:


#Escriba una función en Python que reproduzca lo siguiente:𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2      Valor para X=3 y valor para Y=5

def miLindaFuncion(x,y):
  print(f'Tu operacion de x y es: {x**2 + y**2}')

miLindaFuncion(3,5)

#Ejercicio: Tome el presente ejercicio, y pase a la funcion la lista con los dias de la semana restantes
def lista(arg, result=[]):
  result.append(arg)
  print(result)
lista('domingo',['lunes','martes','miercoles','jueves','viernes','sabado'])

#El problema de seguir el ejercicio establecido es que si se envian los demas dias de la semana por argumentos, entonces no se ejecuta la funcion correctamente y solo se guarda el ultimo dia de la semana ingresado en la lista ya que se ejecuta de forma individual, por eso una forma de realizar este ejercicio seria enviando un argumento que era domingo, y en resultado una lista como argumento, para al momento de unir sea solo una lista.

#Modificando el codigo se puede llegar a algo mejor.
result2 = []
def lista(arg):
  result2.insert(-1,'domingo')
  result2.insert(0,arg)
  for i in result2[0]:
    print(i)
  print(result2[-1])

lista(['lunes','martes','miercoles','jueves','viernes','sabado'])