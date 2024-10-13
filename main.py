# Archivo principal:/ ISI 1K03 AyED 2024 - Cabrera Martín, Rodriguez Lautaro, Rossi Dariana, Sanchez Jimena
# -*- coding: utf-8 -*-

from datetime import datetime
from random   import randint
from getpass  import getpass
import os
import os.path
import pickle
import io
arcest_fisico = "estudiantes.dat"
arcmod_fisico = "moderadores.dat"
arcadm_fisico = "administradores.dat"
arclik_fisico = "likes.dat"
arcrep_fisico = "reportes.dat"

class estudiante:
	def __init__(self):
		self.id = -1
		self.email = "".ljust(45)
		self.contrasena = "".ljust(30)
		self.nombre = "".ljust(30)
		self.nacimiento = "".ljust(10)
		self.hobbies = "".ljust(150)
		self.bio = "".ljust(150)
		self.sexo = "".ljust(10)
		self.estado = True
		
		self.superlike_disponible = True
		self.revelarcandidato_disponible = True

class moderador:
	def __init__(self):
		self.id = -1
		self.email = "".ljust(45)
		self.contrasena = "".ljust(30)
		self.estado = True
		self.reportes_ignorados = 0
		self.reportes_aceptados = 0

class administrador:
	def __init__(self):
		self.id = -1
		self.email = "".ljust(45)
		self.contrasena = "".ljust(30)

class like:
	def __init__(self):
		self.id_remitente = -1
		self.id_destinatario = -1

class reporte:
	def __init__(self):
		self.id_reportante = -1
		self.id_reportado = -1
		self.motivo = "".ljust(150)
		self.estado = 0

# BASICO-ARCHIVOS
def abrirPorTipo(tipo): # 1 estudiante # 2 moderador # 3 administrador # 4 like # 5 reporte #
	match tipo:
		case 1:
			fisico = arcest_fisico
		case 2:
			fisico = arcmod_fisico
		case 3:
			fisico = arcadm_fisico
		case 4:
			fisico = arclik_fisico
		case 5:
			fisico = arcrep_fisico
			
	logico = open(fisico, "r+b")
	return fisico, logico

def cantRegistros(tipo,estado_activado):
	ar_fisico, ar_logico = abrirPorTipo(tipo)
	longitud_archivo = os.path.getsize(ar_fisico)
	i = 0
	while (ar_logico.tell() < longitud_archivo):
		i = i + 1
		reg_t = pickle.load(ar_logico)
		if(estado_activado):
			if(not reg_t.estado):
				i = i - 1
	ar_logico.close()
	return i

def lenRegistro(tipo):
	ar_fisico, ar_logico = abrirPorTipo(tipo)
	longitud_archivo = os.path.getsize(ar_fisico)

	if(longitud_archivo > 0):
		reg_t = pickle.load(ar_logico)
		long_registro = ar_logico.tell()
	else:
		long_registro = 0

	return long_registro

def likesAuto():
	arclik_logico = open(arclik_fisico, "w+b")
	
	cant_estudiantes = cantRegistros(1,False)
	for i in range(cant_estudiantes):
		for j in range(cant_estudiantes):
			if (i != j and randint(0, 99) < 60):
				reg_like = like()
				reg_like.id_remitente = i; reg_like.id_destinatario = j
				pickle.dump(reg_like, arclik_logico)
				arclik_logico.flush()

	arclik_logico.close()

def crearArchivos():
	if not os.path.exists(arcest_fisico):
		ar_temporal = open(arcest_fisico, "w+b")
		reg_temp = estudiante()

		reg_temp.id = 0; reg_temp.email = "a".ljust(45); reg_temp.contrasena = "1".ljust(30)
		reg_temp.nombre = "Julian".ljust(30); reg_temp.nacimiento = "2006-01-07".ljust(10)
		reg_temp.hobbies = "pescar, nadar, papiroflexia".ljust(150)
		pickle.dump(reg_temp, ar_temporal)
		ar_temporal.flush()

		reg_temp.id = 1; reg_temp.email = "estudiante2@ayed.com".ljust(45); reg_temp.contrasena = "333444".ljust(30)
		reg_temp.nombre = "Pedro".ljust(30); reg_temp.nacimiento = "2005-04-10".ljust(10)
		reg_temp.hobbies = "comer, jugar, ver jojos".ljust(150)
		pickle.dump(reg_temp, ar_temporal)
		ar_temporal.flush()

		reg_temp.id = 2; reg_temp.email = "estudiante3@ayed.com".ljust(45); reg_temp.contrasena = "555666".ljust(30)
		reg_temp.nombre = "Ana".ljust(30); reg_temp.nacimiento = "2004-10-20".ljust(10)
		reg_temp.hobbies = "sonic, cocinar comida típica irlandesa".ljust(150)
		pickle.dump(reg_temp, ar_temporal)
		ar_temporal.flush()

		reg_temp.id = 3; reg_temp.email = "estudiante4@ayed.com".ljust(45); reg_temp.contrasena = "777888".ljust(30)
		reg_temp.nombre = "Mauro".ljust(30); reg_temp.nacimiento = "2001-02-02".ljust(10)
		reg_temp.hobbies = "one piece".ljust(150)
		pickle.dump(reg_temp, ar_temporal)
		ar_temporal.flush()

		ar_temporal.close()
	if not os.path.exists(arcmod_fisico):
		ar_temporal = open(arcmod_fisico, "w+b")
		reg_temp = moderador()

		reg_temp.id = 0; reg_temp.email = "b".ljust(45); reg_temp.contrasena = "1".ljust(30)
		pickle.dump(reg_temp, ar_temporal)

		reg_temp.id = 1; reg_temp.email = "bb".ljust(45); reg_temp.contrasena = "1".ljust(30)
		pickle.dump(reg_temp, ar_temporal)

		ar_temporal.flush()

		ar_temporal.close()
	if not os.path.exists(arcadm_fisico):
		ar_temporal = open(arcadm_fisico, "w+b")
		reg_temp = administrador()
		
		reg_temp.id = 0; reg_temp.email = "c".ljust(45); reg_temp.contrasena = "1".ljust(30)
		pickle.dump(reg_temp, ar_temporal)
		ar_temporal.flush()

		ar_temporal.close()
	if not os.path.exists(arclik_fisico):
		likesAuto()
	if not os.path.exists(arcrep_fisico):
		temporal = open(arcrep_fisico, "w+b")
		temporal.close()

