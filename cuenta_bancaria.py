import threading

class CuentaBancaria:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.lock = threading.Lock()
    def ingresar(self, cantidad):
        self.cantidad += cantidad
        print("Ingresando " + str(cantidad) + "€")
    def retirar(self, cantidad):
        self.cantidad -= cantidad
        print("Retirando " + str(cantidad) + "€")
    def get_cantidad(self):
        return self.cantidad
    
class Ingresar(threading.Thread):
    def __init__(self, cuenta, cantidad):
        threading.Thread.__init__(self)
        self.cuenta = cuenta
        self.cantidad = cantidad
    def run(self):
        self.cuenta.lock.acquire()
        self.cuenta.ingresar(self.cantidad)
        self.cuenta.lock.release()

class Retirar(threading.Thread):
    def __init__(self, cuenta, cantidad):
        threading.Thread.__init__(self)
        self.cuenta = cuenta
        self.cantidad = cantidad
    def run(self):
        self.cuenta.lock.acquire()
        self.cuenta.retirar(self.cantidad)
        self.cuenta.lock.release()