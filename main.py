# Archivo principal:/ ISI 1K03 AyED 2024 - Cabrera Martín, Delgado Mauro, Rodriguez Lautaro, Rossi Dariana
# -*- coding: utf-8 -*-

from datetime import datetime
from random   import randint
from getpass  import getpass
import os

# BASICO
def limpiarConsola():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # macOS y Linux
		os.system('clear')

def likesAuto():
	likes = [[0]*8 for n in range(8)] #Aca se rellena al 100% con 0
	for i in range(8):
		for j in range (8):
			likes[i][j] = randint(0,1) 

	return likes

# INICIO
def menuInicio():
	print("INICIO")
	print("\t1. Login")
	print("\t2. Registrarse")
	print("\t11.Bonus Track 1.1 (Ruleta)")
	print("\t21.Bonus Track 2.1 (Edades)")
	print("\t22.Bonus Track 2.2 (Matcheos combinados)")
	print("\t0. Salir \n")

	return int(input("Seleccione la opcion: "))

def login():
	limpiarConsola()
	sesion = -1
	sesion_adm = -1
	intentos_restantes = 3
	while(sesion == -1 and intentos_restantes > 0):
		print("LOGIN\n")
		email = input("Ingrese su email: ").lower() # El .lower es para forzar minusculas
		contrasena = getpass("Ingrese su contraseña: ")

		limpiarConsola()

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

def registro(nueva_sesion):
	limpiarConsola()
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
			limpiarConsola()
			print("El email ya está siendo utilizado o no es válido\n")
		elif(nombre == "novalido"):
			limpiarConsola()
			print("El nombre ya está siendo utilizado o no es válido\n")
		else:
			estudiantes[nueva_sesion][0] = email
			estudiantes[nueva_sesion][2] = nombre
			estudiantes[nueva_sesion][1] = input("Ingrese la contraseña: ")
			estudiantes[nueva_sesion][3] = ingresarNacimiento()
			estudiantes[nueva_sesion][7] = 1
			nueva_sesion = nueva_sesion + 1
			print(nombre, "registrado!\n")
	else:
		print("Ya se alcanzó el máximo de estudiantes\n")

	return nueva_sesion

# MENUS ESTUDIANTE
def menuPrincipalEstudiante(id, nombre):
	print("Menu Principal del estudiante",nombre,"- con id",id)
	print("\t1.  Gestionar mi perfil")
	print("\t2.  Gestionár candidatos")
	print("\t3.  Matcheos")
	print("\t4.  Reportes estadísticos")
	print("\t0.  Salir \n")

	return int(input("Seleccione la opcion: "))

def menuGestionPerfil():
	print("Menu de Gestion de Perfil")
	print("\ta. Editar mis datos personales")
	print("\tb. Eliminar mi perfil")
	print("\tc. Volver\n")

	return input("Seleccione la opcion: ")

def menuGestionCandidatos():
	print("Menu de gestion de candidatos")
	print("\ta. Ver candidatos")
	print("\tb. Reportar un candidato")
	print("\tc. Volver\n")

	return input("Seleccione la opcion: ")

def menuMatcheos():
	print("Menu de gestion de candidatos")
	print("\ta. Ver matcheos")
	print("\tb. Eliminar un matcheo")
	print("\tc. Volver\n")

	print("En construcción...\nNinguna opción es funcional\n")
	return input("Seleccione la opcion: ")

# MENUS MODERADOR
def menuPrincipalModerador(id):
	print("Menu Principal del moderador con id",id)
	print("\t1. Gestionar usuarios")
	print("\t2. Gestionar Reportes")
	print("\t0. Salir \n")

	return int(input("Seleccione la opcion: "))

def menuGestionUsuarios():
	print("Menu de Gestion de Usuarios")
	print("\ta. Desactivar usuario")
	print("\tb. Volver\n")

	return input("Seleccione la opcion: ")

def menuGestionReportes():
	print("Menu de Gestion de Reportes")
	print("\ta. Ver reportes")
	print("\tb. Volver\n")

	return input("Seleccione la opcion: ")

# FUNCIONES ESTUDIANTE
def ingresarNacimiento():
    fecha = input("Formato (año-mes-dia)\nxxxx-xx-xx\nIngrese la fecha de nacimiento: ")
    while len(fecha) != 10:
        print("La longitud de la fecha es incorrecta\n")
        fecha = input("Formato (año-mes-dia)\nxxxx-xx-xx\nIngrese la fecha de nacimiento: ")
    limpiarConsola()
    return fecha

