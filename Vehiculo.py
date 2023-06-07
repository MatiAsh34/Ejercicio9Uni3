from abc import *

class Vehiculo(ABC):
	def __init__(self,modelo,cantidad_puertas,color,precio_base,marca):
		self.__modelo = modelo
		self.__cantidad_puertas = cantidad_puertas
		self.__color = color
		self.__precio_base = precio_base
		self.__marca = marca
		
	def getModelo(self):
		return self.__modelo

	def getCantidad_Puertas(self):
		return self.__cantidad_puertas

	def getColor(self):
		return self.__color

	def getPrecio(self):
		return self.__precio_base

	def getMarca(self):
		return self.__marca

	def setPrecio(self,precio):
		self.__precio_base = precio

	def Importe_Venta(self):
		pass

	def toJSON(self):
		pass

	def MuestraDatos(self):
		print("Modelo: {}, Puertas: {}".format(self.__modelo,self.__cantidad_puertas))
		print("Importe de venta: ",self.Importe_Venta())

	def Mostrar(self):
		print("Modelo: {}, Puertas: {}, Color: {}, Precio base: {}, Marca: {}".format(self.__modelo,self.__cantidad_puertas,self.__color,self.__precio_base,self.__marca))
		print("Importe de venta: ",self.Importe_Venta())

	