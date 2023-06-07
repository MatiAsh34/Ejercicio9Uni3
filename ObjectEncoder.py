import json
from pathlib import *
from Vehiculo import *
from Vehiculo_Nuevo import *
from Vehiculo_Usado import *
from Lista import *
class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Lista':
                vehiculos=d['vehiculos']
                # dvehiculos = vehiculos[0]
                lista=class_()
                for i in range(len(vehiculos)):
                    dvehiculos=vehiculos[i]
                    class_name=dvehiculos.pop('__class__')
                    class_=eval(class_name)
                    atributos=dvehiculos['__atributos__']
                    unVehiculo=class_(**atributos)
                    #unVehiculo.mostrar_datos()
                    lista.AgregarVehiculo(unVehiculo)
            return lista
            
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:json.dump(diccionario, destino, indent=4)
        destino.close()
        
    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:diccionario=json.load(fuente)
        fuente.close()
        return diccionario
    
    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)