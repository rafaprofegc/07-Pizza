class Pizza():

    # Variables de clase
    CON_BORDE_RELLENO = 3.15

    TAMAÑOS = { "M": ["Mediana",8.5],
                "G": ["Grande", 10.15],
                "F": ["Familiar", 14.75]
              }

    INGREDIENTES = { "PI": ["Pimiento", 0.75],
                     "CH": ["Champiñon", 1.15],
                     "AT": ["Atún", 1.55],
                     "PE": ["Peperoni", 2.15],
                     "ES": ["Espinacas", 1.85],
                     "PO": ["Pollo", 1.95],
                     "TE": ["Ternera", 2.25],
                     "AC": ["Aceitunas", 0.85],
                     "JA": ["Jamón", 3.05],
                     "MO": ["Mozzarela", 2.35]
                   }

    # Inicializador
    def __init__(self, tamaño:str, con_borde_relleno: bool):
        self.__tamaño = self.__set_tamaño(tamaño)
        self.__ingredientes = {}
        self.__con_borde_relleno = con_borde_relleno

    # Método para establecer el tamaño
    def __set_tamaño(self, tamaño:str) -> None:
        if tamaño not in Pizza.TAMAÑOS:
            raise KeyError("El tamaño no es correcto")

        self.__tamaño = tamaño

    # Métodos getter y setter
    @property
    def tamaño(self) -> str:
        return self.__tamaño

    @tamaño.setter
    def tamaño(self, tamaño: str):
        self.__set_tamaño(tamaño)

    @property
    def ingredientes(self) -> dict:
        return self.__ingredientes

    @property
    def con_borde_relleno(self) -> bool:
        return self.__con_borde_relleno

    @con_borde_relleno.setter
    def con_border_relleno(self, con_borde: bool):
        self.__con_borde_relleno = con_borde

    def __presenta_ingredientes(self, actuales: bool = True) -> None:
        # Recorro el diccionario de ingredientes
        if actuales:
            print("Ingredientes actualmente en la pizza")
            ingredientes = self.__ingredientes.values()
        else:
            print("Los ingredientes disponibles para la pizza")
            ingredientes = Pizza.INGREDIENTES.values()

        print("Ingrediente".ljust(15) + "Precio".rjust(6))
        print("-" * (15 + 6))
        for ingrediente in ingredientes:
            linea = f"{ingrediente[0]}".ljust(15) + \
                    f"{ingrediente[1]} €".rjust(6)

            print(linea)

    # Métodos para añadir y quitar ingredientes
    def añade_ingrediente(self, ingrediente: str) -> bool:
        if ingrediente.upper() in self.__ingredientes:
            print("El ingrediente ya está en la pizza. NO se puede añadir")
            return False

        if ingrediente.upper() in self.INGREDIENTES:
            print(f"Añadiendo {Pizza.INGREDIENTES[ingrediente.upper()][0]} a la pizza")
            self.__ingredientes[ ingrediente.upper() ] = Pizza.INGREDIENTES[ingrediente.upper()]
            return True
        else:
            raise KeyError("El ingrediente NO EXISTE")


    def quitar_ingrediente(self, ingrediente: str) -> bool:
        if ingrediente.upper() in self.__ingredientes:
            ing = self.__ingredientes.pop(ingrediente.upper())
            print(f"El ingrediente {ing[0]} se ha eliminado")
            return True
        else:
            raise KeyError("El ingrediente no está actualmente en la pizza")


    # Calculamos el precio de la pizza
    def calcular_precio(self) -> float:
        print(f"La pizza tiene tamaño: {Pizza.TAMAÑOS[self.__tamaño][0]}. "
              f"Precio base {Pizza.TAMAÑOS[self.__tamaño][1]} €")

        if self.__con_borde_relleno:
            print(f"La pizza tiene el borde relleno de queso. Incremento de {Pizza.CON_BORDE_RELLENO} €")
        else:
            print("La pizza NO tiene los bordes rellenos de queso")

        self.__presenta_ingredientes()

        precio = Pizza.TAMAÑOS[self.__tamaño][1]
        for ingrediente in self.__ingredientes.values():
            precio += ingrediente[1]

        if self.__con_borde_relleno:
            precio += Pizza.CON_BORDE_RELLENO

        return precio
