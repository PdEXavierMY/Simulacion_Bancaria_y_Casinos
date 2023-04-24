'''
Un banco necesita controlar el acceso a cuentas bancarias y para ello desea hacer un programa de prueba en Java que permita lanzar procesos que ingresen y retiren dinero a la vez y comprobar así si el resultado final es el esperado.

Se parte de una cuenta con 100 euros y se pueden tener procesos que ingresen 100 euros, 50 o 20. También se pueden tener procesos que retiran 100, 50 o 20 euros euros. Se desean tener los siguientes procesos:

40 procesos que ingresan 100

20 procesos que ingresan 50

60 que ingresen 20.

De la misma manera se desean lo siguientes procesos que retiran cantidades.

40 procesos que retiran 100

20 procesos que retiran 50

60 que retiran 20.

Se desea comprobar que tras la ejecución la cuenta tiene exactamente 100 euros, que era la cantidad de la que se disponía al principio.'''

from cuenta_bancaria import CuentaBancaria, Ingresar, Retirar
    

def main():
    cuenta = CuentaBancaria(100)
    hilos = []
    for i in range(40):
        hilos.append(Ingresar(cuenta, 100))
    for i in range(20):
        hilos.append(Ingresar(cuenta, 50))
    for i in range(60):
        hilos.append(Ingresar(cuenta, 20))
    for i in range(40):
        hilos.append(Retirar(cuenta, 100))
    for i in range(20):
        hilos.append(Retirar(cuenta, 50))
    for i in range(60):
        hilos.append(Retirar(cuenta, 20))
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()
    print(cuenta.get_cantidad())

if __name__ == '__main__':
    main()