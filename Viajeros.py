class viajerofrecuente:
    __numero=''
    __dni=''
    __nombre=''
    __apellido=''
    __Macum=0
    def __init__(self,numero='',dni='',nombre='',apellido='',millas=0):
        self.__numero=numero
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__Macum=millas

    def cantitotalmillas(self):
        return self.__Macum
    def getnum(self):
        return self.__numero
    def acumulador(self,milla):
        self.__Macum+=milla
    def canjearmillas(self,millas):
        if (millas<=self.__Macum):
            self.__Macum-=millas
        else:
            print("fallo en la operacion")


