from colorama import Fore, Style, init
import random

init(autoreset=True) # Para que el color no se imprima en la linea siguente

print('Ingrese tus numero de la suerte del 0 al 99')

numeroDelusuario = []

for x in range(6):
    while True:
        numero_usuario = input(f'Número {x+1}: ')
        if numero_usuario.isdigit() and 0 <= int(numero_usuario) <= 99:
            numero_usuario_02 = f"{int(numero_usuario):02d}"
            numeroDelusuario.append(numero_usuario_02)
            break
        else:
            print(Fore.RED + '👀 El Diablo que es eso 🔊 Por favor ingrese un numero entre 0 y 99')

numero_loteria = random.sample(range(0, 99), 6)
numero_loteria_02 = [f"{n:02d}" for n in numero_loteria]

colores_usuario = []
for i in range(6):
    color = Fore.GREEN if numeroDelusuario[i] == numero_loteria_02[i] else Fore.RED
    colores_usuario.append(color + numeroDelusuario[i] + Style.RESET_ALL)

aciertos = 0 
for i in range(6):
    if numeroDelusuario[i] == numero_loteria_02[i]:
        #print({numeroDelusuario[i]} == {numero_loteria_02[i]})
        aciertos += 1
    else:
        #print(f"{numeroDelusuario[i]} ≠ {numero_loteria_02[i]}")
        pass


print()
print("Tus números:        " + " ".join(colores_usuario))
print("Números ganadores:  " + " ".join(numero_loteria_02))
print(f"Aciertos por orden: {aciertos}")
