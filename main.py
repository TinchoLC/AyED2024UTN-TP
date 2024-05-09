# Archivo principal
from datetime import datetime 

def MENU_PRINCIPAL():
	print("\nMenu Principal")
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
	if(sesion != 1):
		print("\nEstudiante 1")
		print("Nombre:", estudiante1_nombre)
		print("Fecha de Nacimiento:", estudiante1_nacimiento)
		print("Edad:", estudiante1_edad)
		print("Biografia:", estudiante1_bio)
		print("Hobbies:", estudiante1_hobbies)

	if(sesion != 2):
		print("\nEstudiante 2")
		print("Nombre:", estudiante2_nombre)
		print("Fecha de Nacimiento:", estudiante2_nacimiento)
		print("Edad:", estudiante2_edad)
		print("Biografia:", estudiante2_bio)
		print("Hobbies:", estudiante2_hobbies)
	
	if(sesion != 3):
		print("\nEstudiante 3")
		print("Nombre:", estudiante3_nombre)
		print("Fecha de Nacimiento:", estudiante3_nacimiento)
		print("Edad:", estudiante3_edad)
		print("Biografia:", estudiante3_bio)
		print("Hobbies:", estudiante3_hobbies)


estudiante1_email = "a"; estudiante1_contrasena = "1"; estudiante1_nombre = "Juliancito"; estudiante1_nacimiento = "2006-01-07"; estudiante1_hobbies = "pescar, nadar"; estudiante1_bio = ""
estudiante2_email = "estudiante2@ayed.com"; estudiante2_contrasena = "333444"; estudiante2_nombre = "Pedrito"; estudiante2_nacimiento = "2005-04-10"; estudiante2_hobbies = "comer, jugar"; estudiante2_bio = ""
estudiante3_email = "estudiante3@ayed.com"; estudiante3_contrasena = "555666"; estudiante3_nombre = "Anita"; estudiante3_nacimiento = "2004-10-20"; estudiante3_hobbies = "leer sobre jojos"; estudiante3_bio = ""

ingreso_correcto = False
intentos_restantes = 3
while(not ingreso_correcto and intentos_restantes > 0):
	email = input("Ingrese su email: ").lower() # El .lower es para forzar minusculas
	contrasena = input("Ingrese su contraseña: ")

	intentos_restantes = intentos_restantes - 1

	if(email == estudiante1_email and contrasena == estudiante1_contrasena):
		print("\nFelicidades",estudiante1_nombre,"ingresaste!\n")
		sesion = 1
		ingreso_correcto = True
	elif(email == estudiante2_email and contrasena == estudiante2_contrasena):
		print("\nFelicidades",estudiante2_nombre,"ingresaste!\n")
		sesion = 2
		ingreso_correcto = True	
	elif(email == estudiante3_email and contrasena == estudiante3_contrasena):
		print("\nFelicidades",estudiante3_nombre,"ingresaste!\n")
		sesion = 3
		ingreso_correcto = True
	else: # No se ingreso correctamente
		print("\nNo ingresaste correctamente :(\n")
		print("Te quedan ",intentos_restantes,"intentos.")

opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
while(ingreso_correcto and opcion != 0):
	
	MENU_PRINCIPAL()
	opcion = int(input("Seleccione la opcion: "))

	match opcion:
		case 1:
			print("Menu de Gestión de Perfil")
			print("\t1. Editar mis datos personales\n")
			opcion_perfil = int(input("Seleccione una opcion: "))
			match opcion_perfil:
				case 1:
					print("¿ Que desea editar ?")
					print("\t1. fecha de nacimiento")
					print("\t2. biografia")
					print("\t3. hobbies\n")
					opcion_editar = int(input("Selecciona la opcion: "))
					match opcion_editar:
						case 1:
							match sesion:
								case 1:
									estudiante1_nacimiento = input("Ingrese una nueva fecha: ")
								case 2:
									estudiante2_nacimiento = input("Ingrese una nueva fecha: ")
								case 3:
									estudiante3_nacimiento = input("Ingrese una nueva fecha: ")

						case 2:
							match sesion:
								case 1:
									estudiante1_bio = input("Ingrese una nueva biografia: ")
								case 2:
									estudiante2_bio = input("Ingrese una nueva biografia: ")
								case 3:
									estudiante3_bio = input("Ingrese una nueva biografia: ")
						case 3:
							match sesion:
								case 1:
									estudiante1_hobbies = input("Ingrese un nuevo hobbie: ")
								case 2:
									estudiante2_hobbies = input("Ingrese un nuevo hobbie: ")
								case 3:
									estudiante3_hobbies = input("Ingrese un nuevo hobbie: ")
		case 2:
			print("Menu de gestion de candidatos")
			print("\t1. Ver candidatos\n")
			opcion_candidatos = int(input("Seleccione la opcion: "))
			match opcion_candidatos:
				case 1:
					MOSTRAR_DATOS_ESTUDIANTES()
					me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ").lower()
					if(me_gusta == estudiante1_nombre.lower() or me_gusta == estudiante2_nombre.lower() or me_gusta == estudiante3_nombre.lower()):	
						if(sesion==1 and estudiante1_nombre.lower() != me_gusta):
							me_gusta1 = me_gusta
							print("\nSeleccionaste a",me_gusta,"espero te corresponda!")
						elif(sesion==2 and estudiante2_nombre.lower() != me_gusta):
							me_gusta2 = me_gusta
							print("\nSeleccionaste a",me_gusta,"espero te corresponda!")
						elif(sesion==3 and estudiante3_nombre.lower() != me_gusta):
							me_gusta3 = me_gusta
							print("\nSeleccionaste a",me_gusta,"espero te corresponda!")
						else:
							print("\nNo puedes seleccionarte a ti mismo!")
					else:
						print("\nEl nombre ingresado no es correcto\n")		
			
			
		case 3:
			print("En construccion")
		case 4:
			print("En construccion")
		case 11:
			porcentaje1 = int(input("Porcentaje de afinidad con la 1er persona: "))
			porcentaje2 = int(input("Porcentaje de afinidad con la 2da persona: "))
			porcentaje3 = int(input("Porcentaje de afinidad con la 3er persona: "))

		case 0:
			print("Elden Ring, saliste, del videojuego")
		case _:
			print("Opcion incorrecta")	
print("Programa terminado.")