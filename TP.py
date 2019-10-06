#Trabajo Practico N1, 
#Integrantes del grupo: Lautaro Cerruti y Alesandro Regolo
#En el tp, se recibira una lita de personas con datos personales tales como su nombre, aprellido, edad, localidad, etc
#y se fomrara parejas de 2 persoanas en base a su ubicacion, su edad y su preferencia sexual.
#La entrada del programa sera un archivo en el cual se almacenara dicha informacion a utilizar.

#La forma a representar a las personas  con su respectiva inforacion en este practico sera de la siguiente forma
#Persona(Nombre,Apellido,Localidad,Edad,Sexo,GeneroInteres)
#Persona(str,str,str,int,str,str)

#A su vez representamos a los candidatos como un diccionario, en el cual las keys son la ubicacion en la que se encuantran las personas
#y el valor dentro del campo es un diccionario en el cual guardaremos otro diccionario con 3 keys las cuales representaran los distintos gurpos de personas
#ordenados segun la edad que tienen. Para luedo dentro de ellas almacenar otro diccionario con 6 keys en las que se agrupan a las personas 
# segun su sexo y su interes.
#candidatos{Localidad:{'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}}

#El resultado de este programa sera 2 archivos de salida que contendran, por un lado las parejas formadas y por otro lado las personas
#que no pudieron formar pareja, especificando el motivo.

 #Dada una lista y una cantida, verifica si la lista posee mas elementos que la cantidad dada
 #Length: List, Int, Int -> Bool
def Length(lista,cant,contador = 0):
    if(contador > cant ):
        return True
    elif(lista == []) :
        return False
    else :
        return Length (lista[1:],cant, contador +1)


#Dada una lista de personas, guarda en un archivo las personas que no pueden formar una pareja y
#el porque.
def ImprimeSingles(NoParejas):
    ArchivoSalidaSolteros = input("Ingrese nombre del archivo que contendra a los solteros :")
    SalidaSingles = open(ArchivoSalidaSolteros, "w+")
    for p in NoParejas:
        string = p[0] + ", " + p[1] + ", " + str(p[3]) + ", " + p[2] + ", NO TIENE PAREJA POR "
        if p[3] <= 10:
            SalidaSingles.write(string  + "SER MENOR DE 11 AÑOS" + "\n")
        elif p[5] == "N":
            SalidaSingles.write(string + "NO TENER INTERES" + "\n")
        else:
            SalidaSingles.write(string + "NO DISPONIBILIDAD DE PERSONAS" + "\n")
    SalidaSingles.close()

#Dada una Persona y un diccionario que continen a las personas que vivien es dicha localidad
#agrego a dicha persona a la lista que corresponde segun su edad y orientacion sexual
#AgregaPersona: Tupla(str,str,str,int,str,str)-> Dict()
def AgregaPersona(Persona, DictLocalidad):
    if Persona[3] >= 18:
        DictLocalidad['18+'][Persona[4] + Persona[5]].append(Persona)
    elif Persona[3] >= 15:
        DictLocalidad['15a17'][Persona[4] + Persona[5]].append(Persona)
    else:
        DictLocalidad['11a14'][Persona[4] + Persona[5]].append(Persona)
    return DictLocalidad
#Dada una persona y un diccionario que contiene a todos los candidatos a formar parejas
#Agrega la persona al campo del diccionario  de la localidad a la que pertenece y de ser necesario 
#Agrega otra key al diccionario y agrega la persona al campo.
#  Filtrado: Tupla(str,str,str,int,str,str)-> Dict()
def Filtrado(Persona, Candidatos):
    if  Persona[2] in Candidatos.keys() :
        Candidatos[Persona[2]] = AgregaPersona(Persona, Candidatos[Persona[2]])
    else :
        Candidatos[Persona[2]] = {'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}
        Candidatos[Persona[2]] = AgregaPersona(Persona, Candidatos[Persona[2]])
    return Candidatos
#Dado un archivo, una lista con personas y un genero, imprime en el archivo dado las parejas que se formaron
#En este caso todas las parejas van a ser del mismo sexo
#MatchingHomosexuals: file Arrary str -> Array
def MatchingHomosexuals(Salida, listPersonas, generoPersonas):
    while Length(listPersonas[generoPersonas + generoPersonas],1) :
        Persona1 = listPersonas[generoPersonas + generoPersonas][0]
        Persona2 = listPersonas[generoPersonas + generoPersonas][1]
        listPersonas[generoPersonas + generoPersonas].pop(0)
        listPersonas[generoPersonas + generoPersonas].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    if len(listPersonas[generoPersonas + generoPersonas]) == 1 and Length(listPersonas[generoPersonas + 'A'],0):
        Persona1 = listPersonas[generoPersonas + generoPersonas][0]
        listPersonas[generoPersonas + generoPersonas].pop(0)
        Persona2 = listPersonas[generoPersonas + 'A'][0]
        listPersonas[generoPersonas + 'A'].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    return listPersonas
#Dado un archivo, una lista con personas, imprime en el archivo dado las parejas que se formaron
#En este caso todas las parejas van a ser parejas heterosexuales
#MatchingHeterosexuals:  file Arrary  -> Array
def MatchingHeterosexuals(Salida, listPersonas):
    while Length(listPersonas['MF'], 0)  and Length(listPersonas['FM'],0):
        Persona1 = listPersonas['MF'][0]
        Persona2 = listPersonas['FM'][0]
        listPersonas['MF'].pop(0)
        listPersonas['FM'].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    if Length(listPersonas['MF'],0) :
        while Length(listPersonas['MF'],0)  and Length(listPersonas['FA'],0):
            Persona1 = listPersonas['MF'][0]
            Persona2 = listPersonas['FA'][0]
            listPersonas['MF'].pop(0)
            listPersonas['FA'].pop(0)
            Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    elif Length(listPersonas['FM'], 0) :
        while Length(listPersonas['FM'], 0)  and Length(listPersonas['MA'], 0):
            Persona1 = listPersonas['FM'][0]
            Persona2 = listPersonas['MA'][0]
            listPersonas['FM'].pop(0)
            listPersonas['MA'].pop(0)
            Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    return listPersonas
#Dado un archivo, una lista con personas, imprime en el archivo dado las parejas que se formaron
#En esta funcion, el resultado seran todas parejas de bisexuales
#MatchingBisexuals: file Array -> Array
def MatchingBisexuals(Salida, listPersonas):
    while Length(listPersonas['MA'],1) :
        Persona1 = listPersonas['MA'][0]
        Persona2 = listPersonas['MA'][1]
        listPersonas['MA'].pop(0)
        listPersonas['MA'].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1]+ ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    while Length(listPersonas['FA'],1) :
        Persona1 = listPersonas['FA'][0]
        Persona2 = listPersonas['FA'][1]
        listPersonas['FA'].pop(0)
        listPersonas['FA'].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    if(len(listPersonas['FA']) == 1 and len(listPersonas['MA']) == 1):
        Persona1 = listPersonas['MA'][0]
        Persona2 = listPersonas['FA'][0]
        listPersonas['MA'].pop(0)
        listPersonas['FA'].pop(0)
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")
    return listPersonas
