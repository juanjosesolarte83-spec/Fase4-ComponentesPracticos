
"""
Módulo Reservas - Empresa Software FJ
Desarrollado para la Fase 4 - Componente Práctico UNAD
"""

class Reserva:
    """
    Clase que integra cliente, servicio, duración y estado de la reserva,
    implementando confirmación, cancelación y métodos sobrecargados de costos.
    """
    def __init__(self, cliente, servicio, duracion_horas):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "Pendiente"

    @property
    def duracion_horas(self):
        return self.__duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La duración en horas debe ser un número mayor a cero.")
        self.__duracion_horas = valor

    def confirmar_reserva(self):
        """Cambia el estado de la reserva a Confirmada."""
        self.estado = "Confirmada"
        return f"Reserva confirmada exitosamente para el cliente {self.cliente.nombre}."

    def cancelar_reserva(self):
        """Cambia el estado de la reserva a Cancelada."""
        self.estado = "Cancelada"
        return f"La reserva del cliente {self.cliente.nombre} ha sido cancelada."

    def calcular_costo(self):
        """Cálculo base del costo utilizando la duración y la tarifa base del servicio."""
        return self.servicio.calcular_costo_base() * self.duracion_horas

    def calcular_costo_con_parametros(self, descuento_porcentaje=0.0, incluye_impuesto=True):
        """
        Método sobrecargado/flexible que permite aplicar un porcentaje de descuento
        y opcionalmente sumar impuestos corporativos (IVA del 19%).
        """
        costo_base = self.calcular_costo()

        if descuento_porcentaje > 0:
            if not (0 <= descuento_porcentaje <= 100):
                raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
            costo_base = costo_base * (1 - (descuento_porcentaje / 100))

        if incluye_impuesto:
            costo_base = costo_base * 1.19

        return round(costo_base, 2)

    def __str__(self):
        costo_total = self.calcular_costo_con_parametros()
        return (f"Reserva [Estado: {self.estado}] - Cliente: {self.cliente.nombre} | "
                f"Servicio: {self.servicio.nombre_servicio} | Duración: {self.duracion_horas}h | "
                f"Costo Total: ${costo_total}")
    