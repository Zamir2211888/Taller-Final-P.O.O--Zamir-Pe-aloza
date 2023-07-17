#Ejercicio 3 Zamir Peñaloza/2211888

class Vuelo:
    def __init__(self, numero, origen, destino, capacidad):
        self.numero = numero
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad
        self.asientos = self.generar_asientos()

    def generar_asientos(self):
        letras = ['A', 'B', 'C', 'D', 'E', 'F']
        asientos = []
        for fila in range(1, self.capacidad // len(letras) + 1):
            for letra in letras:
                asientos.append(str(fila) + letra)
        return asientos

    def mostrar_asientos_disponibles(self):
        return self.asientos_disponibles

    def realizar_reserva(self, pasajero, asiento):
        if asiento in self.asientos:
            self.asientos.remove(asiento)
            self.asientos_disponibles -= 1
            reserva = Reserva(pasajero, self.numero, asiento)
            return reserva
        else:
            return None
        
    #Metodo Nuevo     
    def mostrar_informacion(self):
        print(f"Número de vuelo: {self.numero}")
        print(f"Origen: {self.origen}")
        print(f"Destino: {self.destino}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Asientos disponibles: {self.asientos_disponibles}")



class Pasajero:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Reserva:
    def __init__(self, pasajero, numero_vuelo, asiento):
        self.pasajero = pasajero
        self.numero_vuelo = numero_vuelo
        self.asiento = asiento


# Ejemplo de uso
vuelo1 = Vuelo("001", "Ciudad A", "Ciudad B", 100)
vuelo2 = Vuelo("002", "Ciudad B", "Ciudad C", 200)

pasajero1 = Pasajero("Zamir", "David")
pasajero2 = Pasajero("Patricia", "Peñaloza")

reserva1 = vuelo1.realizar_reserva(pasajero1, "1A")
if reserva1:
    print(f"Reserva realizada para el pasajero {reserva1.pasajero.nombre} en el vuelo {reserva1.numero_vuelo}, asiento {reserva1.asiento}")
else:
    print("El asiento seleccionado no está disponible.")

reserva2 = vuelo1.realizar_reserva(pasajero2, "1A")
if reserva2:
    print(f"Reserva realizada para el pasajero {reserva2.pasajero.nombre} en el vuelo {reserva2.numero_vuelo}, asiento {reserva2.asiento}")
else:
    print("El asiento seleccionado no está disponible.")

reserva3 = vuelo2.realizar_reserva(pasajero2, "2B")
if reserva3:
    print(f"Reserva realizada para el pasajero {reserva3.pasajero.nombre} en el vuelo {reserva3.numero_vuelo}, asiento {reserva3.asiento}")
else:
    print("El asiento seleccionado no está disponible.")

print(f"Asientos disponibles en vuelo 1: {vuelo1.mostrar_asientos_disponibles()}")
print(f"Asientos disponibles en vuelo 2: {vuelo2.mostrar_asientos_disponibles()}")

vuelo1.mostrar_informacion()
vuelo2.mostrar_informacion()