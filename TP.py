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

if __name__ == "__main__":
    Entrada = open("ejemplo1.txt","r")
    Salida = open("Salida.txt", "w+")
    NoParejas = []
    Candidatos = []
    if Entrada.mode == 'r':
        Lineas = Entrada.readlines()
        Entrada.close()
        for l in Lineas:
            l = l.split(", ")
            l[5] = l[5][0]
            if int(l[3]) <= 10 or l[5] == "N":
                NoParejas.append({'Nombre': l[0], 'Apellido': l[1], 'Localidad': l[2], 'Edad': int(l[3]), 'Genero': l[4], 'GeneroInteres': l[5]})
            else:
                Candidatos.append({'Nombre': l[0], 'Apellido': l[1], 'Localidad': l[2], 'Edad': int(l[3]), 'Genero': l[4], 'GeneroInteres': l[5]})
        ImprimeSingles(NoParejas)