# -*- coding: utf-8 -*-
from clientes import Cliente
from reservas import Reserva

print("--- PROBANDO EL SISTEMA DE SOFTWARE FJ ---")

try:
    # 1. Crear un cliente válido
    cliente1 = Cliente("Ana Maria Perez", "12345678", "ana.perez@email.com", "3101234567")
    print("Cliente creado con éxito:", cliente1)

    # Simulación de un servicio básico temporal para probar la reserva
    class ServicioMock:
        def __init__(self, nombre, tarifa):
            self.nombre_servicio = nombre
            self.tarifa_base = tarifa
        def calcular_costo_base(self):
            return self.tarifa_base

    servicio_prueba = ServicioMock("Asesoría Especializada", 50000)

    # 2. Crear una reserva
    reserva1 = Reserva(cliente1, servicio_prueba, 3)
    print("Reserva creada con éxito:", reserva1)

    # 3. Probar métodos de costos
    costo_con_impuesto = reserva1.calcular_costo_con_parametros(descuento_porcentaje=10.0, incluye_impuesto=True)
    print(f"Costo calculado (con 10% descuento e IVA): ${costo_con_impuesto}")

    print("\n ¡Todas las pruebas pasaron sin errores!")

except Exception as e:
    print("Ocurrió un error inesperado:", e)
    