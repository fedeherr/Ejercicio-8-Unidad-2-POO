from Conjuntos import Conjuntos
class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.unionConjuntos,
                            2:self.diferenciaConjuntos,
                            3:self.igualdadConjuntos,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Chao')
    def unionConjuntos(self):
        Conjunto = Conjuntos()
        otroConjunto = Conjuntos()
        band = False
        print('Unión')
        while (not band):
            a = int(input("Ingrese un valor del primer conjunto: "))
            Conjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = True
        while (band):
            a = int(input("Ingrese un valor del segundo conjunto "))
            otroConjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = False
        Conjunto + otroConjunto
        print ("Resultado de la suma: ", Conjunto)

    def diferenciaConjuntos(self):
        Conjunto = Conjuntos()
        otroConjunto = Conjuntos()
        band = False
        print('Diferencia')
        while (not band):
            a = int(input("Ingrese un valor del primer conjunto: "))
            Conjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = True
        while (band):
            a = int(input("Ingrese un valor del segundo conjunto "))
            otroConjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = False
        Conjunto - otroConjunto
        print ("Resultado de la resta: ", Conjunto)
    def igualdadConjuntos(self):
        Conjunto = Conjuntos()
        otroConjunto = Conjuntos()
        band = False
        print('Igualdad')
        while (not band):
            a = int(input("Ingrese un valor del primer conjunto: "))
            Conjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = True
        while (band):
            a = int(input("Ingrese un valor del segundo conjunto "))
            otroConjunto + a
            b = input("Sí termino de ingresar, ingrese x ")
            if (b == 'x'): band = False
        if(Conjunto == otroConjunto): print ("Son iguales")
        else: print("Son distintos")