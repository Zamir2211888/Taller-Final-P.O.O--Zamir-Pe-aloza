#Ejercicio 9 Zamir Peñaloza/2211888

import datetime

class Evento():
    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre 
        self.fecha = fecha 
        self.lugar = lugar 
        self.participantes = []
        self.notificaciones = []
        
    def agregar_participante(self, participante):
        self.participantes.append(participante)

    def enviar_notificacion(self, mensaje):
        notificacion = Notificacion(mensaje)
        self.notificaciones.append(notificacion)
        for participante in self.participantes:
            participante.recibir_notificacion(notificacion)
        
    def gestionar_logistica(self):
        self.reserva_lugar()
        self.coordinar_transporte()
    
    #metodos
    def reserva_lugar(self):
        print(f"Reserva el lugar del evento: {self.lugar}")
        
    def coordinar_transporte(self):
        print(f"Coordinando el transporte de los participantes")
    
    def imprimir_participantes(self):
        print(f"Participants registrados en el evento {self.nombre}")
        for participante in self.participantes:
            print(f"Nombre: {participante.nombre}, Email: {participante.email}")
        
class Participante:
    def __init__(self, nombre, email):
        self.nombre = nombre 
        self.email = email
        
    def recibir_notificacion(self, notificacion):
        print(f"Mensaje recibido por {self.nombre}: {notificacion.mensaje}")
    
        
class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje 
        self.fecha_envio = datetime.datetime.now()
    
#Ejemplo de uso de gestion de eventos
evento = Evento("Evento Congreso Sura","2023-07-24","Salon Principal")

participante1 = Participante("Zamir","zamirpenaloza@gmail.com")
participante2 = Participante("Nayla","Naylacala@gmail.com")
evento.agregar_participante(participante1)
evento.agregar_participante(participante2)

evento.enviar_notificacion("La conferencia se llevara a cabo el proximo lunes en el salon principal.")

evento.gestionar_logistica()

evento.imprimir_participantes()