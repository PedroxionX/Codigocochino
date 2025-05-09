# reservas.py

peliculas = ["Matrix", "Titanic", "Avengers"]
funciones = {
    "Matrix": ["10:00", "13:00", "18:00"],
    "Titanic": ["11:00", "16:00"],
    "Avengers": ["12:00", "20:00"]
}
asientos_disponibles = {
    "Matrix": {"10:00": ["A1", "A2", "A3"], "13:00": ["A1", "A2"], "18:00": ["A1"]},
    "Titanic": {"11:00": ["A1", "A2"], "16:00": ["A1", "A2", "A3"]},
    "Avengers": {"12:00": ["A1", "A2"], "20:00": ["A1"]}
}
reservas = []

def mostrar_peliculas():
    for i, p in enumerate(peliculas):
        print(i+1, p)

def seleccionar_pelicula():
    mostrar_peliculas()
    p = int(input("elige una pelicula: "))
    return peliculas[p-1]

def seleccionar_funcion(peli):
    print("Funciones disponibles para", peli)
    for i, h in enumerate(funciones[peli]):
        print(i+1, h)
    h = int(input("elige funcion: "))
    return funciones[peli][h-1]

def seleccionar_asiento(peli, func):
    print("asientos disponibles:", asientos_disponibles[peli][func])
    a = input("elige asiento: ")
    if a in asientos_disponibles[peli][func]:
        return a
    else:
        print("no disponible")
        return seleccionar_asiento(peli, func)

def reservar():
    p = seleccionar_pelicula()
    f = seleccionar_funcion(p)
    a = seleccionar_asiento(p, f)
    reservas.append({"pelicula": p, "funcion": f, "asiento": a})
    asientos_disponibles[p][f].remove(a)
    print("reserva confirmada:", p, f, a)

# Bucle principal
while True:
    reservar()
    x = input("otra reserva? (s/n): ")
    if x != "s":
        break
