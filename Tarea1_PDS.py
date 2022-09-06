# Desarrollo tarea Nº1 Pruebas de Software
#
# Se busca realizar una mejora en la estimación de 
# requerimiento y formas de realizar pruebas, con la ayuda
# de un compañero.
# A continuación se deja el código realizado de acuerdo a
# esta mejora de requerimientos antes mencionada.

#import de librerias
import os.path
import datetime

#Logger para almacenamiento de entradas y salidas por consola
def logger(mensaje, tipo, reset = 0):
    texto = open("[DEBUG]_Logs.txt","a")
    if reset == 1:
        texto.write("\n####### NEW TEST "+str(datetime.date.today())+" #######\n")
    elif reset == 2:
        texto.write("\n####### END TEST "+str(datetime.date.today())+"#######\n")
    else:
        #Tipo 0 : Output
        if tipo == 0:
            print(mensaje)
            texto.write("\n["+datetime.datetime.now().strftime("%I:%M:%S %p")+"] Output: "+mensaje+"\n")
        #Tipo -1: Output pero sin imprimir por pantalla
        elif tipo == -1:
            texto.write("\n["+datetime.datetime.now().strftime("%I:%M:%S %p")+"] Output: "+mensaje+"\n")
        #Tipo 1 : Input
        elif tipo == 1:
            texto.write("\n["+datetime.datetime.now().strftime("%I:%M:%S %p")+"] Input: "+mensaje+"\n")
    texto.close()
    return

#Carga la pila o la crea en caso de no existir
def loadBat(battery):
    file_exists = os.path.exists("bat_savedata.txt")
    if file_exists:
        with open("bat_savedata.txt") as f:
            s = "".join([l.replace("\n","") for l in f]) 
        s = s.split(";")
        if len(s) >= 10:
            for x in range(10):
                battery.append(s[x])
        else:
            for x in s:
                battery.append(x)
            battery = battery + [""]*(10-len(s))
        logger("[Notificación] Pila recuperada",tipo=0)
        return battery
    else:
        file = open("bat_savedata.txt", "w")
        file.close()
        logger("[Notificación] Archivo de pila creado",tipo=0)
        return ["","","","","","","","","",""]

#Filtra el texto para poder entregar el resultado
def filterText(text):
    res = ''
    for x in text:
        if x not in ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','1','2','3','4','5','6','7','8','9','0',' ']:
            continue
        else:
            res+=x
    return res

#Obtiene el texto de mayor y menor tamaño
def majorMinor(battery):
    temp1 = [[len(battery[x]),x] for x in range(10)]
    temp1.sort(key = lambda x: x[0])
    temp = []
    for x in range(10):
        if temp1[x][0] != 0:
            temp.append(temp1[x])
    if len(temp) == 0:
        logger("Pila vacía, ingrese un texto para realizar esta función", tipo=0)
        return
    else:
        i = " ".join(("Texto de MAYOR tamaño ubicado en espacio:",str(temp[-1][1]),"\nCon",str(temp[-1][0]),"caracteres\n","El texto es:",str(battery[temp[-1][1]])))
        logger(i, tipo = 0)
        i = " ".join(("\nTexto de MENOR tamaño ubicado en espacio:", str(temp[0][1]),"\nCon",str(temp[0][0]),"caracteres\n","El texto es:",str(battery[temp[0][1]])))
        logger(i, tipo = 0)
        return

#imprime el tamaño del texto almacenado en el espacio de la pila según el formato
def seeBat(pos, battery):
    if battery[pos] == "":
        i = (("El texto número", str(pos), "está Vacío\nNo tiene caracteres"))
        logger(i, tipo = 0)
        return
    else:
        i = " ".join(("El texto número",str(pos),"es:",str(battery[pos]),"\nCon una cantidad de",str(len(battery[pos])),"caracteres"))
        logger(i, tipo = 0)
        return

#comparacion de tamaños
def lenCompare(pos1,pos2,battery):
    if len(battery[pos1]) > len(battery[pos2]):
        i = " ".join(("Texto",str(pos1),"es mayor que el texto",str(pos2),"en:",str(len(battery[pos1])-len(battery[pos2])),"caracteres"))
        logger(i, tipo = 0)
        return
    elif len(battery[pos1]) < len(battery[pos2]):
        i = " ".join(("Texto",str(pos2),"es mayor que el texto",str(pos1),"en:",str(len(battery[pos2])-len(battery[pos1])),"caracteres"))
        logger(i, tipo = 0)
        return
    else:
        i = " ".join(("Texto",str(pos1),"y texto",str(pos2),"son iguales en tamaño con",str(len(battery[pos1])),"caracteres"))
        logger(i, tipo=0)
        return

