# Desarrollo tarea Nº1 Pruebas de Software
#
# Se busca realizar una mejora en la estimación de 
# requerimiento y formas de realizar pruebas, con la ayuda
# de un compañero.
# A continuación se deja el código realizado de acuerdo a
# esta mejora de requerimientos antes mencionada.

#import de librerias
import os.path

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
        print("[Notificación] Pila recuperada")
        return battery
    else:
        file = open("bat_savedata.txt", "w")
        file.close()
        print("[Notificación] Archivo de pila creado")
        return ["","","","","","","","","",""]

#Filtra el texto para poder entregar el resultado
def filterText(text):
    res = ''
    for x in text:
        if x not in ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z','1','2','3','4','5','6','7','8','9','0']:
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
        print("Pila vacía, ingrese un texto para realizar esta función")
        return
    else:
        print()
        print("Texto de MAYOR tamaño ubicado en espacio:", temp[-1][1],"\nCon",temp[-1][0],"caracteres\n","El texto es:",battery[temp[-1][1]])
        print("\nTexto de MENOR tamaño ubicado en espacio:", temp[0][1],"\nCon",temp[0][0],"caracteres\n","El texto es:",battery[temp[0][1]])
        return

#imprime el tamaño del texto almacenado en el espacio de la pila según el formato
def seeBat(pos, battery):
    if battery[pos] == "":
        print("El texto número", pos, "está Vacío\nNo tiene caracteres")
        return
    else:
        print("El texto número",pos,"es:",battery[pos],"\nCon una cantidad de",len(battery[pos]),"caracteres")
        return

#comparacion de tamaños
def lenCompare(pos1,pos2,battery):
    if len(battery[pos1]) > len(battery[pos2]):
        print("Texto",pos1,"es mayor que el texto",pos2,"en:",str(len(battery[pos1])-len(battery[pos2])),"caracteres")
        return
    elif len(battery[pos1]) < len(battery[pos2]):
        print("Texto",pos2,"es mayor que el texto",pos1,"en:",str(len(battery[pos2])-len(battery[pos1])),"caracteres")
        return
    else:
        print("Texto",pos1,"y texto",pos2,"son iguales en tamaño con",str(len(battery[pos1])),"caracteres")
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
            # 1 = SI
            if res == "1":
                battery[-1] = text
                print("== OPERACION REALIZADA ==")
                return battery
            elif res == "2":
                print("== OPERACIÓN CANCELADA ==")
                return battery
    else:
        print("Texto '",text,"' almacenado en espacio",x)
        return battery

#quita un texto
def delText(battery):
    flag = 1
    for x in range(9,-1,-1):
        if battery[x] != "":
            print("TEXTO",battery[x],"ELIMINADO")
            battery[x] != ""
            flag = 0
            break
    if flag:
        print("Pila vacía, no se ha eliminado texto")
        return battery
    return battery

#almacena el estado actual de la pila
def storeBat(battery):
    res = ";".join(battery)
    file = open("bat_savedata.txt", "w")
    file.write(res)
    file.close()
    print("[Notificación] Pila almacenada en archivo")
    return

#menu general
def menu(battery):
    print("Bienvenido al editor de pila!")
    battery = loadBat(battery)
    while(1):
        res = input("Seleccione operación a realizar:\n1- Ver texto más largo y más corto\n2- Imprimir un texto de la pila\n3- Comparar tamaños de textos en pila\n4- Agregar un texto a la pila\n5- Quitar último texto de la pila\n6- Salir\n>")
        if res == "1":
            majorMinor(battery)
        elif res == "2":
            while(1):
                res1 = input("Indique posición a ver de la pila (0-9)\n10- Volver\n>")
                if res1 in [str(x) for x in range(10)]:
                    seeBat(int(res1), battery)
                    break
                elif res1 == "10":
                    break
                else:
                    print("Indique el valor correcto")
        elif res == "3":
            while(1):
                res1 = input("Ingrese posición 1 para comparar de la pila (0-9)\n10- Volver\n>")
                if res1 == "10":
                    break
                res2 = input("Ingrese posición 2 para comparar de la pila (0-9)\n10- Volver\n>")
                if res2 == "10":
                    break
                if (res1 in [str(x) for x in range(10)]) and (res2 in [str(x) for x in range(10)]):
                    lenCompare(int(res1),int(res2),battery)
                    break
                else:
                    print("Indique el valor correcto")
        elif res == "4":
            while(1):
                res1 = input("Ingrese texto a agregar a la pila (dejar vacío para volver)\n>")
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
            return

battery = []
menu(battery)


