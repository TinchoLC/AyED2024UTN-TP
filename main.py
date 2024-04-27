# Archivo principal

estudiante1_email = "a"; estudiante1_contrasena = str(1)
estudiante2_email = "estudiante2@ayed.com"; estudiante2_contrasena = str(333444)
estudiante3_email = "estudiante3@ayed.com"; estudiante3_contrasena = str(555666)

ingreso_correcto = False
intentos_restantes = 3
while(not ingreso_correcto and intentos_restantes > 0):
	email = input("Ingrese su email: ")
	contrasena = input("Ingrese su contraseña: ")

	intentos_restantes = intentos_restantes - 1

	if(email == estudiante1_email and contrasena == estudiante1_contrasena):
		print("\nFelicidades ingresaste!\n")
		ingreso_correcto = True
	elif(email == estudiante2_email and contrasena == estudiante2_contrasena):
		print("\nFelicidades ingresaste!\n")
		ingreso_correcto = True	
	elif(email == estudiante3_email and contrasena == estudiante3_contrasena):
		print("\nFelicidades ingresaste!\n")
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
		opcion = input("Selecciona la opcion: ")
	elif(opcion == 2):
		print("a")
	elif(opcion == 3):
		print("En construccion")
	elif(opcion == 4):
		print("En construccion")	
	else: # Opcion invalida
		print("OPCION INCORRECTA")

print("Programa terminado.")