def actualizarRegistro(regA,tipo):
	ar_fisico, ar_logico = abrirPorTipo(tipo)
	longitud_archivo = os.path.getsize(ar_fisico)

	reg_temp = pickle.load(ar_logico)
	longitud_registro = ar_logico.tell()
	while (ar_logico.tell() < longitud_archivo and reg_temp.id != regA.id):
		reg_temp = pickle.load(ar_logico)
	ar_logico.seek(ar_logico.tell()-longitud_registro, 0) 
	pickle.dump(regA, ar_logico)
	ar_logico.flush()
	ar_logico.close()

# BASICO
def limpiarConsola():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # macOS y Linux
		os.system('clear')

def pedirNombreID():
	opcion_usu = ''
	while(opcion_usu != 'a' and opcion_usu != 'b'):
		id_usuario = -1
		opcion_usu = input("Seleccione que ingresara del usuario\n\ta) Nombre\n\tb) ID\nOpcion: ")
		ar_fisico, ar_logico = abrirPorTipo(1)
		longitud_archivo = os.path.getsize(ar_fisico) 
		limpiarConsola()

		match opcion_usu:
			case 'a':
				nombre_usuario = input("Ingrese el nombre del usuario: ").lower().ljust(30)
				
				while (ar_logico.tell() < longitud_archivo):
					reg_temp = pickle.load(ar_logico)
					if(nombre_usuario == reg_temp.nombre.lower()):
						id_usuario = reg_temp.id

			case 'b':
				id_posible_usuario = int(input("Ingrese la id del usuario: "))
				cant_estudiantes = cantRegistros(1,False)
				if(id_posible_usuario >= cant_estudiantes):
					id_usuario = -1
				else:
					while (ar_logico.tell() < longitud_archivo):
						reg_temp = pickle.load(ar_logico)
						if(id_posible_usuario == reg_temp.id):
							id_usuario = reg_temp.id

			case _:
				print("Opcion incorrecta\n")
	ar_logico.close()
	return int(id_usuario)

# INICIO
def menuInicio():
	print("INICIO")
	print("\t1. Login")
	print("\t2. Registrarse")
	print("\t11.Bonus Track 1.1 (Ruleta)")
	print("\t21.Bonus Track 2.1 (Edades)")
	print("\t22.Bonus Track 2.2 (Matcheos combinados)")
	print("\t0. Salir \n")

	op = int(input("Seleccione la opcion: "))
	return op

def login():
	limpiarConsola() 
	
	intentos_restantes = 3

	while(intentos_restantes > 0):
		intentos_restantes = intentos_restantes - 1
		email = input("Ingrese su email: ").lower().ljust(45) # El .lower es para forzar minusculas
		contrasena = getpass("Ingrese su contraseña: ").ljust(30)

		limpiarConsola()

		tipo_sesion = 0
		encontrado = False
		while(tipo_sesion < 3 and not encontrado):
			tipo_sesion = tipo_sesion + 1
			ar_fisico, ar_logico = abrirPorTipo(tipo_sesion)
			longitud_archivo = os.path.getsize(ar_fisico) 
			
			while(ar_logico.tell() < longitud_archivo and not encontrado):
				reg = pickle.load(ar_logico)
				if(email == reg.email and contrasena == reg.contrasena):
					intentos_restantes = 0
					encontrado = True
					if(tipo_sesion != 1):
						print("Felicidades",reg.id,"ingresaste!\n")
					elif(not reg.estado): 
						print("Su cuenta ha sido deshabilitada\n")
						tipo_sesion = 0
					else:
						print("Felicidades",reg.nombre.strip(),"ingresaste!\n")
				else:
					reg.id = -1

		if(intentos_restantes > 0):
			print("No ingresaste correctamente :(")
			print("Te quedan ",intentos_restantes,"intentos.\n")

	ar_logico.close()

	if(reg.id == -1):
		tipo_sesion = 0
		input("Te quedaste sin intentos! Presiona Enter para continuar")
		
	return tipo_sesion, reg

