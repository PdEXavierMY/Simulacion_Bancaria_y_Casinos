import random
import threading

class Ruleta:
    def __init__(self):
        self.lock = threading.Lock()
        self.numero = 0
        self.banca = 50000
    def get_numero(self):
        return self.numero
    def get_banca(self):
        return self.banca
    def set_numero(self, numero):
        self.numero = numero
    def set_banca(self, cantidad):
        self.banca = cantidad
    def tirar(self):
        self.lock.acquire()
        self.numero = random.randint(0, 36)
        self.lock.release()
    def incrementar_banca(self, cantidad):
        self.lock.acquire()
        self.banca += cantidad
        self.lock.release()
    def decrementar_banca(self, cantidad):
        self.lock.acquire()
        self.banca -= cantidad
        self.lock.release()