def mostrarDatosEstudiantes():
	for n in range(cant_estudiantes):
		if(sesion != n and estudiantes[n][7] == 1):
			print("Estudiante",n)
			print("Nombre:", estudiantes[n][2])
			print("Fecha de Nacimiento:", estudiantes[n][3])
			print("Edad:", calcularEdad(estudiantes[n][3]))
			print("Biografia:", estudiantes[n][5])
			print("Hobbies: {} \n" .format(estudiantes[n][4]))

def nombreCorrecto(nombre):
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
def agregarMatcheo():
	me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
	limpiarConsola()

	me_gusta_id = nombreCorrecto(me_gusta.lower())
	if(me_gusta_id > -1):	
		likes[sesion][me_gusta_id] = 1
		print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))
	else:
		print("El nombre ingresado no es correcto\n")

def editarDatos():
	print("¿ Que desea editar ?")
	print("\t1. email")
	print("\t2. contraseña")
	print("\t3. nombre")
	print("\t4. fecha de nacimiento")
	print("\t5. hobbie")
	print("\t6. biografía")
	print("\t7. sexo")

	opcion_editar = int(input("Selecciona la opcion: "))
	limpiarConsola()
	match opcion_editar:
		case 1:
			estudiantes[sesion][0] = input("Ingrese un nuevo email: ")			
		case 2:
			estudiantes[sesion][1] = input("Ingrese un nuevo contraseña: ")
		case 3:
			estudiantes[sesion][2] = input("Ingrese un nuevo nombre: ")
		case 4:
			estudiantes[sesion][3] = ingresarNacimiento()	
		case 5:
			estudiantes[sesion][4] = input("Ingrese un nuevo hobbie: ")
		case 6:
			estudiantes[sesion][5] = input("Ingrese una nueva biografia: ")
		case 7:
			estudiantes[sesion][6] = input("Ingrese un nuevo sexo: ")
		case _: 
			limpiarConsola()
			print("Opción incorrecta.\n")
	if opcion_editar >= 1 and opcion_editar <= 7:
		limpiarConsola()	

def eliminarPerfil(sesion_nueva):
	print("Desea eliminar su perfil?")
	print("\t1. Si")
	print("\t0. No\n")
	opcion_eliminar = int(input("Selecciona la opción: "))
	limpiarConsola()


	match opcion_eliminar:
		case 1:
			estudiantes[sesion][7] = 0 
			sesion_nueva = -1
			
		case 0:
			limpiarConsola()
		case _: 
			limpiarConsola()
			print("Opción incorrecta.\n")
	return sesion_nueva

def pedirNombreID():
	opcion_reportar = ''
	while(opcion_reportar != 'a' and opcion_reportar != 'b'):
		id_reportado = -1
		opcion_reportar = input("Seleccione que ingresara del usuario a reportar\n\ta) Nombre\n\tb) ID\nOpcion: ")
		match opcion_reportar:
			case 'a':
				nombre_reportado = input("\nIngrese el nombre del usuario a reportar: ").lower()
				for i in range(cant_estudiantes):
					if (nombre_reportado == estudiantes[i][2].lower()):
						id_reportado = i

			case 'b':
				id_posible_reportado = int(input("\nIngrese la id del usuario a reportar: "))
				if id_posible_reportado >= 0 and id_posible_reportado < cant_estudiantes:
					id_reportado = id_posible_reportado

			case _:
				print("\nOpcion incorrecta\n\n")
	return int(id_reportado)
def reportar(cant):
	id_reportante = sesion
	id_reportado = pedirNombreID()
	if(id_reportado == -1):
		limpiarConsola()
		print("Usuario no encontrado\n")
	elif(id_reportante == id_reportado):
		limpiarConsola()
		print("No te puedes reportar a ti mismo\n")
	else:
		motivo = input("Ingrese el motivo de su reporte: ")
		limpiarConsola()
		if (cant < len(reportes)):
			print("Reporte enviado\n")
			reportes[cant] = [id_reportante,id_reportado,motivo,'0']
			cant = cant + 1
		else:
			print("No se puede reportar mas candidatos\n")
	return cant

