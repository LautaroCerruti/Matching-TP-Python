def ImprimeSingles(NoParejas):
    SalidaSingles = open("SalidaSingles.txt", "w+")
    for p in NoParejas:
        string = p['Nombre'] + ", " + p['Apellido'] + ", " + str(p['Edad']) + ", " + p['Localidad'] + ", NO TIENE PAREJA POR "
        if p['Edad'] <= 10:
            SalidaSingles.write(string  + "SER MENOR DE 11 AÑOS" + "\n")
        elif p['GeneroInteres'] == "N":
            SalidaSingles.write(string + "NO TENER INTERES" + "\n")
        else:
            SalidaSingles.write(string + "NO DISPONIBILIDAD DE PERSONAS" + "\n")
    SalidaSingles.close()

def AgregaPersona(Persona, DictLocalidad):
    if Persona['Edad'] >= 18:
        DictLocalidad['18+'][Persona['Genero'] + Persona['GeneroInteres']].append(Persona)
    elif Persona['Edad'] >= 15:
        DictLocalidad['15a17'][Persona['Genero'] + Persona['GeneroInteres']].append(Persona)
    else:
        DictLocalidad['11a14'][Persona['Genero'] + Persona['GeneroInteres']].append(Persona)
    return DictLocalidad

def Filtrado(Persona, Candidatos):
    if  Persona["Localidad"] in Candidatos.keys() :
        Candidatos[Persona["Localidad"]] = AgregaPersona(Persona, Candidatos[Persona["Localidad"]])
    else :
        Candidatos[Persona["Localidad"]] = {'11a14':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '15a17':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}, '18+':{'MM':[], 'MF':[], 'MA':[], 'FM':[], 'FF':[], 'FA':[]}}
        Candidatos[Persona["Localidad"]] = AgregaPersona(Persona, Candidatos[Persona["Localidad"]])
    return Candidatos

def MatchingHomosexuals(Salida, listPersonas, generoPersonas):
    while len(listPersonas[generoPersonas + generoPersonas]) > 1:
        Persona1 = listPersonas[generoPersonas + generoPersonas][0]
        Persona2 = listPersonas[generoPersonas + generoPersonas][1]
        listPersonas[generoPersonas + generoPersonas].pop(0)
        listPersonas[generoPersonas + generoPersonas].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    if len(listPersonas[generoPersonas + generoPersonas]) == 1 and len(listPersonas[generoPersonas + 'A']) > 0:
        Persona1 = listPersonas[generoPersonas + generoPersonas][0]
        listPersonas[generoPersonas + generoPersonas].pop(0)
        Persona2 = listPersonas[generoPersonas + 'A'][0]
        listPersonas[generoPersonas + 'A'].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    return listPersonas

def MatchingHeterosexuals(Salida, listPersonas):
    while len(listPersonas['MF']) > 0 and len(listPersonas['FM']) > 0:
        Persona1 = listPersonas['MF'][0]
        Persona2 = listPersonas['FM'][0]
        listPersonas['MF'].pop(0)
        listPersonas['FM'].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    if len(listPersonas['MF']) > 0:
        while len(listPersonas['MF']) > 0 and len(listPersonas['FA']) > 0:
            Persona1 = listPersonas['MF'][0]
            Persona2 = listPersonas['FA'][0]
            listPersonas['MF'].pop(0)
            listPersonas['FA'].pop(0)
            Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    elif len(listPersonas['FM']) > 0:
        while len(listPersonas['FM']) > 0 and len(listPersonas['MA']) > 0:
            Persona1 = listPersonas['FM'][0]
            Persona2 = listPersonas['MA'][0]
            listPersonas['FM'].pop(0)
            listPersonas['MA'].pop(0)
            Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    return listPersonas

def MatchingBisexuals(Salida, listPersonas):
    while len(listPersonas['MA']) > 1:
        Persona1 = listPersonas['MA'][0]
        Persona2 = listPersonas['MA'][1]
        listPersonas['MA'].pop(0)
        listPersonas['MA'].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    while len(listPersonas['FA']) > 1:
        Persona1 = listPersonas['FA'][0]
        Persona2 = listPersonas['FA'][1]
        listPersonas['FA'].pop(0)
        listPersonas['FA'].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    if(len(listPersonas['FA']) == 1 and len(listPersonas['MA']) == 1):
        Persona1 = listPersonas['MA'][0]
        Persona2 = listPersonas['FA'][0]
        listPersonas['MA'].pop(0)
        listPersonas['FA'].pop(0)
        Salida.write(Persona1['Nombre'] + ", " + Persona1['Apellido'] + ", " + str(Persona1['Edad']) + " - " + Persona2['Nombre'] + ", " + Persona2['Apellido'] + ", " + str(Persona2['Edad']) + " - " + Persona2['Localidad'] + "\n")
    return listPersonas

def MatchingFunctionAux(Salida, listPersonas):
    listPersonas = MatchingHomosexuals(Salida, listPersonas, 'M')
    listPersonas = MatchingHomosexuals(Salida, listPersonas, 'F')
    listPersonas = MatchingHeterosexuals(Salida, listPersonas)
    listPersonas = MatchingBisexuals(Salida, listPersonas)
    return listPersonas

def MatchingFunction(Salida, Candidatos):
    for key, value in Candidatos.items():
        Candidatos[key]['11a14'] = MatchingFunctionAux(Salida, value['11a14'])
        Candidatos[key]['15a17'] = MatchingFunctionAux(Salida, value['15a17'])
        Candidatos[key]['18+'] = MatchingFunctionAux(Salida, value['18+'])
    return Candidatos

if __name__ == "__main__":
    Entrada = open("ejemplo2.txt","r")
    NoParejas = []
    Candidatos = dict()
    if Entrada.mode == 'r':
        Lineas = Entrada.readlines()
        Entrada.close()
        for l in Lineas:
            l = l.split(", ")
            l[5] = l[5][0]
            if int(l[3]) <= 10 or l[5] == "N":
                NoParejas.append({'Nombre': l[0], 'Apellido': l[1], 'Localidad': l[2], 'Edad': int(l[3]), 'Genero': l[4], 'GeneroInteres': l[5]})
            else:
                Persona = {'Nombre': l[0], 'Apellido': l[1], 'Localidad': l[2], 'Edad': int(l[3]), 'Genero': l[4], 'GeneroInteres': l[5]}
                Candidatos = Filtrado(Persona,Candidatos)
        Salida = open("Salida.txt", "w+")
        Candidatos = MatchingFunction(Salida, Candidatos)
        for key, value in Candidatos.items():
            Solteros11a14 = value['11a14']['MM'] + value['11a14']['MF'] + value['11a14']['MA'] + value['11a14']['FM'] + value['11a14']['FF'] + value['11a14']['FA']
            Solteros15a17 = value['15a17']['MM'] + value['15a17']['MF'] + value['15a17']['MA'] + value['15a17']['FM'] + value['15a17']['FF'] + value['15a17']['FA']
            Solteros18 = value['18+']['MM'] + value['18+']['MF'] + value['18+']['MA'] + value['18+']['FM'] + value['18+']['FF'] + value['18+']['FA']
            NoParejas = NoParejas + Solteros11a14 + Solteros15a17 + Solteros18
        ImprimeSingles(NoParejas)
