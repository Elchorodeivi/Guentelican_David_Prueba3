from funciones import grabar, buscar, imprimir, salir
import os
import time
import numpy as np

menu = True
database = []
try:
    while menu == True:
        os.system("cls")
        print("Bienvenido al Menú de la Automotora AUTO SEGURO")
        print("Ingrese una opción:\n")
        opcion = int(input("1. Ingresar datos de vehículos\n2. Buscar vehículo\n3. Imprimir certificados\n4. Salir del programa\n"))
        if opcion == 1:
            database.append(grabar())
        elif opcion == 2:
            buscar_patente = input("Ingrese la patente a buscar:\n")
            buscar(buscar_patente, database)
            menu = False
        elif opcion == 3:
            imprimir(database)
        elif opcion == 4:
            salir()
except:
    print("Error, vuelva a intentar.")