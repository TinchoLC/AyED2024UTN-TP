# Archivo principal:/ ISI 1K03 AyED 2024 - Cabrera Martín, Delgado Mauro, Rodriguez Lautaro, Rossi Dariana
# -*- coding: utf-8 -*-
"""
arreglar 	LEER GUÍA DE PREGUNTAS (AGREGAR NUEVAS VARIABLES)

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

# BASICO
def LIMPIAR_CONSOLA():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # macOS y Linux
		os.system('clear')

def LIKES_AUTO():
	likes = [[0]*8 for n in range(8)] #Aca se rellena al 100% con 0
	for i in range(8):
		for j in range (8):
			likes[i][j] = randint(0,1) 

	return likes

# INICIO
def MENU_INICIO():
	print("INICIO")
	print("\t1. Login")
	print("\t2. Registrarse")
	print("\t11.Bonus Track 1.1 (Ruleta)")
	print("\t21.Bonus Track 2.1 (Edades)")
	print("\t22.Bonus Track 2.2 (Matcheos combinados)")
	print("\t0. Salir \n")

	return int(input("Seleccione la opcion: "))

def LOGIN():
	LIMPIAR_CONSOLA()
	sesion = -1
	sesion_adm = -1
	intentos_restantes = 3
	while(sesion == -1 and intentos_restantes > 0):
		print("LOGIN\n")
		email = input("Ingrese su email: ").lower() # El .lower es para forzar minusculas
		contrasena = getpass("Ingrese su contraseña: ")

		LIMPIAR_CONSOLA()

		intentos_restantes = intentos_restantes - 1

		probable = 0
		while(sesion == -1 and sesion_adm == -1 and probable < cant_estudiantes):
			if(email == estudiantes[probable][0] and contrasena == estudiantes[probable][1]):
				intentos_restantes = 0

				if(estudiantes[probable][7]):
					print("Felicidades",estudiantes[probable][2],"ingresaste!\n")
					sesion = probable
				else: 
					print("Su cuenta ha sido deshabilitada\n")
					probable = cant_estudiantes
			elif(probable < cant_admins): # no todo dentro del mismo if porque si no busca más allá del array.
				if(email == admins[probable][0] and contrasena == admins[probable][1]):
					intentos_restantes = 0
					sesion_adm = probable

			probable = probable + 1

		if(intentos_restantes > 0):
			print("No ingresaste correctamente :(")
			print("Te quedan ",intentos_restantes,"intentos.\n")

	return sesion, sesion_adm

def REGISTRO(nueva_sesion):
	LIMPIAR_CONSOLA()
	if(nueva_sesion < 8):
		print("REGISTRO\n")
		email = input("Ingrese un email: ")
		nombre = input("Ingrese un nombre: ")
		for n in range(cant_estudiantes):
			if(email == estudiantes[n][0]):
				email = "novalido"
			elif(n < cant_admins): # no todo dentro del mismo if porque si no busca más allá del array.
				if(email == admins[n][0]):
					email = "novalido"
			if(nombre.lower() == estudiantes[n][2].lower()):
				nombre = "novalido"

		if(email == "novalido"):
			print("\nEl email ya está siendo utilizado o no es válido")
		elif(nombre == "novalido"):
			print("\nEl nombre ya está siendo utilizado o no es válido")
		else:
			estudiantes[nueva_sesion][0] = email
			estudiantes[nueva_sesion][2] = nombre
			estudiantes[nueva_sesion][1] = input("Ingrese la contraseña: ")
			estudiantes[nueva_sesion][3] = INGRESAR_NACIMIENTO()
			estudiantes[nueva_sesion][7] = 1
			nueva_sesion = nueva_sesion + 1
			print(nombre, "registrado!")
	else:
		print("Ya se alcanzó el máximo de estudiantes")

	return nueva_sesion

# MENUS MODERADOR
def MENU_PRINCIPAL_MODERADOR(id):
	print("Menu Principal del moderador con id",id)
	print("\t1. Gestionar usuarios")
	print("\t2. Gestionar Reportes")
	print("\t3. Reportes Estadísticos")
	print("\t0.  Salir \n")

	return int(input("Seleccione la opcion: "))

def MENU_GESTION_USUARIOS():
	print("Menu de Gestion de Usuarios")
	print("\ta. Desactivar usuario")
	print("\tb. Volver\n")

	return input("Seleccione la opcion: ")

def MENU_GESTION_REPORTES():
	print("Menu de Gestion de Reportes")
	print("\ta. Ver reportes")
	print("\tb. Volver\n")

	return input("Seleccione la opcion: ")

# MENUS ESTUDIANTE
def MENU_PRINCIPAL_ESTUDIANTE(id, nombre):
	print("Menu Principal del estudiante",nombre,"con id",id)
	print("\t1.  Gestionar mi perfil")
	print("\t2.  Gestionár candidatos")
	print("\t3.  Matcheos")
	print("\t4.  Reportes estadísticos")
	print("\t0.  Salir \n")

	return int(input("Seleccione la opcion: "))

def MENU_GESTION_PERFIL():
	print("Menu de Gestion de Perfil")
	print("\ta. Editar mis datos personales")
	print("\tb. Eliminar mi perfil")
	print("\tc. Volver\n")

	return input("Seleccione la opcion: ")

def MENU_GESTION_CANDIDATOS():
	print("Menu de gestion de candidatos")
	print("\ta. Ver candidatos")
	print("\tb. Reportar un candidato")
	print("\tc. Volver\n")

	return input("Seleccione la opcion: ")

def MENU_MATCHEOS():
	print("Menu de gestion de candidatos")
	print("\ta. Ver matcheos")
	print("\tb. Eliminar un matcheo")
	print("\tc. Volver\n")

	print("En construcción...\nNinguna opción es funcional\n")
	return input("Seleccione la opcion: ")

# OTRAS FUNCIONES
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
	elif(mes_nacimiento == mes_actual and dia_nacimiento > dia_actual):
		edad = edad - 1
	return edad

def INGRESAR_NACIMIENTO():
	formato_correcto = False
	while(not formato_correcto):
		fecha = input("Formato (año-mes-dia) \nxxxx-xx-xx \nIngrese la fecha de nacimiento: ")
		if(len(fecha)!=10):
			print("La longitud de la fecha es incorrecta\n")
		else:
			formato_correcto = True
	return fecha


def MOSTRAR_DATOS_ESTUDIANTES():
	for n in range(cant_estudiantes):
		if(sesion != n):
			print("Estudiante",n)
			print("Nombre:", estudiantes[n][2])
			print("Fecha de Nacimiento:", estudiantes[n][3])
			print("Edad:", CALCULAR_EDAD(estudiantes[n][3]))
			print("Biografia:", estudiantes[n][5])
			print("Hobbies: {} \n" .format(estudiantes[n][4]))

def AGREGAR_MATCHEO():
	me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
	LIMPIAR_CONSOLA()

	me_gusta_id = NOMBRE_CORRECTO(me_gusta.lower())
	if(me_gusta_id > -1):	
		likes[sesion][me_gusta_id] = 1
		print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
	else:
		print("El nombre ingresado no es correcto\n")

def NOMBRE_CORRECTO(nombre):
	correcto = -1;
	est = 0;
	while(correcto == -1 and est < cant_estudiantes):
		if(nombre == estudiantes[est][2].lower()):
			if(est != sesion):
				correcto = est
			else:
				print("No puedes seleccionarte a ti mismo!\n")
				est = cant_estudiantes
		est = est + 1
	return correcto;

def EDITAR_DATOS():
	print("¿ Que desea editar ?")
	print("\t1. email")
	print("\t2. contraseña")
	print("\t3. nombre")
	print("\t4. fecha de nacimiento")
	print("\t5. hobbie")
	print("\t6. biografía")
	print("\t7. sexo")

	opcion_editar = int(input("Selecciona la opcion: "))
	LIMPIAR_CONSOLA()
	match opcion_editar:
		case 1:
			estudiantes[sesion][0] = input("Ingrese un nuevo email: ")			
			LIMPIAR_CONSOLA()
		case 2:
			estudiantes[sesion][1] = input("Ingrese un nuevo contraseña: ")
			LIMPIAR_CONSOLA()
		case 3:
			estudiantes[sesion][2] = input("Ingrese un nuevo nombre: ")
			LIMPIAR_CONSOLA()
		case 4:
			estudiantes[sesion][3] = INGRESAR_NACIMIENTO()	
			LIMPIAR_CONSOLA()
		case 5:
			estudiantes[sesion][4] = input("Ingrese un nuevo hobbie: ")
			LIMPIAR_CONSOLA()
		case 6:
			estudiantes[sesion][5] = input("Ingrese una nueva biografia: ")
			LIMPIAR_CONSOLA()
		case 7:
			estudiantes[sesion][6] = input("Ingrese un nuevo sexo: ")
			LIMPIAR_CONSOLA()
		case _: 
			LIMPIAR_CONSOLA()
			print("Opción incorrecta.\n")

def ELIMINAR_PERFIL(sesion_nueva):
	print("Desea eliminar su perfil?")
	print("\t1. Si")
	print("\t0. No\n")
	opcion_eliminar = int(input("Selecciona la opción: "))
	LIMPIAR_CONSOLA()


	match opcion_eliminar:
		case 1:
			estudiantes[sesion][7] = 0 
			sesion_nueva = -1
			
		case 0:
			LIMPIAR_CONSOLA()
		case _: 
			LIMPIAR_CONSOLA()
			print("Opción incorrecta.\n")
	return sesion_nueva

def DESACTIVAR_USUARIO():
	desactivar_usuario = input("Ingrese el nombre de usuario que desea desactivar: ").lower()
	usuario_encontrado = False

	for n in range(cant_estudiantes):
		if (desactivar_usuario == estudiantes[n][2].lower()):
			usuario_encontrado = True
			print("Desea eliminar su perfil?")
			print("\t1. Si")
			print("\t0. No\n")
			opcion_desactivar = int(input("Selecciona la opción: "))
			LIMPIAR_CONSOLA()

			match opcion_desactivar:
				case 1:
					estudiantes[n][7] = 0 
			
				case 0:
					print("")
				case _: 
					LIMPIAR_CONSOLA()
					print("Opción incorrecta.\n")

	if not usuario_encontrado:
		print("No se encontro el nombre del usuario que se queria desactivar")

	
def REPORTAR():
	# faltaaaaaaaaa
	id_reportante = ""
	id_reportado = ""
	motivo= ""

	cant_reportes = cant_reportes + 1
	reportes[cant_reportes] = [id_reportante,id_reportado,motivo,'0']

def REPORTES_ESTADISTICOS():
	print("En construcción...\n")

# BONUS TRACKS
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

def EDADES():
	print("Bonus track todavía no resuelto")

def MATCHEOS_COMBINADOS(cant):
	""" Forma alternativa sin formula (fuerza bruta)
	matcheos_posibles = 0
	for i in range(cant):
		for n in range(i):
			matcheos_posibles = matcheos_posibles + 1
	""" 
	matcheos_posibles = cant * (cant-1) / 2
	print("La cantidad de matcheos posibles con la cantidad de estudiantes actuales, es decir",cant,"estudiantes, es de:",int(matcheos_posibles),"\n")

estudiantes = [[""]*8 for n in range(8)] # email | contrasena | nombre | nacimiento | hobbies | bio | sexo | estado
estudiantes[0][0] = "a"; estudiantes[0][1] = "1"; estudiantes[0][2] = "Juliancito"; estudiantes[0][3] = "2006-01-07"; estudiantes[0][4] = "pescar, nadar"; estudiantes[0][7] = 1;
estudiantes[1][0] = "estudiante2@ayed.com"; estudiantes[1][1] = "333444"; estudiantes[1][2] = "Pedrito"; estudiantes[1][3] = "2005-04-10"; estudiantes[1][4] = "comer, jugar"; estudiantes[1][7] = 1;
estudiantes[2][0] = "estudiante3@ayed.com"; estudiantes[2][1] = "555666"; estudiantes[2][2] = "Anita"; estudiantes[2][3] = "2004-10-20"; estudiantes[2][4] = "leer sobre jojos"; estudiantes[2][7] = 1;
cant_estudiantes = 3
# Para probar más rápido un mail válido es a y su contraseña es 1

admins = [[""]*2 for n in range(4)] # email | contrasena
admins[0][0] = "b"; admins[0][1] = "1"
cant_admins = 1

likes = LIKES_AUTO()

reportes = [[""]*4 for n in range(10)] # id_reportante | id_reportado | motivo | estado
cant_reportes = 0

opcion_inicio = -1
while(opcion_inicio != 0):

	sesion = -1
	sesion_adm = -1
	opcion_inicio = -1
	while(opcion_inicio != 0 and opcion_inicio != 1):
		opcion_inicio = MENU_INICIO()
		match opcion_inicio:
			case 1:
				if(cant_estudiantes < 4):
					print("No hay la cantidad de estudiantes necesarios para iniciar el programa, se necesitan",4 - cant_estudiantes, "más.")
				elif(cant_admins < 1):
					print("No hay la cantidad de administradores necesarios para iniciar el programa, se necesita al menos uno.")
				else:
					sesion, sesion_adm = LOGIN()
			case 2:
				cant_estudiantes = REGISTRO(cant_estudiantes)

			case 11:
				RULETA_AFINIDAD()
			case 21:
				EDADES()
			case 22:
				MATCHEOS_COMBINADOS(cant_estudiantes)

			case 0:
				LIMPIAR_CONSOLA()
				print("Adios!")
			case _:
				print("Opción incorrecta.\n")


	opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
	while(sesion > -1 and opcion != 0):

		opcion = MENU_PRINCIPAL_ESTUDIANTE(sesion,estudiantes[sesion][2])
		LIMPIAR_CONSOLA()
		match opcion:
			case 1:
				opcion_perfil = ''
				while(opcion_perfil != 'c' and sesion != -1):
					opcion_perfil = MENU_GESTION_PERFIL()
					match opcion_perfil:
						case 'a':
							LIMPIAR_CONSOLA()
							EDITAR_DATOS() 

						case 'b':
							LIMPIAR_CONSOLA()
							sesion = ELIMINAR_PERFIL(sesion)

						case 'c':
							LIMPIAR_CONSOLA() #volver
						case _: 
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")

			case 2:
				opcion_candidatos = ''
				while(opcion_candidatos != 'c'):
					opcion_candidatos = MENU_GESTION_CANDIDATOS()
					match opcion_candidatos:
						case 'a':
							LIMPIAR_CONSOLA()
							MOSTRAR_DATOS_ESTUDIANTES()
							AGREGAR_MATCHEO()

						case 'b':
							REPORTAR()
							LIMPIAR_CONSOLA()
							
						case 'c':
							LIMPIAR_CONSOLA() #volver							
						case _: 
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")	

			case 3:
				opcion_matcheo = ''
				while(opcion_matcheo != 'c'):	
					opcion_matcheo = MENU_MATCHEOS()
					match opcion_matcheo:
						case 'a':
							LIMPIAR_CONSOLA()
							# VER MATCHEOS
						case 'b':
							LIMPIAR_CONSOLA() 

						case 'c':
							LIMPIAR_CONSOLA() #volver
						case _:
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")		

			case 4:
				REPORTES_ESTADISTICOS()
				
			case 0:
				print("\nPrograma terminado.")
			case _:
				print("Opcion incorrecta")	

	while(sesion_adm > -1 and opcion != 0):

		opcion = MENU_PRINCIPAL_MODERADOR(sesion_adm)
		LIMPIAR_CONSOLA()
		match opcion:
			case 1:
				opcion_gest_usuarios = ''
				while(opcion_gest_usuarios != 'b'):
					opcion_gest_usuarios = MENU_GESTION_USUARIOS()
					match opcion_gest_usuarios:
						case 'a':
							LIMPIAR_CONSOLA()
							DESACTIVAR_USUARIO()
							# falta hacer

						case 'b':
							LIMPIAR_CONSOLA() #volver
						case _:
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")

			case 2:
				opcion_gest_reportes = ''
				while(opcion_gest_reportes != 'b'):
					opcion_gest_reportes = MENU_GESTION_REPORTES()
					match opcion_gest_reportes:
						case 'a':
							LIMPIAR_CONSOLA()
							# falta hacer

						case 'b':
							LIMPIAR_CONSOLA() #volver
						case _:
							LIMPIAR_CONSOLA()
							print("Opción incorrecta.\n")

			case 3:
				REPORTES_ESTADISTICOS()

			case 0:
				print("\nPrograma terminado.")
			case _:
				print("Opcion incorrecta")	

