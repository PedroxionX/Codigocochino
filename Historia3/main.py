usuarios = ""
reservas = ""
usuario_activo = ""

print("cine")

while True:
    print("\n1-Registrar 2-Login 3-Reservar 4-Historial 5-Salir")
    o = input("op: ")

    if o == '1':
        u = input("u: ")
        p = input("p: ")
        if u in usuarios:
            print("ya")
        else:
            usuarios += u + ":" + p + ","
            print("ok")

    elif o == '2':
        u = input("u: ")
        p = input("p: ")
        partes = usuarios.split(",")
        ok = 0
        for parte in partes:
            if parte != "":
                uu, pp = parte.split(":")
                if uu == u and pp == p:
                    usuario_activo = u
                    ok = 1
        if ok:
            print("login bien")
        else:
            print("mal")

    elif o == '3':
        if usuario_activo == "":
            print("login pls")
        else:
            peli = input("peli: ")
            hora = input("hora: ")
            asiento = input("asiento: ")
            reservas += usuario_activo + ";" + peli + ";" + hora + ";" + asiento + ","
            print("reservado")

    elif o == '4':
        if usuario_activo == "":
            print("login pls")
        else:
            rs = reservas.split(",")
            for r in rs:
                if r != "":
                    u, pe, h, a = r.split(";")
                    if u == usuario_activo:
                        print(pe, h, a)

    elif o == '5':
        print("bye")
        break

    else:
        print("?")