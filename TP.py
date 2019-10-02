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

if __name__ == "__main__":
    Entrada = open("ejemplo3.txt","r")
    #Salida = open("Salida.txt", "w+")
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
        ImprimeSingles(NoParejas)