def emailRepetido(mail,arc):
	art_fisico, art_logico = abrirPorTipo(arc)
	longitudt_archivo = os.path.getsize(art_fisico) 

	while(art_logico.tell() < longitudt_archivo):
		regt = pickle.load(art_logico)
		if(mail == regt.email):
			mail = "novalido"

	art_logico.close()
	return mail
def registro(tipo): # tipo 1 estudiante # tipo 2 moderador (usar en menu de admin) #
	limpiarConsola()
	print("REGISTRO\n")
	email = input("Ingrese un email: ").ljust(45)
	nombre = ""
	if(tipo == 1):
		nombre = input("Ingrese un nombre: ").ljust(30)

	limpiarConsola()

	email = emailRepetido(email,3)
	if(tipo == 1):
		email = emailRepetido(email,2)
	elif(tipo == 2):
		email = emailRepetido(email,1)

	ar_fisico, ar_logico = abrirPorTipo(tipo)
	longitud_archivo = os.path.getsize(ar_fisico) 

	while(ar_logico.tell() < longitud_archivo):
		reg = pickle.load(ar_logico)
		if(email == reg.email):
			email = "novalido"
		elif(tipo == 1):
			if(nombre.lower() == reg.nombre.lower()):
				nombre = "novalido"

	nombre_valido = True
	if(tipo == 1): # Parche para que funcione con moderadores
		if(nombre == "novalido"):
			nombre_valido = False 

	if(email == "novalido"):
		limpiarConsola()
		print("El email ya está siendo utilizado o no es válido\n")
	elif(not nombre_valido):
		limpiarConsola()
		print("El nombre ya está siendo utilizado o no es válido\n")
	else:
		reg.id = reg.id + 1
		reg.email = email.ljust(45)
		reg.contrasena = input("Ingrese la contraseña: ").ljust(30)
		reg.estado = True

		limpiarConsola()

		if(tipo == 1):
			reg.nombre = nombre.ljust(30)
			reg.nacimiento = ingresarNacimiento().ljust(10)
			reg.hobbies = "".ljust(150)
			reg.bio = "".ljust(150)
			reg.sexo = "".ljust(10)
			reg.superlike_disponible = True
			reg.revelarcandidato_disponible = True
			print(nombre.strip(), "registrado!\n")
		else:
			reg.reportes_ignorados = 0
			reg.reportes_aceptados = 0
			print("Moderador de id:",reg.id,"registrado!\n")

		ar_logico.seek(longitud_archivo, 0) 
		pickle.dump(reg, ar_logico)
		ar_logico.flush()
		ar_logico.close()

# MENUS ESTUDIANTE
def menuPrincipalEstudiante():
	print("Menu Principal del estudiante", reg.nombre.strip(),"- con id",reg.id)
	print("\t1.  Gestionar mi perfil")
	print("\t2.  Gestionár candidatos")
	print("\t3.  Matcheos")
	print("\t4.  Reportes estadísticos")
	if(reg.superlike_disponible):
		print("\t32.  Dar SuperLike (solo puede hacerse una vez)")
	if(reg.revelarcandidato_disponible):
		print("\t33.  Revelar candidatos que te han dado like (solo puede hacerse una vez)")
	print("\t0.  Salir \n")

	op = int(input("Seleccione la opcion: "))
	return op

def menuGestionPerfil():
	print("Menu de Gestion de Perfil")
	print("\ta. Editar mis datos personales")
	print("\tb. Eliminar mi perfil")
	print("\tc. Volver\n")

	op = input("Seleccione la opcion: ")
	return op

def menuGestionCandidatos():
	print("Menu de gestion de candidatos")
	print("\ta. Ver candidatos")
	print("\tb. Reportar un candidato")
	print("\tc. Volver\n")

	op = input("Seleccione la opcion: ")
	return op

def menuMatcheos():
	print("Menu de gestion de candidatos")
	print("\ta. Ver matcheos")
	print("\tb. Eliminar un matcheo")
	print("\tc. Volver\n")

	print("En construcción...\nNinguna opción es funcional\n")
	op = input("Seleccione la opcion: ")
	return op

# MENUS MODERADOR
def menuPrincipalModerador():
	print("Menu Principal del moderador con id",reg.id)
	print("\t1. Gestionar usuarios")
	print("\t2. Gestionar Reportes")
	print("\t3. Reportes Estadísticos")
	print("\t0. Salir \n")

	op = int(input("Seleccione la opcion: "))
	return op

def menuModGestionUsuarios():
	print("Menu de Gestion de Usuarios")
	print("\ta. Desactivar usuario")
	print("\tb. Volver\n")

	op = input("Seleccione la opcion: ")
	return op

def menuModGestionReportes():
	print("Menu de Gestion de Reportes")
	print("\ta. Ver reportes")
	print("\tb. Volver\n")

	op = input("Seleccione la opcion: ")
	return op
	
# MENUS ADMINISTRADOR
def menuPrincipalAdministrador():
	print("Menu Principal del administrador con id",reg.id)
	print("\t1. Gestionar usuarios")
	print("\t2. Gestionar Reportes")
	print("\t3. Reportes Estadísticos")
	print("\t4. Listado de estudiantes con puntaje")
	print("\t0. Salir \n")

	op = int(input("Seleccione la opcion: "))
	return op

