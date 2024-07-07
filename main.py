# Archivo principal:/ ISI 1K03 AyED 2024 - Cabrera Martín, Delgado Mauro, Rodriguez Lautaro, Rossi Dariana
# -*- coding: utf-8 -*-
"""
INT:
intentos_restantes, sesion,
opcion, opcion_perfil, opcion_editar, opcion_candidatos,
porcentaje1, porcentaje2, porcentaje3, porcentaje_total, random,
ano_actual, mes_actual, dia_actual,
ano_nacimiento1, mes_nacimiento1, dia_nacimiento1, estudiante1_edad,
ano_nacimiento2, mes_nacimiento2, dia_nacimiento2, estudiante2_edad,
ano_nacimiento3, mes_nacimiento3, dia_nacimiento3, estudiante3_edad

STRING:
estudiante1_email, estudiante2_email, estudiante3_email,
estudiante1_contrasena, estudiante2_contrasena, estudiante3_contrasena,
estudiante1_nombre, estudiante2_nombre, estudiante3_nombre,
estudiante1_nacimiento, estudiante2_nacimiento, estudiante3_nacimiento,
estudiante1_hobbies, estudiante2_hobbies, estudiante3_hobbies,
estudiante1_bio, estudiante2_bio, estudiante3_bio,
email, contrasena,
me_gusta, me_gusta1, me_gusta2, me_gusta3
"""

from datetime import datetime
from random   import randint
from getpass  import getpass
import os


def LIMPIAR_CONSOLA():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # macOS y Linux
		os.system('clear')

def MENU_PRINCIPAL():
	print("Menu Principal")
	print("\t1.  Gestionar mi perfil")
	print("\t2.  Gestionár candidatos")
	print("\t3.  Matcheos")
	print("\t4.  Reportes estadisticos")
	print("\t11. Ruleta de afinidad")
	print("\t0. Salir \n")

	return int(input("Seleccione la opcion: "))

def MENU_GESTION_PERFIL():
	print("Menu de Gestion de Perfil")
	print("\t1. Editar mis datos personales")
	print("\t2. Eliminar mi perfil")
	print("\t0. Volver\n")

	return int(input("Seleccione la opcion: "))

def MENU_GESTION_CANDIDATOS():
	print("Menu de gestion de candidatos")
	print("\t1. Ver candidatos")
	print("\t1. Reportar un candidato")
	print("\t0. Volver\n")

	return int(input("Seleccione la opcion: "))

def MENU_MATCHEOS():
	print("Menu de gestion de candidatos")
	print("\t1. Ver matcheos")
	print("\t2. Eliminar un matcheo")
	print("\t0. Volver\n")

	return int(input("Seleccione la opcion: "))

def CALCULAR_EDAD(nacimiento):
	ano_actual = datetime.now().year
	mes_actual = datetime.now().month
	dia_actual = datetime.now().day

	ano_nacimiento = int(nacimiento[:4])
	mes_nacimiento = int(nacimiento[5:7])
	dia_nacimiento = int(nacimiento[8:])

	edad = ano_actual - ano_nacimiento
	if(mes_nacimiento > mes_actual):
		edad = edad - 1
	elif(mes_nacimiento == mes_actual):
		if(dia_nacimiento > dia_actual):
			edad = edad - 1
	return edad

def MOSTRAR_DATOS_ESTUDIANTES():
	for n in range(cant_estudiantes):
		if(sesion != n):
			print("Estudiante",n)
			print("Nombre:", estudiantes[n][2])
			print("Fecha de Nacimiento:", estudiantes[n][3])
			print("Edad:", CALCULAR_EDAD(estudiantes[1][3]))
			print("Biografia:", estudiantes[n][5])
			print("Hobbies: {} \n" .format(estudiantes[n][4]))

def RULETA_AFINIDAD():
	porcentaje_total = -1 
	while(porcentaje_total != 100):
		porcentaje1 = int(input("Porcentaje de afinidad con la persona A: "))
		porcentaje2 = int(input("Porcentaje de afinidad con la persona B: "))
		porcentaje3 = int(input("Porcentaje de afinidad con la persona C: "))
		porcentaje_total = porcentaje1 + porcentaje2 + porcentaje3
		
		if(porcentaje_total != 100):
			LIMPIAR_CONSOLA()
			print("Los porcentajes no suman 100!!! Ingreselos nuevamente. \n")
	
	random = randint(0, 99)
	
	LIMPIAR_CONSOLA()

	if(random < porcentaje1):
		print("Salió la persona A!!!\n")
	elif(random < porcentaje1 + porcentaje2):
		print("Salió la persona B!!!\n")
	else: 
		print("Salió la persona C!!!\n")

