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