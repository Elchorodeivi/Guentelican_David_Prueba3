import os
import time
import numpy as np
import random

def grabar():
    t = True
    while t == True:
        os.system("cls")
        tipo = str(input("Ingrese el tipo de vehículo:\n"))
        if len(tipo) > 0:
            t = False
        else:
            print("Ingrese un dato válido.")
    pat = True
    while pat == True:
        os.system("cls")
        patente = str(input("Ingrese la patente del vehículo:\n"))
        if len(patente) == 6:
            pat = False
        else:
            print("Ingrese un dato válido.")
    mar = True
    while mar == True:
        os.system("cls")
        marca = str(input("Ingrese la marca del vehículo:\n"))
        if len(marca) >= 2 and len(marca) <= 15:
            mar = False
        else:
            print("La marca excede los caracteres permitidos.")
    pre = True
    while pre == True:
        os.system("cls")
        precio = int(input("Ingrese el precio del vehículo:\n"))
        if precio >= 5000000:
            pre = False
        else:
            print("La marca excede los caracteres permitidos.")
    mul = True
    while mul == True:
        os.system("cls")
        multa = int(input("¿El vehículo tiene multa?\n1. Sí\n2. No\n"))
        if multa == 1:
            os.system("cls")
            valor_multa = int(input("Ingrese el valor de la multa:\n"))
            os.system("cls")
            fecha_multa = str(input("Ingrese la fecha de la multa:\n"))
            mul = False
        elif multa == 2:
            valor_multa = 0
            fecha_multa = "null"
            mul = False
        else:
            print("Ingrese una opción válida.")
    r = True
    while r == True:
        os.system("cls")
        fecha_registro = str(input("Ingrese la fecha de registro del vehículo:\n"))
        r = False
    d = True
    while d == True:
        os.system("cls")
        dueño = str(input("Ingrese el nombe y apellido del dueño del vehículo:\n"))
        d = False
        registro = [tipo, patente, marca, precio, valor_multa, fecha_multa, fecha_registro, dueño]
    return(registro)

def buscar(buscar_patente, database):
    base1 = np.array(database)
    for f in range(len(base1)):
        if base1[f][1] == buscar_patente:
            print(f"Tipo de auto: {base1[f, 0]}")
            print(f"Patente: {base1[f, 1]}")
            print(f"Marca del auto: {base1[f, 2]}")
            print(f"Precio: {base1[f, 3]}")
            print(f"Valor de la multa: {base1[f, 4]}")
            print(f"Fecha de la multa: {base1[f, 5]}")
            print(f"Fecha de registro: {base1[f, 6]}")
            print(f"Dueño: {base1[f, 7]}")
            
def imprimir(database):
    costo_certificado = [[0], [0]]
    for fila in range (1):
        for columna in range (1):
            costo_certificado[fila][columna] = random.randint(1500, 3500)
    print("Certificados disponibles:\n")
    print("1. Emisión de contaminantes")
    print("1. Anotaciones vigentes")
    print("1. Multas")
    certificado = int(input("Seleccione una opción:\n"))
    if certificado == 1:
        base2 = np.array(database)
        for f in range(len(base2)):
            if base2[f][1]:
                print(f"Certificado de Emisión de Contaminantes")
                print(f"Patente: {base2[f, 1]}")
                print(f"Dueño: {base2[f, 7]}\n")
                print(f"Valor certificado: {costo_certificado}")
    elif certificado == 2:
        base2 = np.array(database)
        for f in range(len(base2)):
            if base2[f][1]:
                print(f"Certificado de Anotaciones Vigentes")
                print(f"Patente: {base2[f, 1]}")
                print(f"Dueño: {base2[f, 7]}\n")
                print(f"Valor certificado: {costo_certificado}")
    elif certificado == 3:
        base2 = np.array(database)
        for f in range(len(base2)):
            if base2[f][1]:
                print(f"Certificado de Multas")
                print(f"Patente: {base2[f, 1]}")
                print(f"Dueño: {base2[f, 7]}\n")
                print(f"Valor de la multa: {base2[f, 4]}")
                print(f"Fecha de la multa: {base2[f, 5]}")
                print(f"Valor certificado: {costo_certificado}")
                
def salir():
    menu = True
    os.system('cls')
    salida = int(input("¿Desea salir del Menú?\n1. Sí\n2. No"))
    if salida == 1:
        menu = False
    else:
        menu = True