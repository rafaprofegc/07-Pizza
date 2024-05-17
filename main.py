from Pizza import Pizza

def main():
    p = Pizza( "G", True)
    p.añade_ingrediente("PI")
    p.añade_ingrediente("PE")
    p.añade_ingrediente("AT")
    p.añade_ingrediente("PO")
    p.añade_ingrediente("MO")
    p.añade_ingrediente("AC")

    p.quitar_ingrediente("PE")
    p.quitar_ingrediente("AT")

    print(f"Precio de la pizza: {p.calcular_precio()} €")



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