def menuAdmGestionUsuarios():
	print("Menu de Gestion de Usuarios")
	print("\ta. Eliminar un usuario (incluyendo moderadores)")
	print("\tb. Dar de alta un moderador")
	print("\tc. Desactivar usuario")
	print("\td. Volver\n")

	op = input("Seleccione la opcion: ")
	return op

def menuAdmGestionReportes():
	print("Menu de Gestion de Reportes")
	print("\ta. Ver reportes")
	print("\tb. Volver\n")

	op = input("Seleccione la opcion: ")
	return op

# FUNCIONES ESTUDIANTE
def ingresarNacimiento():
	fecha = input("Formato (año-mes-dia)\nxxxx-xx-xx\nIngrese la fecha de nacimiento: ")
	while len(fecha) != 10:
		limpiarConsola()
		print("La longitud de la fecha es incorrecta\n")
		fecha = input("Formato (año-mes-dia)\nxxxx-xx-xx\nIngrese la fecha de nacimiento: ")
	limpiarConsola()
	return fecha

def mostrarDatosEstudiantes():
	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 
	while (ar_logico.tell() < longitud_archivo):
		reg_temp = pickle.load(ar_logico)
		if(reg_temp.id != reg.id):
			print("ID de estudiante: ",reg_temp.id)
			print("\tNombre:", reg_temp.nombre)
			print("\tFecha de Nacimiento:", reg_temp.nacimiento)
			print("\tEdad:", calcularEdad(reg_temp.nacimiento))
			print("\tBiografia:", reg_temp.bio)
			print("\tHobbies: {} \n" .format(reg_temp.hobbies))
	ar_logico.close()
			
def nombreCorrecto(nombre):
	id_nombre_buscado = -1;

	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 
	while (ar_logico.tell() < longitud_archivo):
		reg_temp = pickle.load(ar_logico)
		if(nombre == reg_temp.nombre.lower()):
			if(reg.id == reg_temp.id):
				print("No puedes seleccionarte a ti mismo!\n")
			else:
				id_nombre_buscado = reg_temp.id
	
	ar_logico.close()
	return id_nombre_buscado
def agregarMatcheo():
	print("Desea dar like a un usuario?\n\t1. Si\n\t0. No\n")
	opcion_like = int(input("Selecciona la opción: "))
	
	if(opcion_like==1):
		me_gusta = input("\nIngrese el nombre de la persona con la que le gustaria hacer un matcheo: ")
		limpiarConsola()

		me_gusta_id = nombreCorrecto(me_gusta.lower().ljust(30))
		if(me_gusta_id > -1):	
			ar_fisico, ar_logico = abrirPorTipo(4)
			longitud_archivo = os.path.getsize(ar_fisico) 
			like_repetido = False

			while (ar_logico.tell() < longitud_archivo and not like_repetido):
				like_temp = pickle.load(ar_logico)
				if(like_temp.id_remitente == reg.id and like_temp.id_destinatario == me_gusta_id):
					print("Ya le has dado like a", me_gusta, "\n")
					like_repetido = True
			if not like_repetido:
				like_n = like(); like_n.id_remitente = reg.id; like_n.id_destinatario = me_gusta_id
				ar_logico.seek(longitud_archivo, 0)
				pickle.dump(like_n, ar_logico)
				ar_logico.flush()
				ar_logico.close()
				print("Seleccionaste a {}, espero te corresponda!\n".format(me_gusta))	
		else:
			print("El nombre ingresado no es correcto\n")
	else:
		limpiarConsola()

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
			reg.email = input("Ingrese un nuevo email: ").ljust(45)			
		case 2:
			reg.contrasena = input("Ingrese un nuevo contraseña: ").ljust(30)
		case 3:
			reg.nombre = input("Ingrese un nuevo nombre: ").ljust(30)
		case 4:
			reg.nacimiento = ingresarNacimiento().ljust(10)
		case 5:
			reg.hobbies = input("Ingrese un nuevo hobbie: ").ljust(150)
		case 6:
			reg.bio = input("Ingrese una nueva biografia: ").ljust(150)
		case 7:
			reg.sexo = input("Ingrese un nuevo sexo: ").ljust(10)
		case _: 
			limpiarConsola()
			print("Opción incorrecta.\n")
	if opcion_editar >= 1 and opcion_editar <= 7:
		limpiarConsola()	
	actualizarRegistro(reg,1)

def eliminarMiPerfil():
	tipo_ses = 1
	print("Desea eliminar su perfil?")
	print("\t1. Si")
	print("\t0. No\n")
	opcion_eliminar = int(input("Selecciona la opción: "))
	limpiarConsola()

	match opcion_eliminar:
		case 1:
			reg.estado = False
			tipo_ses = 0

			# SE DEBERIAN ELIMINAR LOS LIKES?

			actualizarRegistro(reg,1)
			
		case 0:
			limpiarConsola()
		case _: 
			limpiarConsola()
			print("Opción incorrecta.\n")
	return tipo_ses

