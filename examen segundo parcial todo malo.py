print("<--------------------------->")

import itertools
import ed
import xc
class Contacto():
    nuevoid = itertools.count()
    def __init__(self, nombre, apellidos, correo, direccion, numero):
        self.codigo=next(self.nuevoid)
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.direccion = direccion
        self.numero = numero
class Agenda():
    def __init__(self):
        self.contactos = []
    def ordenar_nmbre(self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)
    def ordenar_apdos(self):
        self.contactos.sort(key=lambda contacto: contacto.apellidos)
    def añadir(self, nombre, apellidos, correo, direccion, numero):
        contacto=Contacto(nombre, apellidos, correo, direccion, numero)
        self.contactos.append(contacto)
    def mostrar(self):
        self.submenu0rden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    def buscar(self, textbuscar):
        encontrado = 0
        for contacto in self.contactos:
            if(re.findall(textbuscar, contacto.nombre)) or (re.findall(textbuscar, contacto.apellidos)):
                self.imprimeContacto(contacto)
                encontrado = encontrado+1
                self.submenubuscar(contacto.codigo)
        if encontrado == 0:
            self.no_encontrado()

    def modificar(self, codigo):
        for contacto in self.contactos:
            if contacto.codigo==codigo:
                del self.contactos[codigo]
                nombre=str(input("Nombre:\n"))
                apellidos=str(input("Apellidos:\n"))
                correo=str(input("Correo:\n"))
                direccion=str(input("Direccion:\n"))
                numero=str(input("Numero telefonico:\n"))
                contacto=Contacto(nombre.capitalize(), apellidos.capitalize(),
                                  correo.capitalize(), direccion.capitalize(), numero)
                self.contactos.append(contacto)

    def submenubuscar(self, codigo):
        print("<--------------------------->")
        print("Quieres (m)odificarlo")
        print("<--------------------------->")
        opcion = str(input(""))
        if opcion == "m" or opcion == "M":
            self.modificar(codigo)
        else:
            print("Continuamos sin cambios!"
    def grabar(self, contacto):
        with open("agenda.csv", "w") as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(("codigo", "nombre", "apellidos", "numero"))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo, contacto.nombre, contacto.apellidos, contacto.correo,
                                   contacto.direccion, contacto.numero))
    def imprimeContacto(self, contacto):
        print("<--------------------------->")
        print("<--------------------------->")
        print("codigo: {}".format(contacto.codigo))
        