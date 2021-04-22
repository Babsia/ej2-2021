import csv
from Viajeros import viajerofrecuente
class Manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def CargarLista(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            viajero=viajerofrecuente(fila[0],fila[1],fila[2],fila[3],int(fila[4]))
            self.__lista.append(viajero)
    def buscar(self,num):
        for i in range(len(self.__lista)):
            if (self.__lista[i].getnum()==num):
                return self.__lista[i]
    
    def ConsultaMillas(self,num):
        return (self.buscar(num).cantitotalmillas())
    def Acumular(self,num,millas):
        self.buscar(num).acumulador(millas)
    def Canjear(self,num,millas):
        self.buscar(num).canjearmillas(millas)

        
        
