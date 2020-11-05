#! /usr/bin/python3

from trabajo import Trabajo
from repositorioTrabajos import RepositorioTrabajos
import datetime

class ListaTrabajos:

    def __init__(self):
        self.rt = RepositorioTrabajos()
        self.listaTrabajo = self.rt.get_all()

    def nuevo_trabajo(self, cliente, fecha_ingreso, fecha_entrega_propuesta, descripcion):
        "Recibe los datos de una trabajo, crea uno nuevo y lo agrega a la lista"
        t = Trabajo(cliente, fecha_ingreso, fecha_entrega_propuesta, None, descripcion, False)
        t.id_trabajo = self.rt.store(t)
        if t.id_trabajo == 0:
            return None
        else:
            self.listaTrabajo.append(t)
            return t

    def _buscar_por_id(self, id_trabajo):
        """Recibe un id de trabajo y retorna el cliente que coincide con esa
        id, o None si ninguno de ellos coincide"""

        for t in self.listaTrabajo:
            if t.id_trabajo == int(id_trabajo):
                return (t)
        return None

    def modificar_datos_trabajo(self, fecha_ingreso, fecha_entrega_propuesta, descripcion, id_trabajo):
        """Recibe un trabajo y modifica sus datos"""
        t = self._buscar_por_id(id_trabajo)
        if t:
            t.fecha_ingreso = fecha_ingreso
            t.fecha_entrega_propuesta = fecha_entrega_propuesta
            t.descripcion = descripcion
            return self.rt.update(t)
        return None




