from colorama import Fore, Style, Back, init
import os
import random
import json

init(autoreset=True)


numeroDelusuario = []
historial = {
    "resultados":[
        
    ], 
}

try:
    with open("historial.json", "r") as archivo:
        historial = json.load(archivo)
except FileNotFoundError:
    historial = {"resultados": []}

def guardar_historial_en_el_json():
    with open("historial.json", "w") as file:
        json.dump(historial, file, indent=4)

def limpiarConsola():
    os.system("cls" if os.name == "nt" else "clear")

def enterParaContinuar(mensaje: str = Fore.BLUE + Style.BRIGHT + "Enter para continuar..."):
    input(mensaje)


def generar_boleto():
    return [f"{random.randint(0, 49):02d}" for _ in range(6)]

def generar_nunmeros_ganadores():
    return [f"{random.randint(0, 99):02d}" for _ in range(6)]

def menudel1():
    limpiarConsola()
    while True:
        print(Fore.WHITE + Back.BLUE + "=" * 50)
        print(Fore.WHITE + Back.BLUE + "="  + Style.RESET_ALL + Fore.MAGENTA + " "* 15 + "Elige tus numeros" + " " *16 + Style.RESET_ALL + Fore.WHITE + Back.BLUE + "="  + Style.RESET_ALL )
        print(Fore.WHITE + Back.BLUE + "=" * 50)

        print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "Ingresar tus numeros de la suerte" + Style.RESET_ALL + " "*10 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
        print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "2. " + Fore.WHITE + "Boletos" + Style.RESET_ALL + " "*36 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
        print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "3. " + Fore.WHITE + "Regresar" + Style.RESET_ALL + " "*35 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    
        print(Fore.WHITE + Back.BLUE + "=" * 50)

        print("")
        opcion = input(Fore.MAGENTA + "Seleccione una opción: " + Style.RESET_ALL)
         
        if opcion == "1":
            global numeroDelusuario
            print(Fore.MAGENTA + "¿Cuántas veces deseas jugar (cantidad de boletos)?" + Style.RESET_ALL)
            while True:
                try:
                    cantidad_juegos = int(input(Fore.CYAN + "Cantidad de boletos: " + Fore.WHITE + Style.RESET_ALL))
                    if cantidad_juegos:
                        cantidad_juegos_int = int(cantidad_juegos)
                        if 0 < cantidad_juegos_int >= 20:
                            cantidad_juegos = cantidad_juegos_int
                        break
                    else:
                        print(Fore.RED + "🛑 Mano no sea asi, digite un numero que sea mayor que 0 <= 20." + Style.RESET_ALL)
                    enterParaContinuar()
                except:
                    print(Fore.RED + "🛑 Mano no sea asi, digite un numero que sea mayor que 0 <= 20." + Style.RESET_ALL) 
                enterParaContinuar()
            limpiarConsola()   
            
            for i in range(1, cantidad_juegos + 1):
                print(Fore.CYAN + f"\nJugada {i}: Ingresa tus 6 números de la suerte (del 0 al 49)" + Style.RESET_ALL)
                numeros_de_jugadas = []

                for x in range(6):
                    while True:
                        numero_usuario = input(Fore.MAGENTA + f'Número {x+1}: ' + Style.RESET_ALL)
                        if numero_usuario.isdigit() and 0 <= int(numero_usuario) <= 49:
                            numero_usuario_02 = f"{int(numero_usuario):02d}"
                            numeros_de_jugadas.append(numero_usuario_02)
                            break
                        else:
                            print(Fore.RED + "👀 El Diablo que es eso 🔊 Por favor ingrese un numero entre 0 y 49" + Style.RESET_ALL) 
                
                numeroDelusuario.append(numeros_de_jugadas)
                print(Fore.GREEN + "Jugada registrada:", ", ".join(numeros_de_jugadas))

            print(Fore.MAGENTA + "\nTodos tus boletos:")
            for num, boleto in enumerate(numeroDelusuario, 1):
                print(f"Boleto {num}: {', '.join(boleto)}")

            enterParaContinuar()
            limpiarConsola()

        elif opcion == "2":
            while True:
                print("SI no tienes numeros favorito aca te dejo algunos ;3")
                boletos = [generar_boleto() for _ in range(5)]

                for i, boleto in enumerate(boletos, 1):
                    print(f"Boleto {i}: {', '.join(boleto)}")

                seleccion = input("\n¿Con cuáles boletos deseas jugar? (Ej: 1,3,5) o escribe 'cambiar' para generar nuevos: ").strip()

                if seleccion.lower() == "cambiar":
                    print("\n🔄 Generando nuevos boletos...")
                    continue

                indices_validos = []
                try:
                    indices = [int(i.strip()) for i in seleccion.split(',')]
                    for i in indices:
                        if 1 <= i <= 5:
                            indices_validos.append(i - 1)
                        else:
                            raise ValueError
                except ValueError:
                    print(Fore.RED + "Entrada no válida. Intenta de nuevo con un formato como: 1,3,5 o escribe 'cambiar'." + Style.RESET_ALL)
                    continue

                boletos_seleccionados = [boletos[i] for i in indices_validos]
                numeroDelusuario.extend(boletos_seleccionados)

                print("Has elegido jugar con los siguientes boletos:")
                for i, boleto in enumerate(boletos_seleccionados, 1):
                    print(f"Boleto {i}: {', '.join(boleto)}")

                print(Fore.GREEN + "\nBoletos registrados correctamente.")
                enterParaContinuar()
                limpiarConsola()
                break  
        elif opcion == "3":
            break
        else:
            print(Fore.RED + "👀 El Diablo que es eso 🔊 sea serio hermano")
            enterParaContinuar()
        limpiarConsola()

