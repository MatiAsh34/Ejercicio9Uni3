from Lista import *
from Vehiculo import *
from Vehiculo_Nuevo import *
from Vehiculo_Usado import *
from ObjectEncoder import *

if __name__ == '__main__':
	Lista_Enlazada = Lista()
	JsonF = ObjectEncoder()
	diccionario = JsonF.leerJSONArchivo('vehiculos.json')
	Lista_Enlazada = JsonF.decodificarDiccionario(diccionario)

	opcion = None
	while opcion != '0':
		print("\n1- Insertar un vehículo en la colección en una posición determinada.")
		print("2- Agregar un vehículo a la colección.")
		print("3- Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
		print("4- Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
		print("5- Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
		print("6- Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
		print("7- Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”.")
		print("0- Salir")

		opcion = input("\nIngrese codigo: ")

		if opcion == '1':
 			print("\n 1-Nuevo ---- 2-Usado ")
 			tipo = input("\nIngrese tipo de auto: ")
 			modelo = input("Inserte modelo: ")
 			cantidad_puertas = input("Inserte cantidad de puertas: ")
 			color = input("Inserte color: ")
 			precio_base = float(input("Inserte precio base: "))
 			
 			if tipo == '1':
 				marca = 'Toyota'
 				version = input("Inserte version: ")
 				vehiculo = Vehiculo_Nuevo(modelo,cantidad_puertas,color,precio_base,marca,version)

 			if tipo == '2':
 				marca = input("Inserte marca: ")
 				patente = input("Inserte patente: ")
 				año = int(input("Inserte años: "))
 				kilometraje = float(input("Inserte kilometraje: "))
 				vehiculo = Vehiculo_Usado(modelo,cantidad_puertas,color,precio_base,marca,patente,año,kilometraje)

 			posicion = int(input("\nIngrese la posicion: "))-1
 			Lista_Enlazada.Ingresar_Vehiculo_Posicion(posicion,vehiculo)

		elif opcion == '2':
			print("\n 1-Nuevo ---- 2-Usado ")
			tipo = input("\nIngrese tipo de auto: ")
			modelo = input("Inserte modelo: ")
			cantidad_puertas = input("Inserte cantidad de puertas: ")
			color = input("Inserte color: ")
			precio_base = float(input("Inserte precio base: "))
			
			if tipo == '1':
				marca = 'Toyota'
				version = input("Inserte version: ")
				vehiculo = Vehiculo_Nuevo(modelo,cantidad_puertas,color,precio_base,marca,version)

			if tipo == '2':
				marca = input("Inserte marca: ")
				patente = input("Inserte patente: ")
				año = int(input("Inserte años: "))
				kilometraje = float(input("Inserte kilometraje: "))
				vehiculo = Vehiculo_Usado(modelo,cantidad_puertas,color,precio_base,marca,patente,año,kilometraje)

			Lista_Enlazada.AgregarVehiculo(vehiculo)

		elif opcion == '3':
 			posicion = int(input("Inserte posicion: "))
 			Lista_Enlazada.Muestra_Posicion(posicion)

		elif opcion == '4':
 			patente = input("Inserte patente: ")
 			Lista_Enlazada.Modifica(patente)

		elif opcion == '5':
 			vehiculo_economico = Lista_Enlazada.Busco_Economico()
 			if vehiculo_economico != None:
 				if isinstance(vehiculo_economico,Vehiculo_Nuevo):
 					vehiculo_economico.Mostrar()

		elif opcion == '6':
 			Lista_Enlazada.Muestra()

		elif opcion == '7':
			d=Lista_Enlazada.toJSON()
			JsonF.guardarJSONArchivo(d,'vehiculosnuevos.json')

		elif opcion == '0':
 			print("Saliendo...")
