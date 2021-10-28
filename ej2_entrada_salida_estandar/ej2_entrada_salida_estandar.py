print(1,2,3)
print("Hola son las", 6, "de la tarde")
print("Hola son las"+str(6)+"de la tarde")
print("Hola son las "+str(6)+" de la tarde")
print("%d %f %s" % (2.5, 2.5, 2.5))

print("El producto %s cantidad=%d precio=%.2f"%("cesta",23,13.456))

print(1,2,3)
print(1,2,3,sep='-')
print(1,2,3,sep='-',end='.\n')
print('hola'*3)

num1=input("Dame el número 1: ")
print(type(num1))
num2=input("Dame el número 2: ")
print(type(num2))
print(int(num1)+int(num2))
num1 = "hola"
a = int(num1) #ValueError


