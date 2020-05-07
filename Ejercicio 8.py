from menu import Menu


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