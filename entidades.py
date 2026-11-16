# clase base abstracta para los servicios de Software FJ

# herramientas de Python para crear clases abstractas

from abc import ABC, abstractmethod  

class Servicio(ABC): 
    
    def __init__(self, nombre_servicio, tarifa_base):
        # constructor que guarda los datos iniciales del servicio
        self.nombre_servicio = nombre_servicio
        self.tarifa_base = tarifa_base

    @abstractmethod  
    def calcular_costo_base(self):
        pass

    def __str__(self):
        # nos devuelve un texto limpio al imprimir el objeto en consola
        return f"Servicio: {self.nombre_servicio} | Tarifa Base: ${self.tarifa_base}"