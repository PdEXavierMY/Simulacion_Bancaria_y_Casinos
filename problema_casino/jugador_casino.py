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

class JugadorParImpar(Jugador):
    def __init__(self, ruleta, nombre, saldo):
        Jugador.__init__(self, ruleta, nombre, saldo)
        self.par = random.choice([True, False])
    def jugar(self):
        if self.ruleta.get_numero() == 0:
            self.ruleta.decrementar_banca(self.get_saldo())
            self.set_saldo(0)
            print(self.nombre + " ha perdido todo su dinero")
        elif self.par and self.ruleta.get_numero() % 2 == 0:
            self.ruleta.incrementar_banca(20)
            self.incrementar_saldo(20)
            print(self.nombre + " ha ganado 20€")
        elif not self.par and self.ruleta.get_numero() % 2 != 0:
            self.ruleta.incrementar_banca(20)
            self.incrementar_saldo(20)
            print(self.nombre + " ha ganado 20€")
        else:
            self.ruleta.decrementar_banca(10)
            self.decrementar_saldo(10)
            print(self.nombre + " ha perdido 10€")

class JugadorMartingala(Jugador):
    def __init__(self, ruleta, nombre, saldo):
        Jugador.__init__(self, ruleta, nombre, saldo)
        self.numero = random.randint(1, 36)
        self.apuesta = 10
    def jugar(self):
        if self.ruleta.get_numero() == self.numero:
            self.ruleta.incrementar_banca(self.apuesta * 36)
            self.incrementar_saldo(self.apuesta * 36)
            print(self.nombre + " ha ganado " + str(self.apuesta * 36) + "€")
            self.apuesta = 10
        else:
            self.ruleta.decrementar_banca(self.apuesta)
            self.decrementar_saldo(self.apuesta)
            print(self.nombre + " ha perdido " + str(self.apuesta) + "€")
            self.apuesta *= 2