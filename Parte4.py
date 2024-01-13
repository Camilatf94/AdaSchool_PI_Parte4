# MAPA DEL LABERINTO #

# Librerias utilizadas en el proyecto
import os
from typing import List, Tuple
import readchar
from readchar import readkey, key

nombre = input('introduce tu nombre: ')
print('Bienvenido' + nombre + '!')

# Mapa del laberinto
laberinto = """..###################
    ....#...............#
    #.#.#####.#########.#
    #.#...........#.#.#.#
    #.#####.#.###.#.#.#.#
    #...#.#.#.#.....#...#
    #.#.#.#######.#.#####
    #.#...#.....#.#...#.#
    #####.#####.#.#.###.#
    #.#.#.#.......#...#.#
    #.#.#.#######.#####.#
    #...#...#...#.#.#...#
    ###.#.#####.#.#.###.#
    #.#...#.......#.....#
    #.#.#.###.#.#.###.#.#
    #...#.#...#.#.....#.#
    ###.#######.###.###.#
    #.#.#.#.#.#...#.#...#
    #.#.#.#.#.#.#.#.#.#.#
    #.....#.....#.#.#.#.#
    ###################.."""

# Funcion que transforma una cadena en una matriz de caracteres con el punto de separacion dado segun el mapa
def transformar_matriz(laberinto):
    # Dividir el laberinto en filas
    filas = laberinto.split('\n    ')

    # Crear la matriz de caracteres
    matriz = [list(fila) for fila in filas]

    return matriz

# Llama a la funcion y guarda el resultado en una variable para reutilizar
mapa = transformar_matriz(laberinto)

# Inicializacion de punto inicial y final de acuerdo al tamaño del mapa dado
punto_inicial = (0, 0)
punto_final = (len(mapa)-1, len(mapa[0])-1)

# Funcion que imprime el mapa en forma de matriz en la consola para visualizarlo
def vista_de_mapa(mapa):
    clear_terminal()
    for fila in mapa:
        print(''.join(fila))

# Funcion que limpia la pantalla de terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funcion main loop - Desarrollo del la parte 4 del proyecto.
def main(mapa: List[List[str]], punto_inicial: Tuple[int, int], punto_final: Tuple[int, int]):
    # Asignación de tupla de puntos iniciales a las variable eje_x y eje_y
    eje_x, eje_y = punto_inicial

    # Funcion para asignar en el mapa cargado la letra 'P' como punto de partida
    def mostrar_mapa():
        mapa[eje_x][eje_y] = 'P'
        vista_de_mapa(mapa)

    # Llamado de la funcion mostrar_mapa
    mostrar_mapa()

    # Bucle que ejecuta cuenta con las siguientes carcteristicas
    # 1. Se acaba solo cuando los valores de posicion del eje_x y eje_y son iguales cordenada final del mapa (punto_final)
    # 2. Captura la tecla presionada y si corresponde a las teclas ↑ ↓ ← → de tu teclado realiza un cambio de posicion de la letra 'P'
    while (eje_x, eje_y) != punto_final:

        # Capturar el valor de tela presionada y guardarlo en la variable pressed_key.
        pressed_key = readchar.readkey()

        # Declarar variable para nuevas coordendas con el ultomo valor de eje_x y eje_y
        nuevo_eje_x, nuevo_eje_y = eje_x, eje_y

        # Flujo de control para realizar actualizacion de la coordenada depediendo de la tecla presionada
        if pressed_key == key.UP and eje_x > 0 and mapa[eje_x - 1][eje_y] != '#':
            nuevo_eje_x -= 1
        elif pressed_key == key.DOWN and eje_x < len(mapa) - 1 and mapa[eje_x + 1][eje_y] != '#':
            nuevo_eje_x += 1
        elif pressed_key == key.LEFT and eje_y > 0 and mapa[eje_x][eje_y - 1] != '#':
            nuevo_eje_y -= 1
        elif pressed_key == key.RIGHT and eje_y < len(mapa[0]) - 1 and mapa[eje_x][eje_y + 1] != '#':
            nuevo_eje_y += 1

        # Restaura la posición anterior a '.'
        mapa[eje_x][eje_y] = '.'
        eje_x, eje_y = nuevo_eje_x, nuevo_eje_y

        # Mostrar nuevamente con la nueva posicion de la letra 'p'
        mostrar_mapa()

# Llama a la función principal con el mapa y los puntos iniciales y finales para inicializar el juego.
main(mapa, punto_inicial, punto_final)

mensaje_final = 'Felicidades'
print(mensaje_final)


