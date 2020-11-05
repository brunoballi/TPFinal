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

    def modificar_datos_CP(self, nombre, apellido, telefono, mail, id_cliente):
        """Recibe los datos modificados y actualiza los datos del cliente particular"""
        Cp = self._buscar_por_id(id_cliente)
        if Cp:
            if nombre == '':
                nombre = Cp.nombre
            else:
                Cp.nombre = nombre
            if apellido == '':
                apellido = Cp.apellido
            else:
                Cp.apellido = apellido
            if telefono == '':
                telefono = Cp.telefono
            else:
                Cp.telefono = telefono
            if mail == '':
                mail = Cp.mail
            else:
                Cp.mail = mail
            return self.rc.update(Cp)
        return None

    def modificar_datos_CC(self, nombre_empresa, nombre_contacto, telefono_contacto, telefono, mail, id_cliente):
        """Recibe los datos modificados y actualiza los datos del cliente corporativo"""
        Cc = self._buscar_por_id(id_cliente)
        if Cc:
            if nombre_empresa == '':
                nombre_empresa = Cc.nombre_empresa
            else:
                Cc.nombre_empresa = nombre_empresa
            if nombre_contacto == '':
                nombre_contacto = Cc.nombre_contacto
            else:
                Cc.nombre_contacto = nombre_contacto
            if telefono_contacto == '':
                telefono_contacto = Cc.telefono_contacto
            else:
                Cc.telefono_contacto = telefono_contacto
            if telefono == '':
                telefono = Cc.telefono
            else:
                Cc.telefono = telefono
            if mail == '':
                mail = Cc.mail
            else:
                Cc.mail = mail
            return self.rc.update(Cc)
        return None




