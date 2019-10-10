from TP import *
from pytest import *
# Casos de test (pytest) para el trabajo practico 1. 
Lista_Llena = [1,2,3,4]


def test_MayorA():
  assert MayorA(Lista_Llena,1) == True
  assert MayorA(Lista_Llena,5) == False



def test_Agregar():
  Entrada1 = open("test1-1.txt", "r")
  Entrada2 = open("test1-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()
  persona1 = eval(Lineas1[0])
  candidatos1 = eval(Lineas1[1])
  persona2 = eval(Lineas1[2])
  persona3 = eval(Lineas1[3])
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  assert Agregar(persona2,{}) ==  resultado2
  assert Agregar(persona1,candidatos1) == resultado1  
 

def test_MatchingFunction():
  Salida = open("salida-test", "w+")
  Entrada1 = open("test2-1.txt", "r")
  Entrada2 = open("test2-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()  
  lista1 = eval(Lineas1[0])
  lista2 = eval(Lineas1[1])
  lista3 = eval(Lineas1[2])
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  resultado3 = eval(Lineas2[2])
  assert MatchingFunction(Salida,lista1) == resultado1 #test de 3 hombres homosexuales
  assert MatchingFunction(Salida,lista2) == resultado2 #test de 3 hombres homosexuales y bi
  assert MatchingFunction(Salida,lista3) == resultado3 #test de 3 hombres homosecuales y 2 bi
  