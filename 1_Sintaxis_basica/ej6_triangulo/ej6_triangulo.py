def triangulo(num):
    if num < 0: print("Error. Número debe ser > 0")
    elif num == 1:
        print('*')
    else:
        triangulo(num-1)
        print('*'*num)


#Main
num = int(input("Introduzca el lado del triángulo: "))
triangulo(num)