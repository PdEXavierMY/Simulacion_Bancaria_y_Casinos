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