#Ejercicio 9 Zamir Peñaloza/2211888

from datetime import datetime


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
        pass
        
class Participante:
    def __init__(self, nombre, email):
        self.nombre = nombre 
        self.email = email
        
    def recibir_notificacion(self, notoficacion):
        pass
    
class Notificacion:
    def __init__(self, mensaje):
        self.mensaje = mensaje 
        self.fecha_envio = datetime.datetime.now()
    
#Ejemplo de uso de gestion de eventos
