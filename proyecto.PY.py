print("gran menu")
opcion = 0
while opcion != 4:
    print("1.Grados celcius a farhenheit")
    print("2.Convertir dolar a peso")
    print("3.Convertir metros a pies")
    print("4.Salir")
    opcion = int(input("que necesitas :"))

    if opcion == 1:
        a = int(input("Escriba un numero:\n"))
        b = 1.8
        total = (a * b) + 32
        print("El resultado es", total, "grados fahrenheit")
    elif opcion == 2:
        dolares = int(input("Cuantos dolares deseas cambiar a pesos Dominican?:\n"))
        peso = 58
        total = peso * dolares
        print("Serian", total, "pesos dominican")
    elif opcion == 3:
        m = int(input("Introduzca el numero\n")) * 3.2
        print("Serian", m, "Pies")
print("gracias por participar")
