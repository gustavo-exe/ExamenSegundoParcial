# -*- coding: utf-8 -*-
#Programa:estacionamiento.py
#LinkGIT:https://github.com/gustavo-exe/ExamenSegundoParcial.git
#Objetivo: Hacer los calculos respectivos para el stacionamiento
#Fecha:13/marzo/2020

from datetime import datetime, timedelta
from vehiculo import Vehiculo
import random 

class Estacionamiento:
    """
    Contendra los calculos necesarios para
    el vehiculo
    """
    def __init__(self):
        """
        Lista de vehiculos.
        """
        self.estacionamiento = list()

    def nuevo_vehiculo(self,marca,modelo,tipo,numero):
        """
        Insertar un nuevo vehiculo
        """
        self.estacionamiento.append(Vehiculo(marca,modelo,tipo,numero))


    def tarifa(self,vehiculo_id):
        """
        La tarifa por hora o fracción que la empresa maneja es la siguiente:
        1. Automóvil: L 20.00 la primera hora o fraccción. Cada hora adicional tiene un descuento del 20%
        por cada hora. Los descuentos no son acumulables.
        2. Motocicleta: L 10.00 la primera hora o fracción. Cada hora adicional tiene un descuento del 10%
        por cada hora. Los descuentos no son acumulables.
        """
        tiempo = self._numero_aletorio()

        for indice in self.estacionamiento:
            if str(indice.id) == str(vehiculo_id):
                if str(indice.tipo) == str("Automovil"):
                    print("\n Marca: {0} \nModelo: {1} \nTipo: {2}\nNumero: {3}"
                        .format(indice.marca, indice.modelo, indice.tipo, indice.numero_de_placa))
                        print("Tarifa: {0}".format(tiempo*10)) 
                elif str(indice.tipo) == str("Motocicleta"):
                    print("\n Marca{0} \nModelo{1} \nTip0{2}\nNumero"
                        .format(indice.marca, indice.modelo, indice.tipo, indice.numero_de_placa))
                    print("Tarifa: {0}".format(tiempo*10))    


    def _numero_aletorio(self):
        """
        Retorna un numero aleatorio
        """        
        randx = random.randint(0,5)
        return randx

    def _simular_tiempo(self):
        """
        Generar tiempo.
        """
        random = self._numero_aletorio()
        plus_five_hours = datetime.now() + timedelta(hours= random)
        return plus_five_hours



    def salida_de_vehiculo(self,id_vehiculo):
        """
        Al momento de la salida de un cliente en su vehículo, se genera un ticket de salida que muestra un
        resumen del total de las hora(s) o fracción que el cliente estuvo en el estacionamiento y el total a pagar.
        El estado del ingreso se convierte el false.
        """
        tiempo= self._simular_tiempo()

        for indice in self.estacionamiento:
            if str(indice.id) == str(id_vehiculo):
                indice.estado = False
                print("\nPlaca: {0}\nHora de dentrada:{1}"
                        .format(indice.numero_de_placa, indice.hora))
                print("\nHora de salida:{0}".format(tiempo))







        
