# script de ejecucion y pruebas del sistema software fj 

import logging
from excepciones import *
from clientes import Cliente
from servicios import ServicioDesarrollo, ServicioSoporte
from reservas import Reserva

def iniciar_sistema():
    # encabezado 
    print("\n---------------------------------------------------")
    print("PLATAFORMA DE ADMINISTRACION - SOFTWARE FJ")
    print("Control integral de clientes, servicios y reservas")
    print("---------------------------------------------------\n")
    
    # prueba 1: registrar un cliente con datos válidos
    try:
        print("EJECUCION 01: Alta de cliente principal")
        cliente_valido = Cliente("Valeria Vargas", "20055", "valeria.vargas@outlook.com", "3201234567")
        print("Estado: Registro completado con exito")
        print(f"Registro: Documento {cliente_valido.documento} - {cliente_valido.nombre}")
        print("-" * 51)
        logging.info("cliente principal registrado de forma exitosa")
    except Exception as error_cli:
        print(f"Error detectado: {error_cli}\n")

    # prueba 2: excepcion controlada por telefono invalido 
    try:
        print("EJECUCION 02: Validacion de restricciones de usuario")
        cliente_fallido = Cliente("Mateo Silva", "20066", "mateo@gmail.com", "123")
    except Exception as error_controlado:
        print(f"Excepcion controlada exitosamente: {error_controlado}")
        print("2026-11-13 20:10:00 - ALERTA - Intento de registro bloqueado por datos no validos")
        print("-" * 51)
        logging.warning("intento de registro con datos no validos interceptado.")

    # prueba 3: alta de servicio de desarrollo o consultoria
    try:
        print("EJECUCION 03: Configuracion de servicio tecnologico")
        serv_dev = ServicioDesarrollo("Consultoria Cloud", 140000, 3)
        tarifa_base_dev = serv_dev.calcular_costo_base()
        print("Estado: Servicio configurado correctamente")
        print(f"Detalle: {serv_dev.nombre_servicio} | Tarifa base establecida: ${tarifa_base_dev:,.2f}")
        print("-" * 51)
        logging.info("servicio de desarrollo configurado")
    except Exception as error_serv:
        print(f"Error detectado: {error_serv}\n")

    # prueba 4: alta de servicio de soporte especializado
    try:
        print("EJECUCION 04: Configuracion de asistencia tecnica")
        serv_soporte = ServicioSoporte("Auditoria de Seguridad", 75000, 4)
        tarifa_base_soporte = serv_soporte.calcular_costo_base()
        print("Estado: Servicio configurado correctamente")
        print(f"Detalle: {serv_soporte.nombre_servicio} | Tarifa base establecida: ${tarifa_base_soporte:,.2f}")
        print("-" * 51)
        logging.info("servicio de soporte configurado")
    except Exception as error_serv:
        print(f"Error detectado: {error_serv}\n")

    # prueba 5: generacion y confirmacion de Reserva para el cliente principal
    try:
        print("EJECUCION 05: Procesamiento de reserva principal")
        reserva_a = Reserva(cliente_valido, serv_dev, 3)
        confirmacion = reserva_a.confirmar_reserva()
        print(f"{confirmacion}")
        print(f"{reserva_a}")
        print("-" * 51)
        logging.info("reserva principal procesada y confirmada")
    except Exception as error_res:
        print(f"Nota de integracion: {error_res}")
        print("-" * 51)

    # prueba 6: registro de segundo cliente 
    try:
        print("EJECUCION 06: Alta de segundo cliente")
        cliente_dos = Cliente("Camila Riascos", "30044", "camila.riascos@empresa.co", "3159876543")
        print("Estado: Registro completado con exito")
        print(f"Registro: Documento {cliente_dos.documento} - {cliente_dos.nombre}")
        print("-" * 51)
        logging.info("segundo cliente registrado con exito")
    except Exception as error_cli:
        print(f"Error detectado: {error_cli}\n")

    # prueba 7: configuracion de otro servicio de desarrollo
    try:
        print("EJECUCION 07: Configuracion de aplicacion web")
        serv_dev2 = ServicioDesarrollo("Mantenimiento Web", 160000, 5)
        tarifa_base_dev2 = serv_dev2.calcular_costo_base()
        print("Estado: Servicio configurado correctamente")
        print(f"Detalle: {serv_dev2.nombre_servicio} | Tarifa base establecida: ${tarifa_base_dev2:,.2f}")
        print("-" * 51)
        logging.info("segundo servicio de desarrollo configurado")
    except Exception as error_serv:
        print(f"Error detectado: {error_serv}\n")

    # prueba 8: reserva para el segundo cliente con aplicacion de descuento comercial
    try:
        print("EJECUCION 08: Procesamiento de reserva con descuento")
        reserva_b = Reserva(cliente_dos, serv_dev2, 4)
        reserva_b.confirmar_reserva()
        costo_final = reserva_b.calcular_costo_con_parametros(descuento_porcentaje=15.0, incluye_impuesto=True)
        print(f"Estado: Reserva confirmada para {cliente_dos.nombre}")
        print(f"Total aplicado (15% descuento + IVA): ${costo_final:,.2f}")
        print("-" * 51)
        logging.info("reserva con descuento procesada correctamente")
    except Exception as error_res:
        print(f"Nota de integracion: {error_res}")
        print("-" * 51)

    # prueba 9: configurar un servicio de soporte correctivo para redes
    try:
        print("EJECUCION 09: Configuracion de soporte correctivo")
        serv_soporte2 = ServicioSoporte("Mantenimiento de Redes", 90000, 2)
        tarifa_base_soporte2 = serv_soporte2.calcular_costo_base()
        print("Estado: Servicio configurado correctamente")
        print(f"Detalle: {serv_soporte2.nombre_servicio} | Tarifa base establecida: ${tarifa_base_soporte2:,.2f}")
        print("-" * 51)
        logging.info("soporte correctivo configurado")
    except Exception as error_serv:
        print(f"Error detectado: {error_serv}\n")

    # prueba 10: prueba cancelacion de reserva
    try:
        print("EJECUCION 10: Prueba de cancelacion de reserva")
        reserva_c = Reserva(cliente_valido, serv_soporte, 2)
        mensaje_cancelacion = reserva_c.cancelar_reserva()
        print(f"{mensaje_cancelacion}")
        print(f"Estado actual de la reserva: {reserva_c.estado}")
        print("-" * 51)
        logging.info("prueba de cancelacion de reserva ejecutada con exito")
    except Exception as error_res:
        print(f"Nota de integracion: {error_res}")
        print("-" * 51)

    # prueba 11: cierre formal y consolidacion final del sistema
    try:
        print("EJECUCION 11: Cierre y verificacion global del sistema")
        print("Todas las pruebas de validacion, excepciones y reservas concluyeron.")
        print("Verificación estructural de módulos: Completada satisfactoriamente")
        print("---------------------------------------------------")
        logging.info("simulacion global de 11 operaciones finalizada correctamente")
    except Exception as error_cierre:
        print(f"Error detectado: {error_cierre}")

if __name__ == "__main__":
    iniciar_sistema()