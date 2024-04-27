# Archivo principal

print("1. Gestionar mi perfil")
print("2. Gestionar candidatos")
print("3. Matcheos")
print("4. Reportes estadisticos")
print("0. Salir \n")

opcion = int(input("Seleccione la opcion: "))

while(opcion != 0):
	if(opcion == 1):
		print("Elegiste gestionar tu perfil :)")

	if(opcion>4 or opcion<0):
		opcion = int(input("Opcion incorrecta, seleccione otra opcion: "))
	else:
		opcion = int(input("\nSeleccione otra opcion: "))

print("Programa terminado.")
