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
    print("Balance final de cuenta = "+str(cuenta.get_cantidad())+"€")

if __name__ == '__main__':
    main()