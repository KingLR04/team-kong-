'''print('.Crear una aplicación que se ingrese por teclado el nombre de 5 empleados,
 sueldo cobrado por cada empleado en los ultimos 3 meses. Mostrar en pantalla el total pagado a cada empleado
 en los ultimos 3 meses obtener y mostrar cual fue el empleado de mayor ingreso.\n')

Personal1 =  input('ingrese el nombre del primer personal: ' )
Personal2 =  input('ingrese el nombre del segundo personal: ')
Personal3 =  input('ingrese el nombre del tercer personal: ')
Personal4 =  input('ingrese el nombre del cuarto personal: ')
Personal5 =  input('ingrese el nombre del quinto personal: ')


 salario= (50000 , 80000 , 90000,  40000 ,  60000)

salario1, salario2 , salario3 , salario4,salario5 = salarios

if salario1 > salario2  and sueldo1 > sueldo3  and sueldo1 > sueldo4 and sueldo1 > sueldo5:
    print(personal1 , ' "Logré sacar el total  de ',  salario1 ,'en los últimos tres meses, y es el que tiene mayores ingresos' )

elif salario2 > salario1  and salario2 > salario3  and salario2 > salario4 and salario1 > salario5:
    print(personal2, ' "Logré sacar el total de ', salario2, 'en los últimos tres meses, y es el que tiene mayores ingresos')

elif  salario3 > salario1  and salario3 > salario2  and salario3 > salario4 and salario3 > salario5:
    print(personal3, ' "Logré sacar el total de ', salario3, 'en los últimos tres meses, y es el que tiene mayores ingresos')

elif salario4 > salario1  and salario4 > salario2  and salario4 > salario3 and salario4 > salario5:
    print(personal4, ' "Logré sacar el total de ', salario4, 'en los últimos tres meses, y es el que tiene mayores ingresos')

elif  salario5 > salario1  and salario5 > salario2  and salario5 > salario3 and salario5 > sueldo4:
    print(personal5, '  "Logré sacar el total de ', salario5, 'en los últimos tres meses, y es el que tiene mayores ingresos')

print(' Salario generalmente recibido de todos\n')

print(personal1, salario1)
print(personal2, salario2)
print(personal3, salario3)
print(personal4, salario4)
print(personal5, salario5)