def NOMBRE_CORRECTO(nombre):
	correcto = False;
	est = 0;
	while(not correcto and est < cant_estudiantes):
		if(nombre == estudiantes[est][2].lower()):
			if(est != sesion):
				correcto = True
			else:
				print("No puedes seleccionarte a ti mismo!\n")
				est = cant_estudiantes
		est = est + 1
	return correcto;

def EDITAR_DATOS():
	print("¿ Que desea editar ?")
	print("\t1. fecha de nacimiento")
	print("\t2. biografia")
	print("\t3. hobbies\n")
	opcion_editar = int(input("Selecciona la opcion: "))
	LIMPIAR_CONSOLA()
	match opcion_editar:
		case 1:
			estudiantes[sesion][3] = input("Formato (año-mes-dia) \nxxxx-xx-xx \nIngrese una nueva fecha: ")	
			LIMPIAR_CONSOLA()
		case 2:
			estudiantes[sesion][5] = input("Ingrese una nueva biografia: ")
			LIMPIAR_CONSOLA()
		case 3:
			estudiantes[sesion][4] = input("Ingrese un nuevo hobbie: ")
			LIMPIAR_CONSOLA()
		case _: 
			LIMPIAR_CONSOLA()
			print("Opción incorrecta.\n")

estudiantes = [[""]*9 for n in range(8)] # email | contrasena | nombre | nacimiento | hobbies | bio | sexo | gusto | estado
admins = [[""]*2 for n in range(4)] # email | contrasena
# Para probar más rápido un mail válido es a y su contraseña es 1
estudiantes[0][0] = "a"; estudiantes[0][1] = "1"; estudiantes[0][2] = "Juliancito"; estudiantes[0][3] = "2006-01-07"; estudiantes[0][4] = "pescar, nadar";
estudiantes[1][0] = "estudiante2@ayed.com"; estudiantes[1][1] = "333444"; estudiantes[1][2] = "Pedrito"; estudiantes[1][3] = "2005-04-10"; estudiantes[1][4] = "comer, jugar";
estudiantes[2][0] = "estudiante3@ayed.com"; estudiantes[2][1] = "555666"; estudiantes[2][2] = "Anita"; estudiantes[2][3] = "2004-10-20"; estudiantes[2][4] = "leer sobre jojos";
cant_estudiantes = 3

sesion = -1
intentos_restantes = 3

LIMPIAR_CONSOLA()

while(sesion == -1 and intentos_restantes > 0):
	email = input("Ingrese su email: ").lower() # El .lower es para forzar minusculas
	contrasena = getpass("Ingrese su contraseña: ")

	LIMPIAR_CONSOLA()

	intentos_restantes = intentos_restantes - 1

	est = 0
	while(sesion == -1 and est < cant_estudiantes):
		if(email == estudiantes[est][0] and contrasena == estudiantes[est][1]):
			print("Felicidades",estudiantes[est][2],"ingresaste!\n")
			sesion = est
		est = est + 1
	if(sesion == -1):
		print("No ingresaste correctamente :(\n")
		print("Te quedan ",intentos_restantes,"intentos.")

opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
while(sesion > -1 and opcion != 0):

	opcion = MENU_PRINCIPAL()
	LIMPIAR_CONSOLA()
	match opcion:
		case 1:
			opcion_perfil = MENU_GESTION_PERFIL()
			match opcion_perfil:
				case 1:
					LIMPIAR_CONSOLA()
					EDITAR_DATOS() 
				case _: 
					LIMPIAR_CONSOLA()
					print("Opción incorrecta.\n")

		case 2:
			opcion_candidatos = MENU_GESTION_CANDIDATOS()
			match opcion_candidatos:
				case 1:
					LIMPIAR_CONSOLA()
					MOSTRAR_DATOS_ESTUDIANTES()
					me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
					LIMPIAR_CONSOLA()
					if(NOMBRE_CORRECTO(me_gusta.lower())):	
						estudiantes[sesion][7] = me_gusta
						print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
					else:
						print("El nombre ingresado no es correcto\n")
				case _: 
					LIMPIAR_CONSOLA()
					print("Opción incorrecta.\n")		
		case 3:
			opcion_matcheo = MENU_MATCHEOS()
			print("En construcción...\n")
		case 4:
			print("En construcción...\n")
		case 11:
			RULETA_AFINIDAD()

		case 0:
			print("\nPrograma terminado.")
		case _:
			print("Opcion incorrecta")	