# FUNCIONES MODERADOR
def desactivarUsuario():
	desactivar_usuario_v = input("Ingrese el nombre de usuario que desea desactivar: ").lower()
	cartel = "No se encontro el nombre del usuario que se queria desactivar\n"

	for n in range(cant_estudiantes):
		if (desactivar_usuario_v == estudiantes[n][2].lower()):
			print("Desea eliminar su perfil?")
			print("\t1. Si")
			print("\t0. No\n")
			opcion_desactivar = int(input("Selecciona la opción: "))
			limpiarConsola()

			match opcion_desactivar:
				case 1:
					estudiantes[n][7] = 0
					cartel = "El usuario " + estudiantes[n][2] + " de id " + str(n) + " fue correctamente desactivado.\n"
			
				case 0:
					cartel = ""
				case _: 
					limpiarConsola()
					print("Opción incorrecta.\n")

	print(cartel)

def verReportes():
	sin_nuevos_reportes = True
	for i in range(cant_reportes):
		id_reportante = int(reportes[i][0])
		id_reportado = int(reportes[i][1])

		if (estudiantes[id_reportante][7] == 1 and estudiantes[id_reportado][7] == 1 and reportes[i][3] == '0'):
			sin_nuevos_reportes = False
			print("Reporte",i+1)
			print("\tReportante:",estudiantes[id_reportante][2],"ID:",reportes[i][0])
			print("\tReportado:",estudiantes[id_reportado][2],"ID:",reportes[i][1])
			print("\tMotivo:", reportes[i][2], "\n")
			
			opcion_reporte = input("Seleccione como se quiere proceder:\n\ta) Ignorar reporte\n\tb) Bloquear al reportado\nOpcion: ")
			match opcion_reporte:
				case 'a':
					reportes[i][3] = '2'
					print("\nSe ignoro el reporte.\n\n")

				case 'b':
					reportes[i][3] = '1'
					estudiantes[id_reportado][7] = 0
					print("\nSe bloqueo al reportado.\n\n")

				case _:
					print("Opción incorrecta.\n")

	if sin_nuevos_reportes:
		print("No hay reportes por mostrar.\n")

# OTRAS FUNCIONES
def calcularEdad(nacimiento):
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

def reportesEstadisticos():
	match = 0
	likes_dados_no_recibidos = 0
	likes_recibidos_no_dados = 0

	for n in range(cant_estudiantes):
		if n != sesion:

			if likes[sesion][n] == 1 and likes[n][sesion] == 1:
				match = match + 1
			
			if likes[sesion][n] == 1 and likes[n][sesion] == 0:
				likes_dados_no_recibidos = likes_dados_no_recibidos + 1
			
			if likes[sesion][n] == 0 and likes[n][sesion] == 1:
				likes_recibidos_no_dados = likes_recibidos_no_dados + 1 
	
	porcentaje_matcheos_posibles = (match / (cant_estudiantes - 1)) * 100 

	print(f"Matcheados sobre el % posible:{porcentaje_matcheos_posibles:.2f}%")
	print("Likes dados y no recibidos:", likes_dados_no_recibidos)
	print("Likes recibidos y no dados:", likes_recibidos_no_dados,"\n")

# BONUS TRACKS
def ruletaAfinidad():
	porcentaje_total = -1 
	while(porcentaje_total != 100):
		porcentaje1 = int(input("Porcentaje de afinidad con la persona A: "))
		porcentaje2 = int(input("Porcentaje de afinidad con la persona B: "))
		porcentaje3 = int(input("Porcentaje de afinidad con la persona C: "))
		porcentaje_total = porcentaje1 + porcentaje2 + porcentaje3
		
		if(porcentaje_total != 100):
			limpiarConsola()
			print("Los porcentajes no suman 100!!! Ingreselos nuevamente. \n")
	
	random = randint(0, 99)
	
	limpiarConsola()

	if(random < porcentaje1):
		print("Salió la persona A!!!\n")
	elif(random < porcentaje1 + porcentaje2):
		print("Salió la persona B!!!\n")
	else: 
		print("Salió la persona C!!!\n")

