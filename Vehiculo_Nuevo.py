from Vehiculo import Vehiculo


class Vehiculo_Nuevo(Vehiculo):
	def __init__(self,modelo,cantidad_puertas,color,precio_base,marca,version):
		super().__init__(modelo,cantidad_puertas,color,precio_base,marca)
		self.__version = version

	def toJSON(self):
		d = dict(
			__class__=self.__class__.__name__,
			__atributos__ = dict(
				modelo = self.getModelo(),
				cantidad_puertas = self.getCantidad_Puertas(),
				color = self.getColor(),
				precio_base = self.getPrecio(),
				marca = self.getMarca(),
				version = self.__version
				)
			)
		return d

	def Importe_Venta(self):
		importe = self.getPrecio() + self.getPrecio() * 0.10
		if self.__version == 'Full':
			importe = importe + self.getPrecio() * 0.02
		return importe

	def Mostrar(self):
		super().Mostrar()
		print("Version: {}".format(self.__version))