def numeros_ganadores():
    global numeroDelusuario
    if not numeroDelusuario:
        print(Fore.RED + "No tienes boletos para comparar. Primero ingresa tus números.")
        enterParaContinuar()
        return

    while True:
        veces = input(Fore.CYAN + "\n¿Cuántas veces quieres jugar cada boleto contra combinaciones aleatorias? " + Style.RESET_ALL)
        if veces.isdigit() and int(veces) > 0:
            veces = int(veces)
            break
        else:
            print(Fore.RED + "🚫 Ingresa un número válido mayor que 0.")

    print(Fore.MAGENTA + f"\n🎯 Comparando {len(numeroDelusuario)} boletos contra {veces} combinaciones ganadoras...\n")

    temporal = {"ganadores":[]}
    for juego in range(1, veces + 1):
        
        print(Fore.YELLOW + f"\n🔔 Juego {juego}")
        numero_loteria = random.sample(range(0, 49), 6)
        numero_loteria_02 = [f"{n:02d}" for n in numero_loteria]
        
        print("Números ganadores: " + " ".join(numero_loteria_02))
        print("-" * 50)

        for idx, boleto in enumerate(numeroDelusuario, 1):
            colores_usuario = []
            aciertos = 0
            for i in range(6):
                color = Fore.GREEN if boleto[i] == numero_loteria_02[i] else Fore.RED
                colores_usuario.append(color + boleto[i] + Style.RESET_ALL)
                if boleto[i] == numero_loteria_02[i]:
                    aciertos += 1

            print(f"Boleto {idx}:        " + " ".join(colores_usuario))
            print(f"Aciertos por orden: {aciertos}")
            print("-" * 40)
            temporal["ganadores"].append({"ganador":numero_loteria_02,"boleto":boleto, "acierto": aciertos, "juego": juego})
    historial["resultados"].append(temporal)
    print(historial["resultados"])
    guardar_historial_en_el_json()
    enterParaContinuar()