def menuBonus21():
	print("MENU BONUS 2-1")
	print("Probar con...")
	print("\t1. Array random de longitud definida")
	print("\t2. Arrays de ejemplo")
	print("\t3. Array que ingrese")
	print("\t0. Salir \n")

	return int(input("Seleccione la opcion: "))
def sort(array):
	for i in range(len(array)):
		min_idx = i
		for j in range(i+1, len(array)):
			if(array[j] < array[min_idx]):
				min_idx = j
		
		array[i], array[min_idx] = array[min_idx], array[i]
def huecos(array):
	cant_huecos = 0

	for i in range(len(array)-1):
		if(array[i]+2 == array[i+1]):
			cant_huecos += 1

	return cant_huecos
def edades():
	opcion_bonus21 = -1
	while(opcion_bonus21 != 0):
		opcion_bonus21 = menuBonus21()
		limpiarConsola()
		match opcion_bonus21:
			case 1:
				cant_estudiantes_bonus = int(input("Cantidad de estudiantes que quiere tener: "))
				estudiantes_bonus = [randint(10, 40) for _ in range(cant_estudiantes_bonus)] # Edades entre los 10 y 40 años
				
				print("El array de longitud ", cant_estudiantes_bonus, "random es ", estudiantes_bonus,"\n")
				sort(estudiantes_bonus)
				print("El array ordenado sería ", estudiantes_bonus)
				print("Hay ", huecos(estudiantes_bonus)," huecos en total.\n\n")
			
			case 2:
				estu_b1 = [11,14,9,5,7,15]
				estu_b2 = [2,5,3,8,1]
				estu_b3 = [21, 18, 20, 19, 23, 24] 

				print("Ejemplo inventado:\n")
				print("\tEl array de ejemplo es ",estu_b1, "\n")
				sort(estu_b1)
				print("\tEl array ordenado queda ", estu_b1)
				print("\tHay ", huecos(estu_b1), " huecos en total.\n\n")

				print("Ejemplos del TP:\n")
				print("\tPrimer ejemplo:")
				print("\t\tEl array de ejemplo es ",estu_b2, "\n")
				sort(estu_b2)
				print("\t\tEl array ordenado queda ", estu_b2)
				print("\t\tHay ", huecos(estu_b2), " huecos en total.\n")

				print("\tSegundo ejemplo:")
				print("\t\tEl array de ejemplo es ",estu_b3, "\n")
				sort(estu_b3)
				print("\t\tEl array ordenado queda ", estu_b3)
				print("\t\tHay ", huecos(estu_b3), " huecos en total.\n\n")

			case 3:
				cant_estudiantes_bonus = int(input("Cantidad de estudiantes que quiere tener: "))
				estu_bonus_man = [0]*cant_estudiantes_bonus
				print("Ingrese los números: ")
				for i in range(cant_estudiantes_bonus):
					estu_bonus_man[i] = int(input(""))

				limpiarConsola()

				print("El array quedaría así ", estu_bonus_man, "\n")
				sort(estu_bonus_man)
				print("El array ordenado queda ", estu_bonus_man)
				print("Hay ", huecos(estu_bonus_man), " huecos en total.\n\n")
			
			case 0:
				limpiarConsola() #volver
			
			case _:
				print("Opción incorrecta.\n")

def matcheosCombinados(cant):
	""" Forma alternativa sin formula (fuerza bruta)
	matcheos_posibles = 0
	for i in range(cant):
		for n in range(i):
			matcheos_posibles = matcheos_posibles + 1
	""" 
	matcheos_posibles = cant * (cant-1) / 2
	print("La cantidad de matcheos posibles con la cantidad actual de estudiantes ({}) es de:".format(cant), int(matcheos_posibles),"\n")

estudiantes = [[""]*8 for n in range(8)] # email | contrasena | nombre | nacimiento | hobbies | bio | sexo | estado
estudiantes[0][0] = "a"; estudiantes[0][1] = "1"; estudiantes[0][2] = "Julian"; estudiantes[0][3] = "2006-01-07"; estudiantes[0][4] = "pescar, nadar"; estudiantes[0][7] = 1;
estudiantes[1][0] = "estudiante2@ayed.com"; estudiantes[1][1] = "333444"; estudiantes[1][2] = "Pedro"; estudiantes[1][3] = "2005-04-10"; estudiantes[1][4] = "comer, jugar"; estudiantes[1][7] = 1;
estudiantes[2][0] = "estudiante3@ayed.com"; estudiantes[2][1] = "555666"; estudiantes[2][2] = "Ana"; estudiantes[2][3] = "2004-10-20"; estudiantes[2][4] = "leer sobre jojos"; estudiantes[2][7] = 1;
cant_estudiantes = 3
# Para probar más rápido un mail de estudiante válido es a y su contraseña es 1

