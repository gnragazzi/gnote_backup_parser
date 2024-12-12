#Programita para parsear backup de notas creadas en gnote
import xml.etree.ElementTree as ET
import sys
from datetime import datetime

n = len(sys.argv)

if(n!=2):
    print(n)
    print("Número incorrecto de argumentos.")
    exit()

archivo_entrada = sys.argv[1]

try:
    tree = ET.parse(archivo_entrada)
    root = tree.getroot()
    nombre_notas = [x.get("id") + ".note" for x in root]

    nombre_notas.sort()

    t = str(datetime.now().timestamp())
    t = t.replace(t[t.find(".")],"")

    f = open(t + ".txt","w",encoding="utf-8")

    for nombre in nombre_notas:
        temp = ET.parse(nombre).getroot()[1][0]
        texto = "Nota id: " + nombre
        for elem in temp.iter(tag=None):
            texto += temp.text
            if(elem.tail != None):
                texto += elem.tail
        texto += '\n***\n\n'
        f.write(texto)

    f.close()
except:
    print("El archivo " + archivo_entrada + " no existe.")


