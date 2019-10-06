import TP as bs

# Casos de test (pytest) para el trabajo practico 1. 
MujerBi = (EIDA, FONSECA, MONTES DE OCA,20,F,A)
MujerHomo = (DAISY, ROJAS, MONTES DE OCA,  44, F, F)
MujerHete = (EIDA, ESPELETA, MONTES DE OCA,  82, F, M)
HombbreBi = (ALFREDO, MIRANDA, MONTES DE OCA,  76, M, A)
HombreHomo = (ALVARO, FONSECA,  MONTES DE OCA,  30, M, M)
HombreHete =(RAMON VICTOR, SALAS, MONTES DE OCA,  82, M, F)
Menor = (GLADYS, RODRIGUEZ, DESAMPARADOS,  10, F, N)
Asexual = (MARIA LUISA, RODRIGUEZ, SANTO DOMINGO,  55, F, N)

Lista_Llena = [MujerBi,MujerHomo,MujerHete,HombbreBi]

Candidatos_Vacios = {}
Candidatos_Lleno = {MONTES DE OCA: [], ROSARIO:[]}

def Length_test():
    assert bs.Length(Lista_Llena,1) = True
    assert bs.Length(Lista_Llena,5) = False

def AgregaPersona_test():
    asser bs.AgregaPersona(MujerBi,Candidatos_Vacios) = {MONTES DE OCA: [MujerBi]}


def Filtrado_test():

def MatchingHomosexuals_test():

def MatchingHeterosexuals_test():

def MatchingBisexuals_test():

def MatchingFunction_test():

