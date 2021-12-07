def crear_lista_una_dim():
    parar = False
    lista = []
    while not parar:
        element = input("Elemento (-1 para salir): ")
        if not element == "-1":
            lista.append(element)
        else:
            parar = True
    return lista

def crear_lista_varias_dim(dim):
    lista = [] 
    if dim == 1:
        return crear_lista_una_dim()
    else:
        parar = False
        while not parar:
            s = input("Crear elemento para dimensión "+ str(dim) +"(s ó n): ")
            if s == "s":
                lis = crear_lista_varias_dim(dim-1)
                lista.append(lis)
            else:
                parar = True
        return lista
    
def borrar_elemento(element, lista, dim):
    if dim == 1:
        while element in lista:
            lista.remove(element)
    else:
        for sublist in lista:
            borrar_elemento(element, sublist, dim-1)

def contar_elemento(element, lista, dim):
    contador = 0
    if dim == 1:
        return lista.count(element)
    else:
        for sublist in lista:
            contador += contar_elemento(element, sublist, dim-1)
        return contador



dimensiones = int(input("Introduzca el número de dimensiones: "))
if dimensiones < 1:
    print("Error. Número de dimensiones debe ser > 1")
else:
    lista = crear_lista_varias_dim(dimensiones)
    print(lista)
    element = input("Introduzca el elemento a borrar: ")
    borrar_elemento(element, lista, dimensiones)
    print(lista)
    element = input("Introduzca el elemento a contar: ")
    print(contar_elemento(element, lista, dimensiones))
    