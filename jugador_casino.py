import threading
import time
import random

class Jugador(threading.Thread):
    def __init__(self, ruleta, nombre, saldo):
        threading.Thread.__init__(self)
        self.ruleta = ruleta
        self.nombre = nombre
        self.saldo = saldo
    def run(self):
        while self.saldo > 0:
            time.sleep(3)
            self.ruleta.tirar()
            print(self.nombre + " ha sacado el " + str(self.ruleta.get_numero()))
            self.jugar()
    def jugar(self):
        pass
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, cantidad):
        self.saldo = cantidad
    def incrementar_saldo(self, cantidad):
        self.saldo += cantidad
    def decrementar_saldo(self, cantidad):
        self.saldo -= cantidad

