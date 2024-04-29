# Archivo principal
from datetime import datetime 

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
		print("\nFelicidades ingresaste!\n")
		sesion = 1
		ingreso_correcto = True
	elif(email == estudiante2_email and contrasena == estudiante2_contrasena):
		print("\nFelicidades ingresaste!\n")
		sesion = 2
		ingreso_correcto = True	
	elif(email == estudiante3_email and contrasena == estudiante3_contrasena):
		print("\nFelicidades ingresaste!\n")
		sesion = 3
		ingreso_correcto = True
	else: # No se ingreso correctamente
		print("\nNo ingresaste correctamente :(\n")
		print("Te quedan ",intentos_restantes,"intentos.")

opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
while(ingreso_correcto and opcion != 0):
	print("1. Gestionar mi perfil")
	print("2. Gestionár candidatos")
	print("3. Matcheos")
	print("4. Reportes estadisticos")
	print("0. Salir \n")

	opcion = int(input("Seleccione la opcion: "))


	if(opcion == 1): # Opcion Gestionar mi perfil
		print("Menu de Gestión de Perfil")
		print("\t1. Editar mis datos personales\n")
		opcion = int(input("Selecciona la opcion: "))
		if(opcion == 1):
			print("¿ Que desea editar ?")
			print("\t1. fecha de nacimiento")
			print("\t2. biografia")
			print("\t3. hobbies")
			opcion = int(input("Selecciona la opcion: "))
			if(opcion == 1):
				if(sesion == 1):
					estudiante1_nacimiento = input("Ingrese una nueva fecha: ")
				elif(sesion == 2):
					estudiante2_nacimiento = input("Ingrese una nueva fecha: ")
				elif(sesion == 3):
					estudiante3_nacimiento = input("Ingrese una nueva fecha: ")
			elif(opcion == 2):
				if(sesion == 1):
					estudiante1_bio = input("Ingrese una nueva biografia: ")
				elif(sesion == 2):
					estudiante2_bio = input("Ingrese una nueva biografia: ")
				elif(sesion == 3):
					estudiante3_bio = input("Ingrese una nueva biografia: ")
			elif(opcion == 3):
				if(sesion == 1):
					estudiante1_hobbies = input("Ingrese un nuevo hobbie: ")
				elif(sesion == 2):
					estudiante2_hobbies = input("Ingrese un nuevo hobbie: ")
				elif(sesion == 3):
					estudiante3_hobbies = input("Ingrese un nuevo hobbie: ")
	elif(opcion == 2):
		print("Menu de gestion de candidatos")
		print("\t1. Ver candidatos\n")
		opcion = int(input("Seleccione la opcion: "))
		
		if(opcion == 1):
			# Año actual
			current_year = datetime.now().year
			# Calcular la edad de cada estudiante
			estudiante1_edad = current_year - int(estudiante1_nacimiento[:4])
			estudiante2_edad = current_year - int(estudiante2_nacimiento[:4])
			estudiante3_edad = current_year - int(estudiante3_nacimiento[:4])
			
			print("\nEstudiante 1")
			print("Nombre:", estudiante1_nombre)
			print("Fecha de Nacimiento:", estudiante1_nacimiento)
			print("Edad:", estudiante1_edad)
			print("Biografia:", estudiante1_bio)
			print("Hobbies:", estudiante1_hobbies)
			
			print("\nEstudiante 2")
			print("Nombre:", estudiante2_nombre)
			print("Fecha de Nacimiento:", estudiante2_nacimiento)
			print("Edad:", estudiante2_edad)
			print("Biografia:", estudiante2_bio)
			print("Hobbies:", estudiante2_hobbies)
			
			print("\nEstudiante 3")
			print("Nombre:", estudiante3_nombre)
			print("Fecha de Nacimiento:", estudiante3_nacimiento)
			print("Edad:", estudiante3_edad)
			print("Biografia:", estudiante3_bio)
			print("Hobbies:", estudiante3_hobbies)
			
			# FALTA CORROBORAR SI EL NOMBRE ESTA DISPONIBLE
			if(sesion==1):
				me_gusta1 = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
			elif(sesion==2):
				me_gusta2 = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
			elif(sesion==3):
				me_gusta3 = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
	elif(opcion == 3):
		print("En construccion")
	elif(opcion == 4):
		print("En construccion")	
	else: # Opcion invalida
		print("OPCION INCORRECTA")

print("Programa terminado.")