admins = [[""]*2 for n in range(4)] # email | contrasena
admins[0][0] = "b"; admins[0][1] = "1"
cant_admins = 1
# Para probar más rápido un mail válido de moderador es b y su contraseña 1

likes = likesAuto()

reportes = [[""]*4 for n in range(10)] # id_reportante | id_reportado | motivo | estado
cant_reportes = 0

opcion_inicio = -1
limpiarConsola()
while(opcion_inicio != 0):

	sesion = -1
	sesion_adm = -1
	opcion_inicio = -1
	while(opcion_inicio != 0 and opcion_inicio != 1):
		opcion_inicio = menuInicio()
		limpiarConsola()
		match opcion_inicio:
			case 1:
				if(cant_estudiantes < 4):
					print("No hay la cantidad de estudiantes necesarios para iniciar el programa, se necesitan", 4 - cant_estudiantes, "más.\n")
				elif(cant_admins < 1):
					print("No hay la cantidad de administradores necesarios para iniciar el programa, se necesita al menos uno.\n")
				else:
					sesion, sesion_adm = login()
			case 2:
				cant_estudiantes = registro(cant_estudiantes)

			case 11:
				ruletaAfinidad()
			case 21:
				edades()
			case 22:
				matcheosCombinados(cant_estudiantes)

			case 0:
				print("Adios!")
			case _:
				print("Opción incorrecta.\n")


	opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
	while(sesion > -1 and opcion != 0):

		opcion = menuPrincipalEstudiante(sesion,estudiantes[sesion][2])
		limpiarConsola()
		match opcion:
			case 1:
				opcion_perfil = ''
				while(opcion_perfil != 'c' and sesion != -1):
					opcion_perfil = menuGestionPerfil()
					limpiarConsola()
					match opcion_perfil:
						case 'a':
							editarDatos() 

						case 'b':
							sesion = eliminarPerfil(sesion)

						case 'c':
							limpiarConsola() #volver
						case _: 
							print("Opción incorrecta.\n")

			case 2:
				opcion_candidatos = ''
				while(opcion_candidatos != 'c'):
					opcion_candidatos = menuGestionCandidatos()
					limpiarConsola()
					match opcion_candidatos:
						case 'a':
							mostrarDatosEstudiantes()
							agregarMatcheo()

						case 'b':
							cant_reportes = reportar(cant_reportes)
							
						case 'c':
							limpiarConsola() #volver							
						case _: 
							print("Opción incorrecta.\n")	

			case 3:
				opcion_matcheo = ''
				while(opcion_matcheo != 'c'):	
					opcion_matcheo = menuMatcheos()
					limpiarConsola()
					match opcion_matcheo:
						case 'a':
							print("Ver Matcheos aún no realizado.\n") # VER MATCHEOS
						case 'b':
							print("Eliminar un Matcheo aún no realizado.\n") # ELIMINAR UN MATCHEO
						case 'c':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")		

			case 4:
				reportesEstadisticos()
				
			case 0:
				print("\nSesión finalizada.\n")
			case _:
				print("Opcion incorrecta")	

	while(sesion_adm > -1 and opcion != 0):

		opcion = menuPrincipalModerador(sesion_adm)
		limpiarConsola()
		match opcion:
			case 1:
				opcion_gest_usuarios = ''
				while(opcion_gest_usuarios != 'b'):
					opcion_gest_usuarios = menuGestionUsuarios()
					limpiarConsola()
					match opcion_gest_usuarios:
						case 'a':
							desactivarUsuario()

						case 'b':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")

			case 2:
				opcion_gest_reportes = ''
				while(opcion_gest_reportes != 'b'):
					opcion_gest_reportes = menuGestionReportes()
					limpiarConsola()
					match opcion_gest_reportes:
						case 'a':
							verReportes()

						case 'b':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")

			case 0:
				print("\nSesión finalizada.\n")
			case _:
				print("Opcion incorrecta")	
