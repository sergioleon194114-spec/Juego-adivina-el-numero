import random

# Configuración inicial del juego
secret_number = random.randint(1, 20)
max_guesses = 5
guess_count = 0

print("I'm thinking of a number between 1 and 20.")
print(f"You have {max_guesses} guesses. Good luck!")

# Bucle principal para los intentos
while guess_count < max_guesses:
    guess_count += 1
    guess = int(input(f"\nGuess #{guess_count}: "))

    # Validar el intento del jugador
    if guess == secret_number:
        print(f"Correct! You got it in {guess_count} guesses.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")
else:
    # Se ejecuta si se acaban los intentos sin adivinar
    print(f"\nOut of guesses! The number was {secret_number}.")