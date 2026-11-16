# excepciones personalizadas para el sistema de Software FJ

class ErrorSistema(Exception):
    # clase base para los errores propios del proyecto
    pass


class ServicioNoDisponibleError(ErrorSistema):
    # se usa cuando un servicio está ocupado, en mantenimiento o inactivo
    def __init__(self, mensaje="El servicio no está disponible en este momento"):
        super().__init__(mensaje)


class CapacidadExcedidaError(ErrorSistema):
    # se usa cuando el cliente pide más personas o equipos de los permitidos
    def __init__(self, mensaje="Se superó el límite de capacidad permitido para este servicio"):
        super().__init__(mensaje)


class ReservaInvalidaError(ErrorSistema):
    # se usa si intentan confirmar o cancelar algo que no corresponde
    def __init__(self, mensaje="La operación sobre la reserva no es válida"):
        super().__init__(mensaje)