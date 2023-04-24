# Simulacion_Bancaria_y_Casinos


[Este](https://github.com/Xavitheforce/Simulacion_Bancaria_y_Casinos) es el enlace a mi repositorio.

<h6>El ejercicio 1 es el siguiente:</h6>

""" Un banco necesita controlar el acceso a cuentas bancarias y para ello desea hacer un programa de prueba en python(unitt test, dock test o mock test) que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado.

Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

40 procesos que ingresan 100

20 procesos que ingresan 50

60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

40 procesos que retiran 100

20 procesos que retiran 50

60 que retiran 20.

Se desea comprobar que tras la ejecución la cuenta tiene exactamente 100 euros, que era la cantidad de la que se disponía al principio. """

<br>

El código empleado para resolverlo es el siguiente:


Cuenta Bancaria:
```py
import multiprocessing

class CuentaBancaria:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.lock = multiprocessing.Lock()
    def ingresar(self, cantidad):
        self.cantidad += cantidad
        print("Ingresando " + str(cantidad) + "€")
    def retirar(self, cantidad):
        self.cantidad -= cantidad
        print("Retirando " + str(cantidad) + "€")
    def get_cantidad(self):
        return self.cantidad
    
class Ingresar(multiprocessing.Process):
    def __init__(self, cuenta, cantidad):
        multiprocessing.Process.__init__(self)
        self.cuenta = cuenta
        self.cantidad = cantidad
    def run(self):
        self.cuenta.lock.acquire()
        self.cuenta.ingresar(self.cantidad)
        self.cuenta.lock.release()

class Retirar(multiprocessing.Process):
    def __init__(self, cuenta, cantidad):
        multiprocessing.Process.__init__(self)
        self.cuenta = cuenta
        self.cantidad = cantidad
    def run(self):
        self.cuenta.lock.acquire()
        self.cuenta.retirar(self.cantidad)
        self.cuenta.lock.release()
```
El ejercicio también tiene en su archivo correspondiente la solución con hilos (debido a un error de lectura inicial).


Main cuenta bancaria:
```py
from problema_banco.cuenta_bancaria import CuentaBancaria, Ingresar, Retirar
    

def main():
    cuenta = CuentaBancaria(100)
    procesos = []
    for i in range(40):
        procesos.append(Ingresar(cuenta, 100))
    for i in range(20):
        procesos.append(Ingresar(cuenta, 50))
    for i in range(60):
        procesos.append(Ingresar(cuenta, 20))
    for i in range(40):
        procesos.append(Retirar(cuenta, 100))
    for i in range(20):
        procesos.append(Retirar(cuenta, 50))
    for i in range(60):
        procesos.append(Retirar(cuenta, 20))
    for hilo in procesos:
        hilo.start()
    for hilo in procesos:
        hilo.join()
    print("Balance final de cuenta = "+str(cuenta.get_cantidad())+"€")
```


<h6>El ejercicio 2 es el siguiente:</h6>

""" Se desea simular los posibles beneficios de diversas estrategias de juego en un casino. La ruleta francesa es un juego en el que hay una ruleta con 37 números (del 0 al 36). Cada 3000 milisegundos el croupier saca un número al azar y los diversos hilos apuestan para ver si ganan. Todos los hilos empiezan con 1.000 euros y la banca (que controla la ruleta) con 50.000. Cuando los jugadores pierden dinero, la banca incrementa su saldo.

Se puede jugar a un número concreto. Habrá 4 hilos que eligen números al azar del 1 al 36 (no el 0) y restarán 10 euros de su saldo para apostar a ese ese número. Si sale su número su saldo se incrementa en 360 euros (36 veces lo apostado).

Se puede jugar a par/impar. Habrá 4 hilos que eligen al azar si apuestan a que saldrá un número par o un número impar. Siempre restan 10 euros para apostar y si ganan incrementan su saldo en 20 euros.

Se puede jugar a la «martingala». Habrá 4 hilos que eligen números al azar. Elegirán un número y empezarán restando 10 euros de su saldo para apostar a ese número. Si ganan incrementan su saldo en 360 euros. Si pierden jugarán el doble de su apuesta anterior (es decir, 20, luego 40, luego 80, y así sucesivamente)

La banca acepta todas las apuestas pero nunca paga más dinero del que tiene.

Si sale el 0, todo el mundo pierde y la banca se queda con todo el dinero. """

<br>

El código empleado para resolverlo es el siguiente:


Banca:
```py
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
```


Jugador Casino:
```py
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
            print(self.nombre + " ha seleccionado el " + str(self.ruleta.get_numero()))
            self.jugar()
        print(self.nombre + " ha perdido todo su dinero, por lo que se retira del casino")
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
            self.ruleta.decrementar_banca(360)
            self.incrementar_saldo(360)
            print(self.nombre + " ha ganado 360€")
        else:
            self.ruleta.incrementar_banca(10)
            self.decrementar_saldo(10)
            print(self.nombre + " ha perdido 10€")

class JugadorParImpar(Jugador):
    def __init__(self, ruleta, nombre, saldo):
        Jugador.__init__(self, ruleta, nombre, saldo)
        self.par = random.choice([True, False])
    def jugar(self):
        if self.ruleta.get_numero() == 0:
            self.ruleta.incrementar_banca(self.get_saldo())
            self.set_saldo(0)
            print(self.nombre + " ha perdido todo su dinero")
        elif self.par and self.ruleta.get_numero() % 2 == 0:
            self.ruleta.decrementar_banca(20)
            self.incrementar_saldo(20)
            print(self.nombre + " ha ganado 20€")
        elif not self.par and self.ruleta.get_numero() % 2 != 0:
            self.ruleta.decrementar_banca(20)
            self.incrementar_saldo(20)
            print(self.nombre + " ha ganado 20€")
        else:
            self.ruleta.incrementar_banca(10)
            self.decrementar_saldo(10)
            print(self.nombre + " ha perdido 10€")

class JugadorMartingala(Jugador):
    def __init__(self, ruleta, nombre, saldo):
        Jugador.__init__(self, ruleta, nombre, saldo)
        self.numero = random.randint(1, 36)
        self.apuesta = 10
    def jugar(self):
        if self.ruleta.get_numero() == self.numero:
            self.ruleta.decrementar_banca(self.apuesta * 36)
            self.incrementar_saldo(self.apuesta * 36)
            print(self.nombre + " ha ganado " + str(self.apuesta * 36) + "€")
            self.apuesta = 10
        else:
            self.ruleta.incrementar_banca(self.apuesta)
            self.decrementar_saldo(self.apuesta)
            print(self.nombre + " ha perdido " + str(self.apuesta) + "€")
            self.apuesta *= 2
```


Main Casino:
```py
from problema_casino.jugador_casino import JugadorNumero, JugadorParImpar, JugadorMartingala
from problema_casino.banca import Ruleta


def main():
    ruleta = Ruleta()
    jugadores = []
    for i in range(4):
        jugadores.append(JugadorNumero(ruleta, "Jugador " + str(i), 100))
        jugadores.append(JugadorParImpar(ruleta, "Jugador " + str(i), 100))
        jugadores.append(JugadorMartingala(ruleta, "Jugador " + str(i), 100))
    for jugador in jugadores:
        jugador.start()
    for jugador in jugadores:
        jugador.join()
    print("La banca tiene " + str(ruleta.get_banca()) + "€")
```

El archivo que se encarga de controlar la ejecución de ambos ejercicos es el main global:

```py
from problema_banco.main_cuenta_bancaria import main as main_banco
from problema_casino.main_casino import main as main_casino

def main():
    eleccion = input("¿Qué problema quieres ejecutar? (1/2): ")
    if eleccion == "1":
        main_banco()
    elif eleccion == "2":
        main_casino()
    else:
        print("Opción no válida")

if __name__ == '__main__':
    main()
```
