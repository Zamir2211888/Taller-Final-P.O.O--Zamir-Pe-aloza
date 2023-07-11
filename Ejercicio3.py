#Ejercicio 3 Zamir Peñaloza/2211888

class Usuario:
    def __init__(self, nombre, cc, edad):
        self.nombre = nombre 
        self.cc = cc
        self.edad = edad 

class Vuelo(Usuario):
    def __init__(self) -> None:
        pass


class Pasajero(Usuario):
    def __init__(self) -> None:
        pass
    
    
class Reserva(Usuario):
    def __init__(self) -> None:
        pass