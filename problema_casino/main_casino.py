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

if __name__ == '__main__':
    main()