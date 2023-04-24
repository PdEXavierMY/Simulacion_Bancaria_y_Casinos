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

class JugadorNumero(Jugador):
    def __init__(self, ruleta, nombre, saldo):
        Jugador.__init__(self, ruleta, nombre, saldo)
        self.numero = random.randint(1, 36)
    def jugar(self):
        if self.ruleta.get_numero() == self.numero:
            self.ruleta.incrementar_banca(360)
            self.incrementar_saldo(360)
            print(self.nombre + " ha ganado 360€")
        else:
            self.ruleta.decrementar_banca(10)
            self.decrementar_saldo(10)
            print(self.nombre + " ha perdido 10€")

