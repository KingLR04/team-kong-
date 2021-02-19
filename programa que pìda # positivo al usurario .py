
print( "programa que pida # positivo al usuario ")

print("Suma")
valor = 0
while valor !=1:
    print("Suma de numeros positivos")
    n1= int(input("Ingrese  su primer numero: "))
    n2= int(input("Ingrese su segundo numero: "))
    if n1 > 0 and n2 > 0:
        print('el resultado es:',n1 + n2 )
    else:
        print("Error numero negativos y ceros no se pueden rechazar ")
        break





