impresión('1. Crear una persona de clase que tenga como atributos la "cedula, nombre, apellido y la edad (definir las propiedades para poder acceder a dichos atributos)". Definir como responsabilidad una cuncion para mostrar ó imprimir. Crear una segunda clase profesor que aquíde de la clase Persona. Añadir un atributo sueldo (y su propiedad) y en la función para imprimir su sueldo. Definir un objeto de la clase persona y llamar a sus funciones y propiedades. También crear un objeto de la clase profesor y llamar a sus funciones y propiedades. \n')

persona de clase ():

    def __init__(self, cedu,nom, ape, ed):
        self .cedula = cedu
        self . nombre = nom
        self .  = apellido ape
        self .edad = ed

    def mostrar (sí self ):
        wp  = 'cedula: {0} / nombre : {1} / apellido: {2} / edad : {3} '
        devolver wp. formato(auto. cedula, self . nombre, self . apellido, self . Edad)

clase profesor(persona):

    def __init__(self, cedu, nom, ape, ed, suld):
        súper(). __init__(cedu, nom, simio, ed )
        self. salario  = suld

profe = profesor('001-1285166-2', 'junior ', 'santana ', '37', ' / salario: 40000$ pesos dominicanos')
impresión(profe. Mostrar() , profe. salario )

