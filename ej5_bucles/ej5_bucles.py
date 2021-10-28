contador=0
while contador<=30:
    print("Contando: ", contador)
    contador += 1
else:
    print("Hemos terminado de contar")


#For
for i in range(0,31): #Cuenta hasta 30
    print("Contando: ", i)
else:
    print("Hemos terminado de contar")

"""break: termina la ejecución de un bucle, además no ejecuta 
el bloque de instrucciones indicado por la parte else.
continue: deja de ejecutar las restantes instrucciones del bucle 
y vuelve a iterar.
pass: indica una instrucción nula, no ejecuta nada, pero no tenemos
errores de sintaxis"""

"""Con la instrucción for, podemos ejecutar más de una secuencia
utilizando la función zip. Esta función crea una secuencia donde cada 
elemento es una tupla de los elementos de cada secuencia que
toma como parámetro"""

list(zip(range(1,4),["ana", "juan", "pepe"]))

for x,y in zip(range(1,4),["ana","juan","pepe"]):
    print(x,y)
