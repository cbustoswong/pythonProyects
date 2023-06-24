import random


def seleccionar_palabras():
  palabras = ["python", "programacion", "ahorcado", "computadora", "juego"]
  palabra = random.choice(palabras)
  return palabra


def mostrar_tablero(palabra_secreta, letras_adivinadas):
  tablero = ""
  for letra in palabra_secreta:
    if letra in letras_adivinadas:
      tablero += letra + " "
    else:
      tablero += "_ "
  return tablero


def jugar_ahorcado():
  palabra_secreta = seleccionar_palabras()
  letras_adivinadas = []
  intentos = 6

  print("¡Bienvenido al juego del ahorcado!")
  print(mostrar_tablero(palabra_secreta, letras_adivinadas))

  while True:
    if intentos == 0:
      print("¡Oh no! Has perdido. La palabra secreta era:", palabra_secreta)
      break

    letra = input("Ingresa una letra: ").lower()

    if letra in letras_adivinadas:
      print("Ya has ingresado esa letra. Intenta con otra.")
      continue

    letras_adivinadas.append(letra)

    if letra not in palabra_secreta:
      intentos -= 1
      print("Letra incorrecta. Te quedan", intentos, "intentos.")

    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    if all(letra in letras_adivinadas for letra in palabra_secreta):
      print("¡Felicitaciones! Has adivinado la palabra:", palabra_secreta)
      break


jugar_ahorcado()
