from TP import *
from pytest import *
# Casos de test (pytest) para el trabajo practico 1. 
Lista_Llena = [1,2,3,4]


def test_Length():
  assert Length(Lista_Llena,1) == True
  assert Length(Lista_Llena,5) == False

def test_AgregaPersona():
  Entrada1 = open("test1-1.txt","r")
  Entrada2 = open("test1-2.txt","r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()
  persona1 = eval(Lineas1[0]
  persona2 = eval(Lineas1[1]
  persona3 = eval(Lineas1[2]
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  resultado3 = eval(Lineas2[2])
  assert AgregaPersona(persona1,{persona1[2] : []}) == resultado1
  assert AgregaPersona(persona2,{persona2[2] : []}) == resultado2
  assert AgregaPersona(persona3,{persona3[2] : []}) == resultado3

def test_Filtrado():
  Entrada1 = open("test2-1.txt", "r")
  Entrada2 = open("test2-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()
  persona1 = eval(Lineas1[0]
  candidatos1 = eval(Lineas1[1])
  persona2 = eval(Lineas1[2]
  persona3 = eval(Lineas1[3]
  resultado1 = eval(Lineas2[0])
  resultado2 = eval(Lineas2[1])
  resultado3 = eval(Lineas2[2])
  assert Filtrado(persona1,candidatos1) = resultado1  
  assert Filtrado(pesona2,{}) =  resultado2

def test_MatchingHomosexuals():
  Salida = open("salida-test", "w+")
  Entrada1 = open("test3-1.txt", "r")
  Entrada2 = open("test3-2.txt", "r")
  Lineas1 = Entrada1.readlines()
  Lineas2 = Entrada2.readlines()  
  lista1 = eval(Lineas1[0])
  genero1 = eval(Lineas1[1])
  lista2 = eval(Lineas1[2])
  genero2 = eval(Lineas1[3])
  lista3 = eval(Lineas1[4])
  genero3 = eval(Lineas1[5])
