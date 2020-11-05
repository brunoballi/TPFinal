#! /usr/bin/env python3
from cliente import Cliente

class ClienteCorporativo(Cliente):
    '''Representa un cliente particular'''
    def __init__(self, nombre_empresa, nombre_contacto, telefono_contacto,
            telefono, mail, id_cliente = None):
        self.nombre_empresa = nombre_empresa
        self.nombre_contacto = nombre_contacto
        self.telefono_contacto = telefono_contacto
        super().__init__(telefono, mail, id_cliente)
         
    def __str__(self):
        Cadena = f"ID cliente: {self.id_cliente}\n"
        Cadena += f"{self.nombre_empresa} (Cliente Corporativo)\n"
        Cadena += f"Tel.Corporativo: {self.telefono} - Email: {self.mail}\n"
        Cadena += f"Nombre de Contacto: {self.nombre_contacto} - Tel.Contacto: {self.telefono_contacto}\n"
        return Cadena