#Dada un archivo y la lista de candidatos a formar pareje, llama a una funcion auxiliar para crear 
# las parejas dependiendo de la secxualidad de las personas en la lista
# y devuelve las personas que se quedaron sin
# MatchingFunction: file Array -> Dict()
def MatchingFunction(Salida, Candidatos):
    for key, value in Candidatos.items():
        Candidatos[key]['11a14'] = MatchingHomosexuals(Salida, value['11a14'], 'M') 
        Candidatos[key]['11a14'] = MatchingHomosexuals(Salida, value['11a14'], 'F')
        Candidatos[key]['11a14'] = MatchingHeterosexuals(Salida, value['11a14']) 
        Candidatos[key]['11a14'] = MatchingBisexuals(Salida, value['11a14'])
        Candidatos[key]['15a17'] = MatchingHomosexuals(Salida, value['15a17'], 'M') 
        Candidatos[key]['15a17'] = MatchingHomosexuals(Salida, value['15a17'], 'F')
        Candidatos[key]['15a17'] = MatchingHeterosexuals(Salida, value['15a17']) 
        Candidatos[key]['15a17'] = MatchingBisexuals(Salida, value['15a17'])
        Candidatos[key]['18+'] = MatchingHomosexuals(Salida, value['18+'], 'M') 
        Candidatos[key]['18+'] = MatchingHomosexuals(Salida, value['18+'], 'F')
        Candidatos[key]['18+'] = MatchingHeterosexuals(Salida, value['18+']) 
        Candidatos[key]['18+'] = MatchingBisexuals(Salida, value['18+'])
    return Candidatos

if __name__ == "__main__":
    ArchivoEntrada = input("Ingrese el nombre del archivo a leer: ")
    ArchivosParejas = input("Ingrese nombre del archivo que contendra a las parejas: ")
    Entrada = open(ArchivoEntrada,"r")
    NoParejas = []
    Candidatos = dict()
    if Entrada.mode == 'r':
        Lineas = Entrada.readlines()
        Entrada.close()
        for l in Lineas:
            l = l.split(", ")
            l[5] = l[5][0]
            if int(l[3]) <= 10 or l[5] == "N":
                NoParejas.append(( l[0], l[1], l[2],  int(l[3]), l[4], l[5]))
            else:
                Persona = ( l[0],l[1],  l[2], int(l[3]), l[4], l[5])
                Candidatos = Filtrado(Persona,Candidatos)
        Salida = open(ArchivosParejas, "w+")
        Candidatos = MatchingFunction(Salida, Candidatos)
        for key, value in Candidatos.items():
            Solteros11a14 = value['11a14']['MM'] + value['11a14']['MF'] + value['11a14']['MA'] + value['11a14']['FM'] + value['11a14']['FF'] + value['11a14']['FA']
            Solteros15a17 = value['15a17']['MM'] + value['15a17']['MF'] + value['15a17']['MA'] + value['15a17']['FM'] + value['15a17']['FF'] + value['15a17']['FA']
            Solteros18 = value['18+']['MM'] + value['18+']['MF'] + value['18+']['MA'] + value['18+']['FM'] + value['18+']['FF'] + value['18+']['FA']
            NoParejas = NoParejas + Solteros11a14 + Solteros15a17 + Solteros18
        ImprimeSingles(NoParejas)