def reportar():
	rep = reporte()
	rep.id_reportante = reg.id
	rep.id_reportado = pedirNombreID()
	if(rep.id_reportado == -1):
		limpiarConsola()
		print("Usuario no encontrado\n")
	elif(rep.id_reportante == rep.id_reportado):
		limpiarConsola()
		print("No te puedes reportar a ti mismo\n")
	else:
		rep.motivo = input("Ingrese el motivo de su reporte: ").ljust(150)
		limpiarConsola()
		ar_fisico, ar_logico = abrirPorTipo(5)
		longitud_archivo = os.path.getsize(ar_fisico) 
		ar_logico.seek(longitud_archivo, 0) 
		pickle.dump(rep, ar_logico)
		ar_logico.flush()
		ar_logico.close()
		print("Reporte enviado\n")

# FUNCIONES MODERADOR
def desactivarID(idd):
	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 
	reg_est = pickle.load(ar_logico)
	while (ar_logico.tell() < longitud_archivo and reg_est.id != idd):
		reg_est = pickle.load(ar_logico)
	ar_logico.close()
	reg_est.estado = False 

	# SE DEBERIAN ELIMINAR LOS LIKES?

	actualizarRegistro(reg_est,1)

def desactivarUsuario():
	id_desactivado = pedirNombreID()
	if(id_desactivado == -1):
		limpiarConsola()
		print("Usuario no encontrado\n")
	else:
		print("Desea desactivar al usuario con id",id_desactivado,"definitivamente?")
		print("\t1. Si")
		print("\t0. No\n")
		opcion_desactivar = int(input("Selecciona la opción: "))
		limpiarConsola()
		if(opcion_desactivar == 1):
			desactivarID(id_desactivado)
			print("Se ha deshabilitado al usuario\n")

def obtenerNombre(idd):
	art_fisico, art_logico = abrirPorTipo(1)
	longitudt_archivo = os.path.getsize(art_fisico) 

	while (art_logico.tell() < longitudt_archivo):
		reg_temp = pickle.load(art_logico)
		if(idd == reg_temp.id):
			nombre = reg_temp.nombre
	art_logico.close()
	return nombre
def verReportes():
	ar_fisico, ar_logico = abrirPorTipo(5)
	longitud_archivo = os.path.getsize(ar_fisico) 
	longitud_registro = lenRegistro(5)
	i = 0
	while (ar_logico.tell() < longitud_archivo):
		i = i + 1
		rep = pickle.load(ar_logico)
		if(rep.estado == 0):
			print("Reporte",i)
			print("\tReportante:", obtenerNombre(rep.id_reportante).strip(), "ID:",rep.id_reportante)
			print("\tReportado:", obtenerNombre(rep.id_reportado).strip(), "ID:",rep.id_reportado)
			print("\tMotivo:", rep.motivo, "\n")
			opcion_reporte = input("Seleccione como se quiere proceder:\n\ta) Ignorar reporte\n\tb) Bloquear al reportado\nOpcion: ")

			match opcion_reporte:
				case 'a':
					rep.estado = 2
					limpiarConsola()
					print("Se ignoro el reporte.\n\n")
					if(tipo_sesion == 2):
						reg.reportes_ignorados = reg.reportes_ignorados + 1
						actualizarRegistro(reg, 2)

				case 'b':
					rep.estado = 1
					desactivarID(rep.id_reportado)
					limpiarConsola()
					print("Se bloqueo al reportado.\n\n")
					if(tipo_sesion == 2):
						reg.reportes_aceptados = reg.reportes_aceptados + 1
						actualizarRegistro(reg, 2)

				case _:
					limpiarConsola()
					print("Opción incorrecta.\n")
			
			ar_logico.seek(ar_logico.tell()-longitud_registro)
			pickle.dump(rep, ar_logico)
			ar_logico.flush()

	ar_logico.close()

	print("No hay nuevos reportes por mostrar.\n")

#FUNCIONES ADMIN
def pedirIDModerador():
    id_moderador = -1
    ar_fisico, ar_logico = abrirPorTipo(2)
    longitud_archivo = os.path.getsize(ar_fisico)

    id_posible_moderador = int(input("\nIngrese la ID del moderador: "))
    cant_moderadores = cantRegistros(2, False)

    if id_posible_moderador >= cant_moderadores:
        print("\nID no encontrado.\n")
    else:
        while ar_logico.tell() < longitud_archivo:
            reg_temp = pickle.load(ar_logico)
            if id_posible_moderador == reg_temp.id:
                id_moderador = reg_temp.id

    ar_logico.close()
    return int(id_moderador)

def desactivarModeradorID(id_moderador):
    ar_fisico, ar_logico = abrirPorTipo(2)
    longitud_archivo = os.path.getsize(ar_fisico)
    
    reg_mod = pickle.load(ar_logico)
    while ar_logico.tell() < longitud_archivo and reg_mod.id != id_moderador:
        reg_mod = pickle.load(ar_logico)
    
    ar_logico.close()

    if(reg_mod.id == id_moderador):
    	reg_mod.estado = False
    	actualizarRegistro(reg_mod, 2)
def eliminarModerador():
	id_mod = pedirIDModerador()
	if id_mod == -1:
		limpiarConsola()
		print("Moderador no encontrado\n\n")
	else:
		print("Desea desactivar al moderador con id",id_mod,"definitivamente?")
		print("\t1. Si")
		print("\t0. No\n")
		op_desactivar = int(input("Selecciona la opción: "))
		limpiarConsola()
		if(op_desactivar == 1):
			desactivarModeradorID(id_mod)
			print("Se ha deshabilitado el moderador")
