a = 3
b = 3.0
print(type(a)) #class int
print(type(b)) #class float
print(a is b) #false

#Asignación múltiple
tipo, x, y, z, activo = 'Punto1', 10, 10, 10, True

#Visualización de valores
print("Tipo: ", tipo, "Pos: ", x, y, z, " Activo: ", activo)

#Asignación múltiple con una tupla
tupla_punto = ('Punto2', 11, 11, 11, False)
tipo, x, y, z, activo = tupla_punto
print("Tipo: ", tipo, " Pos: ", x, y, z, " Activo: ", activo)

#Asignación múltiple con una lista
lista_punto = ['Punto', 12, 12, 12, True]
tipo, x, y, z, activo = lista_punto
print("Tipo: ", tipo, " Pos: ", x, y, z, " Activo: ", activo)