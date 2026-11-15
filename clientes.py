# -*- coding: utf-8 -*-
"""
Módulo Clientes - Empresa Software FJ
Desarrollado para la Fase 4 - Componente Práctico UNAD
"""

class Cliente:
    """
    Clase que representa a un cliente de la empresa Software FJ,
    aplicando encapsulación y validaciones estrictas de datos personales.
    """
    def __init__(self, nombre, documento, correo, telefono):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del cliente no puede estar vacío y debe ser texto.")
        self.__nombre = valor.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        doc_str = str(valor).strip()
        if not doc_str.isdigit() or len(doc_str) < 5:
            raise ValueError("El número de documento debe contener solo dígitos y tener al menos 5 caracteres.")
        self.__documento = doc_str

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor:
            raise ValueError(f"El correo '{valor}' no tiene un formato válido.")
        self.__correo = valor.strip()

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        tel_str = str(valor).strip()
        if not tel_str.isdigit() or len(tel_str) < 7:
            raise ValueError("El teléfono debe contener solo dígitos y un mínimo de 7 números.")
        self.__telefono = tel_str

    def __str__(self):
        return f"Cliente: {self.__nombre} | Documento: {self.__documento} | Correo: {self.__correo}"
    