def eliminaUsuario():
	print("1. Estudiante")
	print("2. Moderador\n")
	op_elimina = int(input("Seleccione cual:"))
	limpiarConsola()
	match op_elimina:
		case 1:
			desactivarUsuario()
		case 2:
			eliminarModerador()
		case _:
			print("Opcion incorrecta")

def porcentajeIgnorados():
    ar_fisico, ar_logico = abrirPorTipo(5) 
    cantidad_ignorados = 0
    total_reportes = cantRegistros(5,False)
    longitud_archivo = os.path.getsize(ar_fisico)

    while ar_logico.tell() < longitud_archivo:
        reg_reporte = pickle.load(ar_logico)
        if reg_reporte.estado == 2:  
            cantidad_ignorados = cantidad_ignorados + 1

    ar_logico.close()
    porcentaje_ignorados = (cantidad_ignorados / total_reportes) * 100
    return porcentaje_ignorados
def porcentajeAceptados():
    ar_fisico, ar_logico = abrirPorTipo(5) 
    cantidad_aceptados = 0
    total_reportes = cantRegistros(5,False)
    longitud_archivo = os.path.getsize(ar_fisico)

    while ar_logico.tell() < longitud_archivo:
        reg_reporte = pickle.load(ar_logico)
        if reg_reporte.estado == 1:
            cantidad_aceptados = cantidad_aceptados + 1

    ar_logico.close()
    porcentaje_aceptados = (cantidad_aceptados / total_reportes) * 100
    return porcentaje_aceptados
def moderadorReporteIgnorados():
    ar_fisico, ar_logico = abrirPorTipo(2)
    mayor_ignorados = -1
    moderador_id = -1
    longitud_archivo = os.path.getsize(ar_fisico)

    while ar_logico.tell() < longitud_archivo:
        reg_mod = pickle.load(ar_logico)
        if reg_mod.reportes_ignorados > mayor_ignorados:
            mayor_ignorados = reg_mod.reportes_ignorados
            moderador_id = reg_mod.id

    ar_logico.close()
    return moderador_id, mayor_ignorados
def moderadorReporteAceptados():
    ar_fisico, ar_logico = abrirPorTipo(2) 
    mayor_aceptados = -1
    moderador_id = -1
    longitud_archivo = os.path.getsize(ar_fisico)

    while ar_logico.tell() < longitud_archivo:
        reg_mod = pickle.load(ar_logico)
        if reg_mod.reportes_aceptados > mayor_aceptados:
            mayor_aceptados = reg_mod.reportes_aceptados
            moderador_id = reg_mod.id

    ar_logico.close()
    return moderador_id, mayor_aceptados
def moderadorReporteProcesados():
    ar_fisico, ar_logico = abrirPorTipo(2) 
    mayor_procesados = -1
    moderador_id = -1
    longitud_archivo = os.path.getsize(ar_fisico)

    while ar_logico.tell() < longitud_archivo:
        reg_mod = pickle.load(ar_logico)
        total_procesados = reg_mod.reportes_ignorados + reg_mod.reportes_aceptados
        if total_procesados > mayor_procesados:
            mayor_procesados = total_procesados
            moderador_id = reg_mod.id

    ar_logico.close()
    return moderador_id, mayor_procesados
def mostrarReportesEstadisticos():
	total_reportes = cantRegistros(5,False)
	if(total_reportes != 0):
		reportes_ignorados = porcentajeIgnorados()
		reportes_aceptados = porcentajeAceptados()
		mod_ignorado, cant_ignorados = moderadorReporteIgnorados()
		mod_aceptado, cant_aceptados = moderadorReporteAceptados()
		mod_procesado, cant_procesado = moderadorReporteProcesados()

		print("Cantidad de reportes realizados por los estudiantes: ",total_reportes)
		print(f"Porcentaje de reportes ignorados: {reportes_ignorados:.2f}%")
		print(f"Porcentaje de reportes aceptados: {reportes_aceptados:.2f}%\n")
		print("El moderador con mayor cantidad de reportes ignorados ID:", mod_ignorado,"(con", cant_ignorados, "reportes)")
		print("El moderador con mayor cantidad de reportes aceptados ID:", mod_aceptado,"(con", cant_aceptados, "reportes)")
		print("El moderador con mayor cantidad de reportes procesados ID:", mod_procesado,"(con", cant_procesado, "reportes)\n\n")
	else:
		print("Los estudiantes todavia no generaron ningun reporte\n\n")

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

def likeValido(lik):
	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 

	valido = True
	while (ar_logico.tell() < longitud_archivo and valido):
		reg_temp = pickle.load(ar_logico)
		if(not reg_temp.estado and (reg_temp.id == lik.id_destinatario or reg_temp.id == lik.id_remitente)):
			valido = False
			
	ar_logico.close()
	return valido

