from CreadorDeParejas import *
from pytest import *
# Casos de test (pytest) para el trabajo practico 1. 

# Testeamos la foncion MayorA, evitamos el uso de archivo por la simpleza de esta funcion
Lista_Llena = [1,2,3,4]
def test_MayorA():
  assert MayorA(Lista_Llena,1) == True
  assert MayorA(Lista_Llena,5) == False

# Testeamos la funcion Agregar
# La entrada Consiste de las personas como una tupla de 6 valores ("Nombre", "Apellido", "Localidad", Edad, "Genero", "GeneroInteres")
# Y de un diccionario de la forma candidatos{Localidad:{'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}}
# La salida para revisar si funciono es un diccionario pero con la persona agregada en la posicion que corresponda sugun su localidad, edad y genero/interes
def test_Agregar():
  Entrada1 = open("test1-1.txt", "r")
  Entrada2 = open("test1-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()
  persona1 = eval(Lineas1[0])
  candidatos1 = eval(Lineas1[1])
  persona2 = eval(Lineas1[2])
  candidatos2 = eval(Lineas1[3])
  persona3 = eval(Lineas1[4])
  candidatos3 = eval(Lineas1[5])
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  resultado3 = eval(Lineas2[2])
  assert Agregar(persona1,candidatos1) == resultado1 # testeo agregar una persona a un diccionario que tiene ciudades pero no personas
  assert Agregar(persona2,candidatos2) == resultado2 # testeo de agregar una persona a un diccionario que todavia no tiene ninguna ciudad ni personas
  assert Agregar(persona3,candidatos3) == resultado3 # testeo agregar una persona a un diccionario que ya teniene ciudades y personas 
 
# Testeamos la funcion MatchingFunction
# La entrada es diccionario de la forma candidatos{Localidad:{'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}} con personas agregadas
# La salida para revisar si funciono es un diccionario de la misma forma, pero ahora sin las personas con las que se podia formar parejas
def test_MatchingFunction():
  Salida = open("salida-test.txt", "w+")
  Entrada1 = open("test2-1.txt", "r")
  Entrada2 = open("test2-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()  
  lista1 = eval(Lineas1[0]) 
  lista2 = eval(Lineas1[1])
  lista3 = eval(Lineas1[2])
  lista4 = eval(Lineas1[3])
  lista5 = eval(Lineas1[4])
  lista6 = eval(Lineas1[5])
  lista7 = eval(Lineas1[6])
  lista8 = eval(Lineas1[7])
  lista9 = eval(Lineas1[8])
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  resultado3 = eval(Lineas2[2])
  resultado4 = eval(Lineas2[3])
  resultado5 = eval(Lineas2[4])
  resultado6 = eval(Lineas2[5])
  resultado7 = eval(Lineas2[6])
  resultado8 = eval(Lineas2[7])
  resultado9 = eval(Lineas2[8])
  assert MatchingFunction(Salida,lista1) == resultado1 #test de 3 hombres homosexuales
  assert MatchingFunction(Salida,lista2) == resultado2 #test de 3 hombres homosexuales y bi
  assert MatchingFunction(Salida,lista3) == resultado3 #test de 3 hombres homosexuales y 2 bi
  assert MatchingFunction(Salida,lista4) == resultado4 #test de 3 hombres homosexuales y  bi , 1 hombre hetero y 1 mujer hetero
  assert MatchingFunction(Salida,lista5) == resultado5 #test de 3 hombres homosexuales y  bi , 1 hombre hetero y 2 mujer hetero
  assert MatchingFunction(Salida,lista6) == resultado6 #test de 3 hombres homosexuales y  2 bi , 2 hombre hetero y 1 mujer hetero
  assert MatchingFunction(Salida,lista7) == resultado7 #test de 3 hombres homosexuales y  2 bi , 2 hombre hetero y 1 mujer hetero pero con edades entre 15 y 17
  assert MatchingFunction(Salida,lista8) == resultado8 #test de 1 hombre hetero y 1 mujer hetero mayores de edad
  assert MatchingFunction(Salida,lista9) == resultado9 #test de 1 hombre homo y 1 hombre hetero mayores de edad de una localidad y un hombre homo y una mujer hetero de otra localidad distinta a las personas antes mensionadas  
