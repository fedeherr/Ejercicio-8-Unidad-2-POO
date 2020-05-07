class Conjuntos:
    __conjunto = []
    def __init__(self):
        self.__conjunto = []
    def getConjunto(self):
        return self.__conjunto
    def __str__(self):
        return str(self.__conjunto)
    def __add__(self, otroConjunto):
        if (isinstance(otroConjunto, Conjuntos)):
            self.__conjunto.extend(otroConjunto.getConjunto())
        else:
            if (isinstance(otroConjunto, int)):
                self.__conjunto.append(otroConjunto)
    def __sub__(self, otroConjunto):
        if (isinstance(otroConjunto, Conjuntos)):
            for i in range(len(otroConjunto.getConjunto())):
                if (otroConjunto.getConjunto()[i] in self.__conjunto):
                    self.__conjunto.remove(otroConjunto.getConjunto()[i])
        else:
            if (isinstance(otroConjunto, int)):
                if (otroConjunto in self.__conjunto):
                    self.__conjunto.remove(otroConjunto[i])        
    def __eq__(self, otroConjunto):
        a = 0
        tam = len(self.__conjunto)
        if (len(otroConjunto.getConjunto()) == tam):
            for i in range(len(otroConjunto.getConjunto())):
                if (otroConjunto.getConjunto()[i] in self.__conjunto):
                    a = a + 1
        else: return(False)
        if (a == tam): return(True)
        



if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Union de dos conjuntos
              2 Diferencia de dos conjuntos
              3 Igualdad entre dos conjuntos""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0