def reporteEstadisticoPropio():
	match = 0
	likes_dados_no_recibidos = 0
	likes_recibidos_no_dados = 0
	cant_posibles_match = cantRegistros(1,True) - 1

	ids_likes_dados = [0] * cant_posibles_match 
	ar_fisico, ar_logico = abrirPorTipo(4)
	longitud_archivo = os.path.getsize(ar_fisico)

	while (ar_logico.tell() < longitud_archivo):
		like_temp = pickle.load(ar_logico)
		if(reg.id == like_temp.id_remitente and likeValido(like_temp)):
			ids_likes_dados[likes_dados_no_recibidos] = like_temp.id_destinatario
			likes_dados_no_recibidos = likes_dados_no_recibidos + 1

	ar_logico.seek(0,0)
	while (ar_logico.tell() < longitud_archivo):
		like_temp = pickle.load(ar_logico)
		if(reg.id == like_temp.id_destinatario and likeValido(like_temp)):
			likes_recibidos_no_dados = likes_recibidos_no_dados + 1
			for i in range(likes_dados_no_recibidos):
				if(ids_likes_dados[i] == like_temp.id_remitente):
					ids_likes_dados[i] = ids_likes_dados[likes_dados_no_recibidos - 1] # Hay que salvar el ultimo dato porque el for será de uno menos
					likes_dados_no_recibidos = likes_dados_no_recibidos - 1 
					likes_recibidos_no_dados = likes_recibidos_no_dados - 1
					match = match + 1
				
	ar_logico.close()
	
	porcentaje_matcheos_posibles = match / cant_posibles_match * 100 

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

	op = int(input("Seleccione la opcion: "))
	return op	
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

def puntajeCandidato(id_estudiante):
	puntaje = 0
	
	likes_dados = 0
	cant_posibles_match = cantRegistros(1,True) - 1

	ids_likes_dados = [0] * cant_posibles_match 
	ar_fisico, ar_logico = abrirPorTipo(4)
	longitud_archivo = os.path.getsize(ar_fisico)

	while (ar_logico.tell() < longitud_archivo):
		like_temp = pickle.load(ar_logico)
		if(id_estudiante == like_temp.id_remitente and likeValido(like_temp)):
			ids_likes_dados[likes_dados] = like_temp.id_destinatario
			likes_dados = likes_dados + 1

	racha = 0
	for i in range(likes_dados):
		puntaje = puntaje - 1
		ar_logico.seek(0,0)
		perdio_racha = True
		while (ar_logico.tell() < longitud_archivo):
			like_temp = pickle.load(ar_logico)
			if(ids_likes_dados[i] == like_temp.id_remitente and id_estudiante == like_temp.id_destinatario and likeValido(like_temp)):
				puntaje = puntaje + 2
				racha = racha + 1
				perdio_racha = False
				if(racha >= 3):
					puntaje = puntaje + 1
		if(perdio_racha):
			racha = 0

	ar_logico.close()
	return puntaje
def listadoPuntaje():
	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 
	while (ar_logico.tell() < longitud_archivo):
		reg_temp = pickle.load(ar_logico)
		print("ID de estudiante: ",reg_temp.id)
		print("\tNombre:", reg_temp.nombre)
		print("\tPuntaje:",puntajeCandidato(reg_temp.id),"\n")
	ar_logico.close()

def superLike():
	print("Estos son los candidatos para dar el Super-like\n")
	mostrarDatosEstudiantes()  
	id_candidato = int(input("\n\nIngrese el id del estudiante: "))
	if(id_candidato >= cantRegistros(1,False) or id_candidato == reg.id):
		limpiarConsola()
		print("El id no es correcto\n")
	else:
		ar_fisico, ar_logico = abrirPorTipo(4) 
		longitud_archivo = os.path.getsize(ar_fisico)
		like_dado = False
		like_recibido = False

		while ar_logico.tell() < longitud_archivo:
			like_temp = pickle.load(ar_logico)
			if like_temp.id_remitente == reg.id and like_temp.id_destinatario == id_candidato:
				like_dado = True
			if like_temp.id_remitente == id_candidato and like_temp.id_destinatario == reg.id:
				like_recibido = True
			
		like_n = like()
		ar_logico.seek(longitud_archivo, 0)
		if not like_dado:
			like_n.id_remitente = reg.id
			like_n.id_destinatario = id_candidato
			pickle.dump(like_n, ar_logico)
			ar_logico.flush()
			
		if not like_recibido:
			like_n.id_remitente = id_candidato
			like_n.id_destinatario = reg.id
			pickle.dump(like_n, ar_logico) 
			ar_logico.flush()

			limpiarConsola()
			print(f"¡Has dado un Super-like a {id_candidato}! ¡Ahora tienen un match!\n")
			
		ar_logico.close()

def recibioLikeSinDar(id_enamorado):
	ar_fisico, ar_logico = abrirPorTipo(4)
	longitud_archivo = os.path.getsize(ar_fisico)
	ignorado = True
	enamorado = False

	while ar_logico.tell() < longitud_archivo:
		like_temp = pickle.load(ar_logico)
		if like_temp.id_remitente == reg.id and like_temp.id_destinatario == id_enamorado:
			ignorado = False
		if like_temp.id_remitente == id_enamorado and like_temp.id_destinatario == reg.id:
			enamorado = True

	ar_logico.close()
	return enamorado and ignorado
