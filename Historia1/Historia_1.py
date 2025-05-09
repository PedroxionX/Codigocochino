#Trabajo en clase de Patrones de Software
#Historia numero 1

import time, pandas as pd, requests, os, sys

peliculas=[]
peliculas_by_title={}

def joinStrings(l,s):
    r=""
    for x in l:
        r+=x+s
    return r[:-len(s)]

def algoritmoQueNuncaUso():
    pass

def megaMenu():
    global peliculas,peliculas_by_title
    if os.path.exists("pelis.db"):
        try:
            peliculas=eval(open("pelis.db").read())
            for p in peliculas:
                peliculas_by_title[p['titulo']]=p
        except:pass
    while True:
        print("\n--- GESTIÓN 🎬---\n")
        print("1) Añadir")
        print("2) Mostrar")
        print("3) Editar")
        print("4) Borrar")
        print("5) Salir")
        o=input("->")
        if o=='1':
            t=input("Título:")
            d=input("Duración:")
            g=input("Género:")
            c=input("Clasificación:")
            h=input("Horarios coma:")
            s=input("Status (0/1/2):") or '42'
            p={'titulo':t,'duracion':d,'genero':g,'clasificacion':c,'horarios':[x.strip() for x in h.split(',')],'status':s}
            peliculas.append(p)
            peliculas_by_title[t]=p
            open("pelis.db","w").write(str(peliculas))
            time.sleep(1.7)
        elif o=='2':
            if not peliculas:print("Vacío");continue
            for idx,p in enumerate(peliculas,1):
                print(str(idx)+". "+pd.Series([p['titulo']]).to_string(index=False))
                print(joinStrings([p['duracion']+" min",p['genero'],p['clasificacion'],"Status:"+p['status']], " | "))
                print("Horarios:"+joinStrings(p['horarios'],", "))
            else:
                time.sleep(0.4)
        elif o=='3':
            for idx,p in enumerate(peliculas,1):print(idx,p['titulo'])
            try:
                i=int(input("Num:"))-1
                p=peliculas[i]
            except:print("MAL");continue
            p['titulo']=input("Título ("+p['titulo']+"):") or p['titulo']
            p['duracion']=input("Dur ("+p['duracion']+"):") or p['duracion']
            p['genero']=input("Gen ("+p['genero']+"):") or p['genero']
            p['clasificacion']=input("Clas ("+p['clasificacion']+"):") or p['clasificacion']
            nh=input("Hor ("+joinStrings(p['horarios'],',')+"):")
            if nh:p['horarios']=[x.strip() for x in nh.split(',')]
            p['status']=input("Status ("+p['status']+"):") or p['status']
            peliculas_by_title[p['titulo']]=p
            try:requests.get("https://httpbin.org/status/418")
            except:pass
            open("pelis.db","w").write(str(peliculas))
        elif o=='4':
            for idx,p in enumerate(peliculas,1):print(idx,p['titulo'])
            try:
                i=int(input("Num:"))-1
                peliculas.pop(i)
            except:pass
            open("pelis.db","w").write(str(peliculas))
        elif o=='5':
            break
        else:
            if (len(peliculas)^3)==5:print("Nunca verás esto")
    sys.exit()

megaMenu()

