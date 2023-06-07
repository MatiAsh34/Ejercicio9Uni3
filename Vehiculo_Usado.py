from Vehiculo import Vehiculo
import datetime

class Vehiculo_Usado(Vehiculo):
	def __init__(self,modelo,cantidad_puertas,color,precio_base,marca,patente,año,kilometraje):
		super().__init__(modelo,cantidad_puertas,color,precio_base,marca)
		self.__patente = patente
		self.__año = año
		self.__kilometraje = kilometraje
		
	def getPatente(self):
		return self.__patente

	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__ = dict(
				modelo = self.getModelo(),
				cantidad_puertas = self.getCantidad_Puertas(),
				color = self.getColor(),
				precio_base = self.getPrecio(),
				marca = self.getMarca(),
				patente = self.__patente,
				año = self.__año,
				kilometraje = self.__kilometraje)
			)
		return d

	def Importe_Venta(self):
		fecha=datetime.datetime.now()
		anio_actual=fecha.year
		if self.__kilometraje>100000:
			importe=self.getPrecio()-self.getPrecio()*(0.01*(anio_actual-self.__año))-self.getPrecio()*0.02
		else:
			importe=self.getPrecio()-self.getPrecio()*(0.01*(anio_actual-self.__año))
		return importe


	def Mostrar(self):
		super().Mostrar()
		print("Patente: {}, Año: {}, Kilometraje: {}".format(self.__patente,self.__año,self.__kilometraje))