def revelarCandidatos():
				
	unEnamorado = False
	ar_fisico, ar_logico = abrirPorTipo(1)
	longitud_archivo = os.path.getsize(ar_fisico) 
	
	print("Estos son los candidatos que te han dado like y no han sido correspondidos:\n")
	while (ar_logico.tell() < longitud_archivo):
		reg_temp = pickle.load(ar_logico)
		
		if(recibioLikeSinDar(reg_temp.id)):
			print("ID de estudiante: ",reg_temp.id)
			print("Nombre:", reg_temp.nombre)
			print("Fecha de Nacimiento:", reg_temp.nacimiento)
			print("Edad:", calcularEdad(reg_temp.nacimiento))
			print("Biografia:", reg_temp.bio)
			print("Hobbies: {} \n" .format(reg_temp.hobbies))
			unEnamorado = True
	
	ar_logico.close()
		
	if(not unEnamorado):
		print("No hay candidatos :(")
		print("Nadie que no hayas likeado busca hacer un matcheo contigo.\n")

##############################################################
crearArchivos()
if(os.path.getsize(arclik_fisico)==0):
	likesAuto()

opcion_inicio = -1
limpiarConsola()
while(opcion_inicio != 0):
	tipo_sesion = 0 # 0 ninguna # 1 estudiante # 2 moderador # 3 administrador
	opcion_inicio = -1
	while(opcion_inicio != 0 and opcion_inicio != 1):

		opcion_inicio = menuInicio()
		limpiarConsola()
		match opcion_inicio:
			case 1:
				cant_estudiantes = cantRegistros(1,True)
				if(cant_estudiantes < 4):
					print("No hay la cantidad de estudiantes necesarios para iniciar el programa, se necesitan", 4 - cant_estudiantes, "más.\n")
				elif(cantRegistros(2,True) < 1):
					print("No hay la cantidad de moderadores necesarios para iniciar el programa, se necesita al menos uno.\n")
				elif(cantRegistros(3,False) < 1):
					print("No hay la cantidad de administradores necesarios para iniciar el programa, se necesita al menos uno.\n")	
				else:
					tipo_sesion, reg = login()

			case 2:
				registro(1)

			case 11:
				ruletaAfinidad()
			case 21:
				edades()
			case 22:
				matcheosCombinados(cantRegistros(1,True))

			case 0:
				print("Adios!")
			case _:
				print("Opción incorrecta.\n")

	opcion = -1 # Porque tiene que ser distinto de 0 para entrar al while
	while(opcion != 0 and tipo_sesion == 1): # Estudiante

		opcion = menuPrincipalEstudiante()
		limpiarConsola()
		match opcion:
			case 1:
				opcion_perfil = ''
				while(opcion_perfil != 'c' and tipo_sesion == 1):
					opcion_perfil = menuGestionPerfil()
					limpiarConsola()
					match opcion_perfil:
						case 'a':
							editarDatos() 

						case 'b':
							tipo_sesion = eliminarMiPerfil()

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
							reportar()
							
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
							print("Ver Matcheos aún no realizado.\n")
						case 'b':
							print("Eliminar un Matcheo aún no realizado.\n")
						case 'c':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")		

			case 4:
				reporteEstadisticoPropio()

			case 32:
				if(reg.superlike_disponible):
					superLike()
				reg.superlike_disponible = False
				actualizarRegistro(reg,1)

			case 33:
				if(reg.revelarcandidato_disponible):
					revelarCandidatos()
				reg.revelarcandidato_disponible = False
				actualizarRegistro(reg,1)
				
			case 0:
				print("Sesión finalizada.\n")
			case _:
				print("Opcion incorrecta")	 

	while(opcion != 0 and tipo_sesion == 2): # Moderador
		
		opcion = menuPrincipalModerador()
		limpiarConsola()
		match opcion:
			case 1:
				opcion_gest_usuarios = ''
				while(opcion_gest_usuarios != 'b'):
					opcion_gest_usuarios = menuModGestionUsuarios()
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
					opcion_gest_reportes = menuModGestionReportes()
					limpiarConsola()
					match opcion_gest_reportes:
						case 'a':
							verReportes()

						case 'b':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")
			
			case 3:
				mostrarReportesEstadisticos()

			case 0:
				print("Sesión finalizada.\n")
			case _:
				print("Opcion incorrecta")	 


	while(opcion != 0 and tipo_sesion == 3): # Administrador

		opcion = menuPrincipalAdministrador()
		limpiarConsola()
		match opcion:
			case 1:
				opcion_gest_usuarios = ''
				while(opcion_gest_usuarios != 'd'):
					opcion_gest_usuarios = menuAdmGestionUsuarios()
					limpiarConsola()
					match opcion_gest_usuarios:
						case 'a':
							eliminaUsuario()

						case 'b':
							registro(2)

						case 'c':
							desactivarUsuario()	#muy parecieda al a opcion A, raro

						case 'd':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")

			case 2:
				opcion_gest_reportes = ''
				while(opcion_gest_reportes != 'b'):
					opcion_gest_reportes = menuAdmGestionReportes()
					limpiarConsola()
					match opcion_gest_reportes:
						case 'a':
							verReportes()

						case 'b':
							limpiarConsola() #volver
						case _:
							print("Opción incorrecta.\n")

			case 3:
				mostrarReportesEstadisticos()

			case 4:
				listadoPuntaje()

			case 0:
				print("Sesión finalizada.\n")
			case _:
				print("Opcion incorrecta")	 