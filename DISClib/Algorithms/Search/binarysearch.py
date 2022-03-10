from DISClib.ADT import list as lt

def busqueda(lista, elemento, cmpfunction):
    """
    Busqueda Binaria de un elemento en una lista ordenada ascendentemente
    Resultado: Indice en la lista donde se encuentra el elemento. -1 si no se encuentra.
    """
    i = 1
    f = lt.size(lista)
    pos = -1
    encontro = False
    while i <= f and not encontro:
        # calcular la posicion de la mitad entre i y f
        m = (i + f) // 2
        if cmpfunction(lista, m, elemento) == 0:
            pos = m
            encontro = True
        elif cmpfunction(lista, m, elemento) == 1:
            i = m + 1
        else:
            f = m - 1

    return pos