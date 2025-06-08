from colorama import Fore, Style, init
import random

init(autoreset=True)

print('Ingrese tus números de la suerte del 0 al 99')

numerosDelUsuario = []

# Entrada del usuario
for x in range(6):
    while True:
        numero_usuario = input(f'Número {x+1}: ')
        if numero_usuario.isdigit() and 0 <= int(numero_usuario) <= 99:
            numero_usuario_02 = f"{int(numero_usuario):02d}"
            numerosDelUsuario.append(numero_usuario_02)
            break
        else:
            print("Por favor ingrese un número válido entre 0 y 99.")

# Números aleatorios del sorteo
numero_loteria = random.sample(range(0, 7), 6)
numero_loteria_02 = [f"{n:02d}" for n in numero_loteria]

# Comparación uno a uno
aciertos = 0
print("\nResultado de la comparación:")
for i in range(6):
    usuario = numerosDelUsuario[i]
    ganador = numero_loteria_02[i]
    if usuario == ganador:
        print(Fore.GREEN + f"✔ Posición {i+1}: {usuario} == {ganador}")
        aciertos += 1
    else:
        print(Fore.RED + f"✘ Posición {i+1}: {usuario} ≠ {ganador}")

# Colorear cada número del usuario según acierto o fallo
colores_usuario = []
for i in range(6):
    color = Fore.GREEN if numerosDelUsuario[i] == numero_loteria_02[i] else Fore.RED
    colores_usuario.append(color + numerosDelUsuario[i] + Style.RESET_ALL)

# Mostrar resultados finales
print()
print("Tus números:        " + " ".join(colores_usuario))
print("Números ganadores:  " + " ".join(numero_loteria_02))
print(f"Aciertos por orden: {aciertos}")
