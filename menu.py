#! /usr/bin/python3
import sys

from datetime import date
import self as self

from listaTrabajo import ListaTrabajos
from lista_Clientes import ListaClientes
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos


class Menu:
    "Muestra ocpiones"

    def __init__(self):
        self.rc = RepositorioClientes()
        self.rt = RepositorioTrabajos()
        self.list_clientes = ListaClientes()
        self.listaTrabajo = ListaTrabajos()
        self.opciones = {
            "1": self.mostrar_clientes,
            "2": self.nuevo_cliente,
            "3": self.buscar_cliente,
            "4": self.modificar_datos_clientes,
            "5": self.borrar_cliente,
            "6": self.nuevo_trabajo,
            "7": self.mostrar_trabajos,
            "8": self.finalizar_trabajo,
            "9": self.retirar_trabajo,
            "10": self.eliminar_trabajo,
            "11": self.historial_T,

            "0": self.salir
        }

    def mostrar_menu(self):
        print("""
Menú del sistema:
===================================================
- CLIENTES:                                                     
===================================================
1. Mostrar todos los clientes. 
2. Ingresar un nuevo cliente.                                       
3. Buscar un cliente.                                               
4. Modificar los datos de un cliente.                               
5. Eliminar un cliente.                                               
===================================================
- TRABAJOS:                                                                        
===================================================
6. Cargar nuevo trabajo.                                                                          
7. Mostrar todos los trabajos.
8. Finalizar un trabajo.
9. Retirar un trabajo.
10.Eliminar un trabajo.
11.Ver Historial de trabajos de cada cliente.
===================================================
0. Salir del sistema
        """)

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.
        '''
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))

    def mostrar_clientes(self):
        "Muestra todos los clientes"
        c = self.rc.get_all()
        if c:
            l = self.rc.get_all_corporativos()
            print("""         Clientes CORPORATIVOS:       """)
            if l:
                for i in l:
                    print("..................................................")
                    print(i)
                    print("..................................................")
            t = self.rc.get_all_particulares()

            print("""         Clientes PARTICULARES:        """)
            if t:
                for i in t:
                    print("..................................................")
                    print(i)
                    print("..................................................")
            input("\nPrecione 0 para volver al menu principal")
        else:
            print("\nNo hay cliente cargados en el sistema")
            input("\nPrecione 0 para volver al menu principal")

    def nuevo_cliente(self):
        "Ingresa un nuevo cliente, ya sea corporativo o particular"
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de Cliente: C:Corporativo / P:Particular")
        nombre = input("Ingrese el nombre: ")
        if tipo in ("C", "c"):
            nombre_contacto = input("Ingrese el nombre de contacto: ")
            telefono_contacto = input("Ingrese el telefono de contacto: ")
        else:
            apellido = input("Ingrese el apellido: ")
        telefono = input("Ingrese el numero de telefono: ")
        mail = input("Ingrese el correo electronico: ")
        if tipo in ("C", "c"):
            c = self.list_clientes.nuevo_cliente_corporativo(nombre, nombre_contacto, telefono_contacto, telefono, mail)
        else:
            c = self.list_clientes.nuevo_cliente_particular(nombre, apellido, telefono, mail)
        if c is None:
            print("Error al cargar cliente")
        else:
            print("Cliente cargado correctamente")

    def buscar_cliente(self):
        "Solicita un ID, busca al cliente con ese ID y lo muestra"
        c = self.rc.get_all()
        if c:
            while True:
                try:
                    id_cliente = int(input("Ingrese el ID del cliente que desea buscar: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            c = self.list_clientes._buscar_por_id(id_cliente)
            if c == None:
                print("El ID ingresado no pertenece a ningun cliente que este cargado actualmente")
            else:
                print("\n..................................................\n")
                print(c)
                print("..................................................")
            input("\nPrecione 0 para volver al menu principal")
        else:
            print("\nNo se encuentra ningun cliente particular que este guardado en el sistema")
            input("\nPrecione 0 para volver al menu principal")

    def modificar_datos_clientes(self):
        "Modificar los datos de un cliente, ya sea cliente corporativo o particular"
        tipo = "A"
        while tipo not in ("C", "c", "P", "p"):
            tipo = input("Ingrese el tipo de Cliente:  C:Corporativo / P:Particular")

        if tipo in ("C", "c"):
            l = self.rc.get_all_corporativos()
            if l:
                print("""         Clientes CORPORATIVOS           """)
                print("""-----------------------------------------""")
                for i in l:
                    print(i)
                    print("..................................................\n")
                    while True:
                        try:
                            id_cliente = int(input("Ingrese el ID del cliente: "))
                        except ValueError:
                            print('Debe ingresar un numero')
                            continue
                        break
                    cliente = self.list_clientes._buscar_por_id(id_cliente)
                    if cliente:
                        print(cliente)
                        print("Modifique el dato que desea: ")
                        print("..................................................\n")
                        nombre_empresa = input("Ingrese el nombre de la empresa: ")
                        nombre_contacto = input("Ingrese el nombre del contacto: ")
                        telefono_contacto = input("Ingrese el telefono del contacto: ")
                        telefono = input("Ingrese el telefono: ")
                        Mail = input("Ingrese el mail: ")
                        C = self.list_clientes.modificar_datos_CC(nombre_empresa, nombre_contacto, telefono_contacto,
                                                                  telefono, Mail, id_cliente)
                        if C == None:
                            print("Error al modificar los datos del cliente")
                            input("\nPrecione 0 para volver al menu principal")
                        else:
                            print("""Los datos fueron modificados con exito""")
                            print("\n..................................................\n")
                            print(cliente)
                            print("..................................................")
                            input("\nPrecione 0 para volver al menu principal")
                    else:
                        print("\nEl ID ingresado no pertenece a ningun cliente corporativo guardado en el sistema")
                        input("\nPrecione 0 para volver al menu principal")
                else:
                    print("\nNo se encuentra ningun cliente corporativo que este guardado en el sistema")
                    input("\nPrecione 0 para volver al menu principal")
        else:
            l = self.rc.get_all_particulares()
            if l:
                print("""         Clientes PARTICULARES            """)
                print("""------------------------------------------""")
                for i in l:
                    print(i)
                    print("..................................................\n")
                while True:
                    try:
                        id_cliente = int(input("Ingrese el ID del cliente: "))
                    except ValueError:
                        print('Debe ingresar un numero')
                        continue
                    break
                cliente = self.list_clientes._buscar_por_id(id_cliente)
                if cliente:
                    print(cliente)
                    print("..................................................\n")

                    Nombre = input("Ingrese el nombre: ")
                    Apellido = input("Ingrese el apellido: ")
                    Tel = input("Ingrese el telefono: ")
                    Mail = input("Ingrese el mail: ")
                    C = self.list_clientes.modificar_datos_CP(Nombre, Apellido, Tel, Mail, id_cliente)
                    if C == None:
                        print("Error al modificar los datos del cliente")
                        input("\nPrecione 0 para volver al menu principal")
                    else:
                        print("Los datos fueron modificados con exito")
                        print("..................................................\n")
                        print(cliente)
                        print("..................................................")
                        input("\nPrecione 0 para volver al menu principal")
                else:
                    print("\nEl ID ingresado no pertenece a ningun cliente particular que este guardado en el sistema")
                    input("\nPrecione 0 para volver al menu principal")
            else:
                print("\nNo se encuentra ningun cliente particular que este guardado en el sistema")
                input("\nPrecione 0 para volver al menu principal")

    def borrar_cliente(self):
        "Solicita un ID y borra al cliente, en caso de que tenga trabajos pendientes, tambien los borra"
        b = self.rc.get_all_corporativos()
        if b:

            print("           Clientes CORPORATIVOS           ")
            print("-------------------------------------------")
            for i in b:
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre_empresa)
                print("..................................................")
        t = self.rc.get_all_particulares()
        if t:
            print("""         CLIENTES PARTICULARES""")
            print("""-----------------------------------------""")
            for i in t:
                print("ID cliente: ", i.id_cliente, "- Nombre: ", i.nombre)
                print("..................................................\n")
        if b or t:
            while True:
                try:
                    id_cliente = int(input("Ingrese el ID del cliente: "))
                except ValueError:
                    print('Debe ingresar un numero')
                    continue
                break
            d = self.list_clientes._buscar_por_id(id_cliente)
            if d:
                print("\n..................................................\n")
                print(d)
                print("..................................................\n")
                f = "A"
                while f not in ("1", "2"):
                    f = input("""¿Seguro que desea eliminar al cliente? 
       1:Si Borrar.  / 2: No Borrar. 

       Ingrese una opcion: """)
                if f in ("1"):
                    a = self.list_clientes._buscar_por_id(id_cliente)
                    if a == None:
                        print("Ocurrio un error al querer borrar al cliente")
                        print("..................................................")
                        input("\nPrecione 0 para volver al menu principal")
                    else:
                        print("El cliente fue eliminado con exito")
                        print("..................................................")
                        input("\nPrecione 0 para volver al menu principal")

                else:
                    print("\nEl cliente no ha sido eliminado.")
                    input("\nPrecione 0 para volver al menu principal")
            else:
                print("\nEl ID ingresado no pertenece a ningun cliente que este guardado en el sistema")
                input("\nPrecione 0 para volver al menu principal")
        else:
            print("\nActualmente no se encuentra ningun cliente guardado en el sistema")
            input("\nPrecione 0 para volver al menu principal")

    def salir(self):
        """Sale del sistema"""
        print("Gracias por utilizar el sistema.")
        sys.exit(0)


if __name__ == "__main__":
    m = Menu()
    m.ejecutar()
