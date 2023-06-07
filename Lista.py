from Nodo import *
from Vehiculo_Nuevo import *
from Vehiculo_Usado import *

class Lista(object):
	def __init__(self):
		self.__comienzo = None
		
	def AgregarVehiculo(self,vehiculo):
		nodo = Nodo(vehiculo)
		nodo.setSiguiente(self.__comienzo)
		self.__comienzo = nodo

	def Ingresar_Vehiculo_Posicion(self,posicion,vehiculo):
		aux=self.__comienzo

		for i in range(posicion):
			anterior = aux
			aux = aux.getSiguiente()

		nuevonodo = Nodo(vehiculo)
		anterior.setSiguiente(nuevonodo)
		nuevonodo.setSiguiente(aux)

	def Muestra_Posicion(self,posicion):
		i = 1
		aux = self.__comienzo

		while ((i < posicion) and (aux != None)):
			aux = self.__comienzo.getSiguiente()
			i+=1

		if i == posicion:
			if isinstance(aux.getDato(),Vehiculo_Nuevo):
				print("El auto es nuevo!")
			elif isinstance(aux.getDato(),Vehiculo_Usado):
				print("El auto es usado!")
		else:
			print("Posicion no encontrada!")


	def Modifica(self,patente):
		band = False
		aux = self.__comienzo
		while aux != None and band == False:
			vehiculo = aux.getDato()
			if isinstance(vehiculo,Vehiculo_Usado):
				if patente == vehiculo.getPatente():
					precio = float(input("Ingrese nuevo precio: "))
					vehiculo.setPrecio(precio)
					print("Precio de venta: ",vehiculo.Importe_Venta())
					band = True

			aux = aux.getSiguiente()
		if aux == None:
			print("Patente no encontrada!")

	def Busco_Economico(self):
		minimo = 9999999
		aux = self.__comienzo
		retorno = None
		while aux != None:
			vehiculo = aux.getDato()
			if vehiculo.Importe_Venta() < minimo:
				retorno = vehiculo
				minimo = vehiculo.Importe_Venta()
			aux = aux.getSiguiente()
		return retorno

	def Muestra(self):
		aux = self.__comienzo
		while aux != None:
			aux.getDato().MuestraDatos()
			aux = aux.getSiguiente()

	def toJSON(self):
		aux=self.__comienzo
		listanormal=[]
		while aux != None:
			listanormal.append(aux.getDato())
			aux=aux.getSiguiente()
		d=dict(
			__class__="Lista",
			vehiculos=[vehiculo.toJSON() for vehiculo in listanormal]
		)
		return d