# -*- coding: utf-8 -*-
#Programa:vehiculo.py
#LinkGIT:https://github.com/gustavo-exe/ExamenSegundoParcial.git
#Objetivo: Crear el obejto vehiculo con sus propiedades
#Fecha:13/marzo/2020
import datetime
last_id = 0
class Vehiculo:
    def __init__(self,marca,modelo,tipo, numero = ""):
        """
        Al momento del ingreso de un cliente en su vehículo se toman los
        siguientes datos
        """
        self.numero_de_placa = numero
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.hora = datetime.date.today()
        self.estado = True
        global last_id
        last_id += 1
        self.id = last_id

