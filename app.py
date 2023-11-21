import random

def jugar_piedra_papel_tijeras():
    opciones = ["piedra", "papel", "tijeras"]
    puntaje = {"jugador": 0, "oponente": 0}

    while True:
        print("\nElige: piedra, papel o tijeras")
        eleccion_jugador = input("Tu elección: ").lower()

        if eleccion_jugador not in opciones:
            print("¡Opción no válida! Por favor, elige piedra, papel o tijeras.")
            continue

        eleccion_oponente = random.choice(opciones)
        print("El oponente elige:", eleccion_oponente)

        resultado = determinar_ganador(eleccion_jugador, eleccion_oponente)

        if resultado == "Ganaste":
            puntaje["jugador"] += 1
        elif resultado == "Perdiste":
            puntaje["oponente"] += 1

        print("Resultado:", resultado)
        print("Puntaje - Jugador: {}, Oponente: {}".format(puntaje["jugador"], puntaje["oponente"]))

        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
            print("¡Gracias por jugar! Puntaje final - Jugador: {}, Oponente: {}".format(puntaje["jugador"], puntaje["oponente"]))
            break

def determinar_ganador(eleccion_jugador, eleccion_oponente):
    if eleccion_jugador == eleccion_oponente:
        return "Empate"
    elif (eleccion_jugador == "piedra" and eleccion_oponente == "tijeras") or \
         (eleccion_jugador == "tijeras" and eleccion_oponente == "papel") or \
         (eleccion_jugador == "papel" and eleccion_oponente == "piedra"):
        return "Ganaste"
    else:
        return "Perdiste"

# Iniciar el juego
jugar_piedra_papel_tijeras()