def mostrar_historial():
    if not historial["resultados"]:
        print(Fore.YELLOW + "📭 No hay historial aún.")
        enterParaContinuar()
        return

    print(Fore.MAGENTA + "\n📜 Historial de Juegos:\n")

    for entrada in historial["resultados"]:
        for registro in entrada["ganadores"]:
            juego = registro["juego"]
            numeros_ganadores = registro["ganador"]
            boleto = registro["boleto"]
            aciertos = registro["acierto"]

            print(Fore.YELLOW + f"\n🎯 Juego {juego}")
            print("Números ganadores: " + " ".join(numeros_ganadores))

            colores_usuario = []
            for i in range(6):
                color = Fore.GREEN if boleto[i] == numeros_ganadores[i] else Fore.RED
                colores_usuario.append(color + boleto[i] + Style.RESET_ALL)

            print("Tu boleto:          " + " ".join(colores_usuario))
            print(f"Aciertos por orden: {aciertos}")
            print("-" * 50)

    enterParaContinuar()

def reglasDeLaloteria():
    print(Fore.WHITE + Back.BLUE + "=" * 50)
    print(Fore.WHITE + Back.BLUE + "=" + Style.RESET_ALL + Fore.MAGENTA + Style.BRIGHT + " " * 10 + "📝 Reglas de la loteria 🤑" + " " * 12 + Style.RESET_ALL + Fore.WHITE + Back.BLUE + "=" ) 
    print(Fore.WHITE + Back.BLUE + "=" * 50)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "Eleccion de Numeros." + Style.RESET_ALL + " "*6 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*4 + Fore.MAGENTA + Style.BRIGHT + "·" + Fore.WHITE + "Cada jugador selecciona una combinación de números únicos dentro de un rango predefinido \n (por ejemplo, del 1 al 40)." + Style.RESET_ALL + " "*6 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "El jugador elige sus numeros al azar." + Style.RESET_ALL + " "*6 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "El jugador elige sus numeros al azar." + Style.RESET_ALL + " "*6 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "El jugador elige sus numeros al azar." + Style.RESET_ALL + " "*6 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)

    enterParaContinuar()

def mostrarMenu():
    print(Fore.WHITE + Back.BLUE + "=" * 50)
    print(Fore.WHITE + Back.BLUE + "="  + Style.RESET_ALL + Fore.MAGENTA + " " * 15 + "Loteria de Kaneki" + " " *16 + Style.RESET_ALL + Fore.WHITE + Back.BLUE + "="  + Style.RESET_ALL )
    print(Fore.WHITE + Back.BLUE + "=" * 50)

    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "1. " + Fore.WHITE + "Elige tus numeros" + Style.RESET_ALL + " "*26 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "2. " + Fore.WHITE + "Numeros Ganadores" + Style.RESET_ALL + " "*26 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "3. " + Fore.WHITE + "Premios" + Style.RESET_ALL + " "*36 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "4. " + Fore.WHITE + "Historial de juego" + Style.RESET_ALL + " "*25 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "5. " + Fore.WHITE + "Reglas de la loteria" + Style.RESET_ALL + " "*23 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    print(Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL + " "*2 + Fore.MAGENTA + Style.BRIGHT + "6. " + Fore.WHITE + "Salir" + Style.RESET_ALL + " "*38 + Fore.WHITE + Back.BLUE + "|" + Style.RESET_ALL)
    
    print(Fore.WHITE + Back.BLUE + "=" * 50)
    
    print("")
    opcion = input(Fore.MAGENTA + "Seleccione una opción: " + Style.RESET_ALL)
    return opcion

if __name__ == "__main__":
    while True:
        limpiarConsola()
        opcion = mostrarMenu()
        if opcion == "1":
            menudel1()
        if opcion == "2":
            numeros_ganadores()
        if opcion == "3":
            pass
        if opcion == "4":
            mostrar_historial()
        if opcion == "5":
            reglasDeLaloteria()
        elif opcion == "6":
            print("chao")
            break
        else:
            print(Fore.RED + "👀 El Diablo que es eso 🔊 sea serio hermano")
            enterParaContinuar()
    