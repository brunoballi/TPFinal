#! /usr/bin/python3


from clienteCorporativo import ClienteCorporativo
from clienteParticular import ClienteParticular
from repositorioClientes import RepositorioClientes
from repositorioTrabajos import RepositorioTrabajos


class ListaClientes:

    def __init__(self):
        self.rc = RepositorioClientes()
        self.rt = RepositorioTrabajos()
        self.list_clientes = self.rc.get_all()
        self.listaTrabajo = self.rt.get_all()

    def nuevo_cliente_corporativo(self, nombre, nombre_contacto, telefono_contacto, telefono, mail):
        """Recibe los datos de un cliente corporativo, crea un nuevo cliente corporativo y lo agrega a lista de clientes"""
        c = ClienteCorporativo(nombre, nombre_contacto, telefono_contacto,
                               telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.list_clientes.append(c)
            return c

    def nuevo_cliente_particular(self, nombre, apellido, telefono, mail):
        """Recibe los datos de un cliente particular, crea un nuevo cliente particular y lo agrega a la lista de clietes"""
        c = ClienteParticular(nombre, apellido, telefono, mail)
        c.id_cliente = self.rc.store(c)
        if c.id_cliente == 0:
            return None
        else:
            self.list_clientes.append(c)
            return c

    def _buscar_por_id(self, id_cliente):
        """Recibe un id de contacto y retorna el contacto que coincide con esa
        id, o None si ninguno de ellos coincide"""

        for C in self.list_clientes:
            if C.id_cliente == int(id_cliente):
                return (C)
        return None






