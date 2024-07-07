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

def MOSTRAR_DATOS_ESTUDIANTES():
	# Calcular la edad de cada estudiante. Esto en el futuro podria ser una funcion aparte
	ano_actual = datetime.now().year
	mes_actual = datetime.now().month
	dia_actual = datetime.now().day

	ano_nacimiento_1 = int(estudiante1_nacimiento[:4])
	mes_nacimiento_1 = int(estudiante1_nacimiento[5:7])
	dia_nacimiento_1 = int(estudiante1_nacimiento[8:])

	ano_nacimiento_2 = int(estudiante2_nacimiento[:4])
	mes_nacimiento_2 = int(estudiante2_nacimiento[5:7])
	dia_nacimiento_2 = int(estudiante2_nacimiento[8:])

	ano_nacimiento_3 = int(estudiante3_nacimiento[:4])
	mes_nacimiento_3 = int(estudiante3_nacimiento[5:7])
	dia_nacimiento_3 = int(estudiante3_nacimiento[8:])

	estudiante1_edad = ano_actual - ano_nacimiento_1
	if(mes_nacimiento_1 > mes_actual):
		estudiante1_edad = estudiante1_edad - 1
	elif(mes_nacimiento_1 == mes_actual):
		if(dia_nacimiento_1 > dia_actual):
			estudiante1_edad = estudiante1_edad - 1

	estudiante2_edad = ano_actual - ano_nacimiento_2
	if(mes_nacimiento_2 > mes_actual):
		estudiante2_edad = estudiante2_edad - 1
	elif(mes_nacimiento_2 == mes_actual):
		if(dia_nacimiento_2 > dia_actual):
			estudiante2_edad = estudiante2_edad - 1

	estudiante3_edad = ano_actual - ano_nacimiento_3
	if(mes_nacimiento_3 > mes_actual):
		estudiante3_edad = estudiante3_edad - 1
	elif(mes_nacimiento_3 == mes_actual):
		if(dia_nacimiento_3 > dia_actual):
			estudiante3_edad = estudiante3_edad - 1

	# Mostrar los estudiantes
	LIMPIAR_CONSOLA()
	if(sesion != 1):
		print("Estudiante 1")
		print("Nombre:", estudiante1_nombre)
		print("Fecha de Nacimiento:", estudiante1_nacimiento)
		print("Edad:", estudiante1_edad)
		print("Biografia:", estudiante1_bio)
		print("Hobbies: {} \n" .format(estudiante1_hobbies))

	if(sesion != 2):
		print("Estudiante 2")
		print("Nombre:", estudiante2_nombre)
		print("Fecha de Nacimiento:", estudiante2_nacimiento)
		print("Edad:", estudiante2_edad)
		print("Biografia:", estudiante2_bio)
		print("Hobbies: {} \n" .format(estudiante2_hobbies))
	
	if(sesion != 3):
		print("Estudiante 3")
		print("Nombre:", estudiante3_nombre)
		print("Fecha de Nacimiento:", estudiante3_nacimiento)
		print("Edad:", estudiante3_edad)
		print("Biografia:", estudiante3_bio)
		print("Hobbies: {} \n" .format(estudiante3_hobbies))

estudiantes = [[""]*6 for n in range(8)] # email |contrasena | nombre |nacimiento |hobbies | bio
admins = [[""]*2 for n in range(4)] # email |contrasena

# Para probar más rápido un mail válido es a y su contraseña es 1
estudiantes[0][0] = "a"; estudiantes[0][1] = "1"; estudiantes[0][2] = "Juliancito"; estudiantes[0][3] = "2006-01-07"; estudiantes[0][4] = "pescar, nadar"; estudiantes[0][5] = ""
estudiantes[1][0] = "estudiante2@ayed.com"; estudiantes[1][1] = "333444"; estudiantes[1][2] = "Pedrito"; estudiantes[1][3] = "2005-04-10"; estudiantes[1][4] = "comer, jugar"; estudiantes[1][5] = ""
estudiantes[2][0] = "estudiante3@ayed.com"; estudiantes[2][1] = "555666"; estudiantes[2][2] = "Anita"; estudiantes[2][3] = "2004-10-20"; estudiantes[2][4] = "leer sobre jojos"; estudiantes[2][5] = ""
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
			sesion = est + 1
	if(sesion == -1):
		print("No ingresaste correctamente :(\n")
		print("Te quedan ",intentos_restantes,"intentos.")

opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
while(sesion > -1 and opcion != 0):

	MENU_PRINCIPAL()
	opcion = int(input("Seleccione la opcion: "))
	LIMPIAR_CONSOLA()

	match opcion:
		case 1:
			print("Menu de Gestión de Perfil")
			print("\t1. Editar mis datos personales\n")
			opcion_perfil = int(input("Seleccione una opcion: "))
			match opcion_perfil:
				case 1:
					LIMPIAR_CONSOLA()
					print("¿ Que desea editar ?")
					print("\t1. fecha de nacimiento")
					print("\t2. biografia")
					print("\t3. hobbies\n")
					opcion_editar = int(input("Selecciona la opcion: "))
					LIMPIAR_CONSOLA()
					match opcion_editar:
						case 1:
							match sesion:
								case 1:
									estudiante1_nacimiento = input("Formato (año-mes-dia) \nxxxx-xx-xx \nIngrese una nueva fecha: ")
								case 2:
									estudiante2_nacimiento = input("Formato (año-mes-dia) \nxxxx-xx-xx \nIngrese una nueva fecha: ")
								case 3:
									estudiante3_nacimiento = input("Formato (año-mes-dia) \nxxxx-xx-xx \nIngrese una nueva fecha: ")
								
							LIMPIAR_CONSOLA()

						case 2:
							match sesion:
								case 1:
									estudiante1_bio = input("Ingrese una nueva biografia: ")
								case 2:
									estudiante2_bio = input("Ingrese una nueva biografia: ")
								case 3:
									estudiante3_bio = input("Ingrese una nueva biografia: ")
								
							LIMPIAR_CONSOLA()
						
						case 3:
							match sesion:
								case 1:
									estudiante1_hobbies = input("Ingrese un nuevo hobbie: ")
								case 2:
									estudiante2_hobbies = input("Ingrese un nuevo hobbie: ")
								case 3:
									estudiante3_hobbies = input("Ingrese un nuevo hobbie: ")
							
							LIMPIAR_CONSOLA()

						case _: 
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")



				case _: 
					LIMPIAR_CONSOLA()
					print("Opción incorrecta.\n")

		case 2:
			print("Menu de gestion de candidatos")
			print("\t1. Ver candidatos\n")
			opcion_candidatos = int(input("Seleccione la opcion: "))
			match opcion_candidatos:
				case 1:
					MOSTRAR_DATOS_ESTUDIANTES()
					me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ").lower()
					LIMPIAR_CONSOLA()
					if(me_gusta == estudiante1_nombre.lower() or me_gusta == estudiante2_nombre.lower() or me_gusta == estudiante3_nombre.lower()):	
						if(sesion==1 and estudiante1_nombre.lower() != me_gusta):
							me_gusta1 = me_gusta
							print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
						elif(sesion==2 and estudiante2_nombre.lower() != me_gusta):
							me_gusta2 = me_gusta 
							print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
						elif(sesion==3 and estudiante3_nombre.lower() != me_gusta):
							me_gusta3 = me_gusta
							print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
						else:
							print("No puedes seleccionarte a ti mismo!\n")
					else:
						print("El nombre ingresado no es correcto\n")
				case _: 
					LIMPIAR_CONSOLA()
					print("Opción incorrecta.\n")		
			
			
		case 3:
			LIMPIAR_CONSOLA()
			print("En construcción...\n")
		case 4:
			LIMPIAR_CONSOLA()
			print("En construcción...\n")
		case 11:
			LIMPIAR_CONSOLA()
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

		case 0:
			LIMPIAR_CONSOLA()
			print("\nPrograma terminado.")
		case _:
			LIMPIAR_CONSOLA()
			print("Opcion incorrecta")	
