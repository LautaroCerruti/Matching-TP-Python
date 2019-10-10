# Trabajo Practico N1, 
# Integrantes del grupo: Lautaro Cerruti y Alesandro Regolo
# En el tp, se recibira una lista de personas con datos personales tales como su nombre, aprellido, edad, localidad, etc
# y se formara parejas de 2 persoanas en base a su ubicacion, su edad y su preferencia sexual. Se maximizara la cantidad de parejas formadas.
# La entrada del programa sera un archivo en el cual se almacenara dicha informacion a utilizar.

# La forma a representar a las personas  con su respectiva informacion en este practico sera de la siguiente forma
# Persona(Nombre,Apellido,Localidad,Edad,Genero,GeneroInteres)
# Persona(str,str,str,int,str,str)

# A su vez representamos a los candidatos como un diccionario, en el cual las keys son la ubicacion en la que se encuantran las personas
# y el valor dentro del campo es un diccionario en el cual guardaremos otro diccionario con 3 keys las cuales representaran los distintos gurpos de personas
# ordenados segun la edad que tienen. Para luedo dentro de ellas almacenar otro diccionario con 6 keys en las que se agrupan a las personas 
# segun su Genero y su interes.
# candidatos{Localidad:{'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}}

# El resultado de este programa sera 2 archivos de salida que contendran, por un lado las parejas formadas y por otro lado las personas
# que no pudieron formar pareja, especificando el motivo.

# MayorA: List -> Int -> Int -> Bool
# Dada una lista y una cantidad, verifica si la lista posee mas elementos que la cantidad dada
def MayorA(lista, cant, contador = 0):
    if(contador > cant ):   # Si el contador es mayor a la cantidad dada como parametro
        return True         # Retorna verdadero
    elif(lista == []):      # Si la lista esta vacia
        return False        # Retorna falso
    else:
        return MayorA(lista[1:], cant, contador + 1)    # Hace una recursividad con el contador+1 y la tail de la lista

# ImprimeSingles: array(tuplas(str,str,str,int,str,str))
# Dada una lista de personas, guarda en un archivo las personas que no pueden formar una pareja y el porque.
def ImprimeSingles(NoParejas):
    ArchivoSalidaSolteros = input("Ingrese nombre del archivo que contendra a los solteros :")
    SalidaSingles = open(ArchivoSalidaSolteros, "w+")
    for persona in NoParejas: # Por cada persona en el array que no tienen parejas
        string = persona[0] + ", " + persona[1] + ", " + str(persona[3]) + ", " + persona[2] + ", NO TIENE PAREJA POR " # Crea un string auxiliar
        if persona[3] <= 10:    # Si es menor de 11 años
            SalidaSingles.write(string  + "SER MENOR DE 11 AÑOS" + "\n") # Imprime en el archivo la string auxiliar + La causa que es su edad
        elif persona[5] == "N": # Si no tiene intereses
            SalidaSingles.write(string + "NO TENER INTERES" + "\n") # Imprime en el archivo la string auxiliar + La causa que es la falta de interes
        else:   # Si es por no haberle encontrado pareja
            SalidaSingles.write(string + "NO DISPONIBILIDAD DE PERSONAS" + "\n") # Imprime en el archivo la string auxiliar + La causa
    SalidaSingles.close()

# Como ya filtramos por localidad, la lista de candidatos se reduce al diccionario por rango etarios, y la persona como la tupla con los 7 datos
# AgregaALocalidad: Tupla(str,str,str,int,str,str) Dict(Dict(array(Tuplas(str,str,str,int,str,str))))
# Dada una Persona y un diccionario que continen a las personas que vivien es dicha localidad
# agrego a dicha persona a la lista que corresponde segun su edad y orientacion sexual
def AgregaALocalidad(Persona, DictLocalidad):
    if Persona[3] >= 18:    # Si es mayor de 18 años:
        DictLocalidad['18+'][Persona[4] + Persona[5]].append(Persona)   # Agrega a esta persona a la lista dentro del diccionario dado por la key " Genero + GeneroInteres" que es un value del diccionario de edades, relacionado con la key "18+"
    elif Persona[3] >= 15:  # Si es mayor de 14 años y menor a 18:
        DictLocalidad['15a17'][Persona[4] + Persona[5]].append(Persona) # Agrega a esta persona a la lista dentro del diccionario dado por la key " Genero + GeneroInteres" que es un value del diccionario de edades, relacionado con la key "15a17"
    else:   # Si es mayor de 10 años y menor a 15:
        DictLocalidad['11a14'][Persona[4] + Persona[5]].append(Persona) # Agrega a esta persona a la lista dentro del diccionario dado por la key " Genero + GeneroInteres" que es un value del diccionario de edades, relacionado con la kay "11a14"

