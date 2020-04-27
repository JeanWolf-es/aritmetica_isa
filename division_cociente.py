#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:39:41 2020

@author: jeanwolf
"""
# programa para hacer divisiones

print ("Hola Isabel")

divisor = (int(input("Introduce el divisor: ")))
dividendo = (int(input("Introduce el dividendo: ")))
print ("el divisor es: ", divisor)
print ("el dividendo es: ", dividendo)

# aqui muestra el cociente y resto
print("********")
print("El resultado es: ", divmod(divisor, dividendo))
print("********")
print("no olvides que el primer numero es el Resultado y el segundo el Resto")
print("********")
print("elevar a un numero x")
base = (int(input("Introduce la base: ")))
potencia = (int(input("Introduce la potencia: ")))
print("resultado de x elevado a y", base ** potencia)
