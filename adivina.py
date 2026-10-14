import random
import argparse


def play_game(low=1, high=100, max_attempts=None):
    secret = random.randint(low, high)
    attempts = 0
    print(f"He elegido un número entre {low} y {high}. ¡Adivina! (escribe 'salir' para terminar)")

    while True:
        guess = input("Tu intento: ").strip()
        if guess.lower() in ("salir", "q", "quit"):
            print("Juego terminado. ¡Hasta luego!")
            return

        try:
            guess_num = int(guess)
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")
            continue

        attempts += 1

        if guess_num < secret:
            print("Demasiado bajo.")
        elif guess_num > secret:
            print("Demasiado alto.")
        else:
            print(f"¡Correcto! Adivinaste el número en {attempts} intentos.")
            break

        if max_attempts is not None and attempts >= max_attempts:
            print(f"Se acabaron los intentos. El número era {secret}.")
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Juego: Adivina el número")
    parser.add_argument("--min", type=int, default=1, help="Valor mínimo (por defecto 1)")
    parser.add_argument("--max", type=int, default=100, help="Valor máximo (por defecto 100)")
    parser.add_argument("--attempts", type=int, default=None, help="Intentos máximos (opcional)")
    args = parser.parse_args()

    if args.min >= args.max:
        raise SystemExit("Error: --min debe ser menor que --max.")

    play_game(args.min, args.max, args.attempts)