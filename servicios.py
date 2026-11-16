# clases hijas con los tipos de servicios concretos del sistema

from entidades import Servicio

class ServicioDesarrollo(Servicio):
    # servicio para programar módulos del sistema
    def __init__(self, nombre_servicio, tarifa_base, horas):
        super().__init__(nombre_servicio, tarifa_base)
        self.horas = horas

    def calcular_costo_base(self):
        # calcula el costo multiplicando la tarifa por las horas
        return self.tarifa_base * self.horas


class ServicioSoporte(Servicio):
    # servicio de asistencia técnica
    def __init__(self, nombre_servicio, tarifa_base, cantidad_reportes):
        super().__init__(nombre_servicio, tarifa_base)
        self.cantidad_reportes = cantidad_reportes

    def calcular_costo_base(self):
        # calcula el costo basado en los reportes atendidos
        return self.tarifa_base * self.cantidad_reportes