# -*- coding: utf-8 -*-
#Programa:menu.py
#LinkGIT:https://github.com/gustavo-exe/ExamenSegundoParcial.git
#Objetivo: Generar las funciones par ael objeto
#Fecha:13/marzo/2020

import sys
import platform
import os

from estacionamiento import Estacionamiento
class Menu:

    def __init__(self):
        """
        diccionario para el progarama
        """
        self.carro = Estacionamiento()
        self.options ={ "1": self.new_vehiculo,
                        "2": self.tarifa,
                        "3": self.salida_vehiculo
                        }

    def desplegar_menu(self):
        """
        Ver menu de opciones para el estacionamiento
        """
        print("""
                E S T A C I O N A M I E N T O
                1.Ingreso de un vehiculo
                2.Tarifa
                3.Salida de vehiculo
                """) 

    def press_enter(self):
        """Realizar una pausa y solicitar presionar una tecla"""
        input("\n Presiona ENTER para continuar")

    def new_vehiculo(self):
        """
        Ingreso de un nuevo vehiculo
        """
        print("...Ingrese un nuevo vehiculo...")
        numero= input("Ingrese numero de placa:")
        marca = input("Ingrese la marca: ")
        modelo = input("Ingrese el modelo:")
        tipo = input("Tipo de vehiculo:")
        
        self.carro.nuevo_vehiculo(marca,modelo,tipo,numero)
        print("Insertaste un nuevo vehiculo.")
        self.press_enter()


    def tarifa(self):
        """
        Me devuelve mi vehiculo con la tarifa ya aplicada
        """

        id = input("Ingrese el id del vehiculo que quiere buscar: ")
        self.carro.tarifa(id)


    def salida_vehiculo(self):
        """
        Se muestra el ticket del vehiculo que va salir
        """
        id = input ("Id del vehiculo que va salir: ")
        self.carro.salida_de_vehiculo(id)



    def run(self):
        while True:
            self.desplegar_menu()
            choise = input("Ingrese una opcion:")
            action = self.options.get(choise)

            if action:
                action()
            else:
                print("{0} Opcion no valida".format(choise))


if __name__ == "__main__":
    menu = Menu()
    menu.run()