#añade un texto
def addText(battery, text):
    flag = 1
    for x in range(10):
        if battery[x] == "":
            battery[x] = text
            res = x
            flag=0
            break
    if flag:
        while(1):
            res = input("Texto '",text,"' no ha podido ser añadido, pila esta completa, ¿Desea reemplazar el último espacio de la pila (9) con su nuevo texto?\nTEXTO A REEMPLAZAR:"+battery[-1]+"\n1 - SI\n2 - NO\n>")
            i = " ".join(("Texto '",str(text),"' no ha podido ser añadido, pila esta completa, ¿Desea reemplazar el último espacio de la pila (9) con su nuevo texto?\nTEXTO A REEMPLAZAR:"+str(battery[-1])+"\n1 - SI\n2 - NO\n>"))
            logger(i,tipo=-1)
            logger(res, tipo = 1)
            # 1 = SI
            if res == "1":
                battery[-1] = text
                logger("== OPERACION REALIZADA ==",tipo = 0)
                return battery
            elif res == "2":
                logger("== OPERACIÓN CANCELADA ==",tipo = 0)
                return battery
    else:
        i = " ".join(("Texto '",str(text),"' almacenado en espacio",str(x)))
        logger(i,tipo = 0)
        return battery

#quita un texto
def delText(battery):
    flag = 1
    for x in range(9,-1,-1):
        if battery[x] != "":
            i = " ".join(("TEXTO",str(battery[x]),"ELIMINADO"))
            logger(i, tipo = 0)
            battery[x] != ""
            flag = 0
            break
    if flag:
        logger("Pila vacía, no se ha eliminado texto", tipo = 0)
        return battery
    return battery

#almacena el estado actual de la pila
def storeBat(battery):
    res = ";".join(battery)
    file = open("bat_savedata.txt", "w")
    file.write(res)
    file.close()
    logger("[Notificación] Pila almacenada en archivo", tipo = 0)
    return

#menu general
def menu(battery):
    logger("Bienvenido al editor de pila!", tipo = 0)
    battery = loadBat(battery)
    while(1):
        res = input("Seleccione operación a realizar:\n1- Ver texto más largo y más corto\n2- Imprimir un texto de la pila\n3- Comparar tamaños de textos en pila\n4- Agregar un texto a la pila\n5- Quitar último texto de la pila\n6- Salir\n>")
        i = "Seleccione operación a realizar:\n1- Ver texto más largo y más corto\n2- Imprimir un texto de la pila\n3- Comparar tamaños de textos en pila\n4- Agregar un texto a la pila\n5- Quitar último texto de la pila\n6- Salir\n>"
        logger(i, tipo = -1)
        logger(res, tipo = 1)
        if res == "1":
            majorMinor(battery)
        elif res == "2":
            while(1):
                res1 = input("Indique posición a ver de la pila (0-9)\n10- Volver\n>")
                i = "Indique posición a ver de la pila (0-9)\n10- Volver\n>"
                logger(i, tipo = -1)
                logger(res1, tipo=1)
                if res1 in [str(x) for x in range(10)]:
                    seeBat(int(res1), battery)
                    break
                elif res1 == "10":
                    break
                else:
                    logger("Indique el valor correcto", tipo = 0)
        elif res == "3":
            while(1):
                res1 = input("Ingrese posición 1 para comparar de la pila (0-9)\n10- Volver\n>")
                i = "Ingrese posición 1 para comparar de la pila (0-9)\n10- Volver\n>"
                logger(i, tipo = -1)
                logger(res1, tipo = 1)
                if res1 == "10":
                    break
                res2 = input("Ingrese posición 2 para comparar de la pila (0-9)\n10- Volver\n>")
                i = "Ingrese posición 2 para comparar de la pila (0-9)\n10- Volver\n>"
                logger(i, tipo = -1)
                logger(res2, tipo = 1)
                if res2 == "10":
                    break
                if (res1 in [str(x) for x in range(10)]) and (res2 in [str(x) for x in range(10)]):
                    lenCompare(int(res1),int(res2),battery)
                    break
                else:
                    logger("Indique el valor correcto", tipo = 0)
        elif res == "4":
            while(1):
                res1 = input("Ingrese texto a agregar a la pila (dejar vacío para volver)\n>")
                i = "Ingrese texto a agregar a la pila (dejar vacío para volver)\n>"
                logger(i, tipo = -1)
                logger(res1, tipo = 1)
                if res1 != "":
                    battery = addText(battery, filterText(res1))
                    storeBat(battery)
                    break
                else:
                    break

        elif res == "5":
            while(1):
                battery = delText(battery)
                storeBat(battery)
                break
        elif res == "6":
            logger("", reset = 2, tipo = 0)
            return

battery = []
logger("", reset = 1, tipo = 0)
menu(battery)