# Representamos la estructura donde se guarda cada persona como el diccionario de candidatos que se menciona mas arriba, y la persona como la tupla con los 7 datos
# Agregar: Tupla(str,str,str,int,str,str) -> Dict(Dict(Dict(array(Tuplas(str,str,str,int,str,str))))) -> Dict(Dict(Dict(array(Tuplas(str,str,str,int,str,str)))))
# Dada una persona y un diccionario que contiene a todos los candidatos a formar parejas
# Agrega la persona al campo del diccionario  de la localidad a la que pertenece y de ser necesario 
# Agrega otra key al diccionario y agrega la persona al campo.
def Agregar(Persona, Candidatos):
    if  Persona[2] in Candidatos.keys():    # Si la localidad de la persona ya es una key del diccionario donde lo agregamos:
        AgregaALocalidad(Persona, Candidatos[Persona[2]])   # Ejecutamos AgregaLocalidad con la persona y el diccionario de esta localidad
    else:                                   # En caso de que la localidad no sea una key
        Candidatos[Persona[2]] = {'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}} # Creamos esta key con un value que es el diccionario de edades, con cada edad con su respectivo diccionario para separar las personas
        AgregaALocalidad(Persona, Candidatos[Persona[2]])   # Ejecutamos AgregaLocalidad con la persona y el diccionario que acabamos de crear
    return Candidatos   # Retorna el diccionario con la persona agregada en su localidad correspondiente

# En este caso la lista de candidatos es la de una localidad y de un rango etario correspondiente, por lo que solo nos quedaria un diccionario con las keys de generos y intereses, con el array correspondiete a cada una
# MatchingHomosexuals: file Dict(array(Tuplas(str,str,str,int,str,str))) str
# Dado un archivo, una lista con personas y un genero, imprime en el archivo dado las parejas que se formaron
# En este caso todas las parejas van a ser del mismo genero, representado por el string
def MatchingHomosexuals(Salida, listPersonas, generoPersonas):
    while MayorA(listPersonas[generoPersonas + generoPersonas],1):  # Mientras haya mas de 1 homosexual en la lista:
        Persona1 = listPersonas[generoPersonas + generoPersonas][0] # Tomamos al primer Homosexual de la lista
        Persona2 = listPersonas[generoPersonas + generoPersonas][1] # Tomamos al segundo Homosexual de la lista
        listPersonas[generoPersonas + generoPersonas].pop(0)    # Eliminamos el primer elemento del array
        listPersonas[generoPersonas + generoPersonas].pop(0)    # Eliminamos nuevamente el primer elemento del array, por lo que con los 2 pops, eliminariamos las 2 persona que acabamos de matchear
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja
    if len(listPersonas[generoPersonas + generoPersonas]) == 1 and MayorA(listPersonas[generoPersonas + 'A'],0): # Si me quedo un unico Homosexual y Tengo algun Bisexual en esta localidad y rango etario
        Persona1 = listPersonas[generoPersonas + generoPersonas][0] # Tomamos al unico homosexual que nos quedo sin pareja
        listPersonas[generoPersonas + generoPersonas].pop(0)    # Luego de tomar al unico homosexual que queda, lo sacamos de la lista, por lo que quedaria sin mas homosexuales
        Persona2 = listPersonas[generoPersonas + 'A'][0]        # Tomamos el primer Bisexual de la lista
        listPersonas[generoPersonas + 'A'].pop(0)               # Borramos a este bisexual
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja

# En este caso la lista de candidatos es la de una localidad y de un rango etario correspondiente, por lo que solo nos quedaria un diccionario con las keys de generos y intereses, con el array correspondiete a cada una
# MatchingHeterosexuals: file Dict(array(Tuplas(str,str,str,int,str,str)))
# Dado un archivo, una lista con personas, imprime en el archivo dado las parejas que se formaron
# En este caso todas las parejas van a ser parejas heterosexuales
def MatchingHeterosexuals(Salida, listPersonas):
    while MayorA(listPersonas['MF'], 0)  and MayorA(listPersonas['FM'],0):  #Mientras haya 1 hombre y 1 mujer:
        Persona1 = listPersonas['MF'][0]    # Tomo un hombre de la lista
        Persona2 = listPersonas['FM'][0]    # Tomo una mujer de la lista
        listPersonas['MF'].pop(0)    # Eliminamos el hombre que tomamos del array
        listPersonas['FM'].pop(0)    # Eliminamos la mujer que tomamos del array
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja
    if MayorA(listPersonas['MF'], 0):    # Si me quedaron hombres sin matchear:
        while MayorA(listPersonas['MF'], 0) and MayorA(listPersonas['FA'], 0): # Mientras Haya hombres Hetero sin matchear y mujeres bi sin matchear
            Persona1 = listPersonas['MF'][0]    # Tomo un hombre de la lista
            Persona2 = listPersonas['FA'][0]    # Tomo una mujer de la lista
            listPersonas['MF'].pop(0)    # Eliminamos el hombre que tomamos del array
            listPersonas['FA'].pop(0)    # Eliminamos la mujer que tomamos del array
            Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja
    elif MayorA(listPersonas['FM'], 0): # Si me quedaron mujeres sin matchear
        while MayorA(listPersonas['FM'], 0) and MayorA(listPersonas['MA'], 0): # Mientras haya mujeres hetero y hombres bisexuales:
            Persona1 = listPersonas['FM'][0]    # Tomo una mujer de la lista
            Persona2 = listPersonas['MA'][0]    # Tomo un hombre de la lista
            listPersonas['FM'].pop(0)    # Eliminamos la mujer que tomamos del array
            listPersonas['MA'].pop(0)    # Eliminamos el hombre que tomamos del array
            Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja

# En este caso la lista de candidatos es la de una localidad y de un rango etario correspondiente, por lo que solo nos quedaria un diccionario con las keys de generos y intereses, con el array correspondiete a cada una
# MatchingBisexuals: file Dict(array(Tuplas(str,str,str,int,str,str)))
# Dado un archivo, una lista con personas, imprime en el archivo dado las parejas que se formaron
# En esta funcion, el resultado seran todas parejas de bisexuales
def MatchingBisexuals(Salida, listPersonas):
    while MayorA(listPersonas['MA'], 1):    # Mientras haya hombres bisexuales:
        Persona1 = listPersonas['MA'][0]    # Toma el primer hombre bisexual
        Persona2 = listPersonas['MA'][1]    # Toma el segundo hombre bisexual
        listPersonas['MA'].pop(0)    # Eliminamos el primer elemento del array
        listPersonas['MA'].pop(0)    # Eliminamos nuevamente el primer elemento del array, por lo que con los 2 pops, eliminariamos las 2 persona que acabamos de matchear
        Salida.write(Persona1[0] + ", " + Persona1[1]+ ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")   # Imprime En el archivo la pareja
    while MayorA(listPersonas['FA'], 1):    # Mientras haya mujeres bisexuales:
        Persona1 = listPersonas['FA'][0]    # Toma a la primer mujer bisexual
        Persona2 = listPersonas['FA'][1]    # Toma a la segunda mujer bisexual
        listPersonas['FA'].pop(0)    # Eliminamos el primer elemento del array
        listPersonas['FA'].pop(0)    # Eliminamos nuevamente el primer elemento del array, por lo que con los 2 pops, eliminariamos las 2 persona que acabamos de matchear
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja
    if(len(listPersonas['FA']) == 1 and len(listPersonas['MA']) == 1): # Si me queda un hombre bi y una mujer bi:
        Persona1 = listPersonas['MA'][0]    # Tomo al hombre
        Persona2 = listPersonas['FA'][0]    # Tomo a la mujer
        listPersonas['MA'].pop(0)           # Elimino al hombre que acabo de tomar
        listPersonas['FA'].pop(0)           # Elimino a la mujer que acabo de tomar
        Salida.write(Persona1[0] + ", " + Persona1[1] + ", " + str(Persona1[3]) + " - " + Persona2[0] + ", " + Persona2[1] + ", " + str(Persona2[3]) + " - " + Persona2[2] + "\n")  # Imprime En el archivo la pareja

# En este caso la lista de candidatos la representamos con la estructura de diccionarios mencionada arriba de todo
# MatchingFunction: file -> Dict(Dict(Dict(array(Tuplas(str,str,str,int,str,str))))) -> Dict(Dict(Dict(array(Tuplas(str,str,str,int,str,str)))))
# Dada un archivo y la lista de candidatos a formar pareje, llama a unas funciones auxiliar para crear 
# las parejas dependiendo del genero de las personas en la lista
# y devuelve las personas que se quedaron sin pareja
def MatchingFunction(Salida, Candidatos):
    for key, value in Candidatos.items():
        MatchingHomosexuals(Salida, value['11a14'], 'M')    # Matchea Hombres Homosexuales entre 11 y 14 años
        MatchingHomosexuals(Salida, value['11a14'], 'F')    # Matchea Mujeres Homosexuales entre 11 y 14 años
        MatchingHeterosexuals(Salida, value['11a14'])       # Matchea Heterosexuales entre 11 y 14 años
        MatchingBisexuals(Salida, value['11a14'])           # Matchea Bisexuales entre 11 y 14 años
        MatchingHomosexuals(Salida, value['15a17'], 'M')    # Matchea Hombres Homosexuales entre 15 y 17 años
        MatchingHomosexuals(Salida, value['15a17'], 'F')    # Matchea Mujeres Homosexuales entre 15 y 17 años
        MatchingHeterosexuals(Salida, value['15a17'])       # Matchea Heterosexuales entre 15 y 17 años
        MatchingBisexuals(Salida, value['15a17'])           # Matchea Bisexuales entre 15 y 17 años
        MatchingHomosexuals(Salida, value['18+'], 'M')      # Matchea Hombres Homosexuales entre mayores a 18
        MatchingHomosexuals(Salida, value['18+'], 'F')      # Matchea Mujeres Homosexuales entre mayores a 18
        MatchingHeterosexuals(Salida, value['18+'])         # Matchea Heterosexuales entre mayores a 18
        MatchingBisexuals(Salida, value['18+'])             # Matchea Bisexuales entre mayores a 18
    return Candidatos                                       # Retorno el diccionario que tiene las personas que no van a poder ser matcheadas

# En el main del programa, que es lo primero que se ejecuta,
# nos encargaos de pedir los nombres de los archivos de entrada y salida
# Leer todas las lineas de la entrada y separar las que no pueden formar parejas desde el comienzo
# Ejecutar todas la funciones correspondientes para poder formar las parejas e imprimir los resulados
if __name__ == "__main__":
    ArchivoEntrada = input("Ingrese el nombre del archivo a leer: ")
    ArchivosParejas = input("Ingrese nombre del archivo que contendra a las parejas: ")
    Entrada = open(ArchivoEntrada,"r",encoding ="latin1")
    NoParejas = []  # Los que no tienen parejas los almacenaremos en una lista
    Candidatos = dict() # Creamos el diccionario para los candidatos
    Lineas = Entrada.readlines()    # Leemos todas las lineas del archivo
    Entrada.close()
    for linea in Lineas:    # Por cada linea del archivo:
        linea = linea.split(", ")   # Separamos el string en un array de valores, usando el separador ', '
        linea[5] = linea[5][0]      # Como en el ultimo campo nos queda "value\n" y sabemos que es un solo caracter antes del \n, tomamos solo lo almacenado en la posicion 0
        linea[3] = int(linea[3])    # Transformamos la edad en int
        if linea[3] <= 10 or linea[5] == "N":   # si la edad es menor a 11 o no tiene intereses:
            NoParejas.append((linea[0], linea[1], linea[2],  linea[3], linea[4], linea[5])) # Almacenamos a esta persona en la lista de solteros
        else:   # Si es un posible candidato
            Candidatos = Agregar((linea[0],linea[1],  linea[2], linea[3], linea[4], linea[5]), Candidatos) # Agregamos a la estrucura de candidatos esta persona
    Salida = open(ArchivosParejas, "w+")
    Candidatos = MatchingFunction(Salida, Candidatos)    # Ejecutamos la foncion para hacer los matcheos
    for key, value in Candidatos.items():   # Por cada localidad en candidatos
        Solteros11a14 = value['11a14']['MM'] + value['11a14']['MF'] + value['11a14']['MA'] + value['11a14']['FM'] + value['11a14']['FF'] + value['11a14']['FA'] # Unimos todas las posibles listas donde podria haber solteros de 11 a 14 años
        Solteros15a17 = value['15a17']['MM'] + value['15a17']['MF'] + value['15a17']['MA'] + value['15a17']['FM'] + value['15a17']['FF'] + value['15a17']['FA'] # Unimos todas las posibles listas donde podria haber solteros de 15 a 17 años
        Solteros18 = value['18+']['MM'] + value['18+']['MF'] + value['18+']['MA'] + value['18+']['FM'] + value['18+']['FF'] + value['18+']['FA']    # Unimos todas las posibles listas donde podria haber solteros de mayores de 18 años
        NoParejas = NoParejas + Solteros11a14 + Solteros15a17 + Solteros18 # Unimos todas las listas de solteros
    ImprimeSingles(NoParejas)   # Ejecutamos la funcion para imprimir los solteros es un archivo
