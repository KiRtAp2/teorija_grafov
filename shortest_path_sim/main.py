import math
import pygame
import graph
from algoritmi.bfs.bfs_ss_draw import bfs_step, bfs_done
from shortest_path_sim import constants, colors
from sys import exit as quit
import multiprocessing


window = pygame.display.set_mode((constants.window_width, constants.window_height))


seznam_sosednjosti = []
for i in range(constants.all_squares):
    """ konstruira posamezne sosednje elemente """

    l = []

    if i >= constants.number_of_squares[0]: l.append(i-constants.number_of_squares[0])
    # če vozlišče ni na zgornjem robu, dodaj v sosednje elemente vozlišče nad i

    if i % constants.number_of_squares[0] != 0: l.append(i-1)
    # če vozlišče ni na levem robu, dodaj v sosednje elemente vozlišče levo od i

    if i < (constants.all_squares-constants.number_of_squares[0]): l.append(i+constants.number_of_squares[0])
    # če vozlišče ni v spodnji vrsti, dodaj v sosednjost tistega pod i

    if ((i+1) % constants.number_of_squares[0]) != 0: l.append(i+1)
    # če vozlišče ni na desnem robu, dodaj v sosednjost tistega desno od i

    seznam_sosednjosti.append(l)
    print(i, l)


graf = graph.GrafSS(constants.all_squares, seznam_sosednjosti)
in_progress = ""
graf.vozlica[0].oznaka = 3
graf.vozlica[-1].oznaka = 3


def narisi_kvadrate():
    for vx in range(constants.number_of_squares[0]):
        for vy in range(constants.number_of_squares[1]):
            if (graf.vozlica[ vy*constants.number_of_squares[1]+vx ].oznaka is None) or (graf.vozlica[ vy*constants.number_of_squares[1]+vx ].oznaka == 0):
                pygame.draw.rect(
                    window,
                    colors.kvadrat,
                    (
                        constants.border_width + (vx) * constants.square_width,  # x
                        constants.border_height + (vy) * constants.square_height,  # y
                        constants.square_width,  # sx
                        constants.square_height  # sy
                    )
                )
            elif graf.vozlica[ vy*constants.number_of_squares[1]+vx ].oznaka == 1:
                pygame.draw.rect(
                    window,
                    colors.pobarvan,
                    (
                        constants.border_width + (vx) * constants.square_width,  # x
                        constants.border_height + (vy) * constants.square_height,  # y
                        constants.square_width,  # sx
                        constants.square_height  # sy
                    )
                )
            elif graf.vozlica[ vy*constants.number_of_squares[1]+vx ].oznaka == 2:
                pygame.draw.rect(
                    window,
                    colors.obiskan,
                    (
                        constants.border_width + (vx) * constants.square_width,  # x
                        constants.border_height + (vy) * constants.square_height,  # y
                        constants.square_width,  # sx
                        constants.square_height  # sy
                    )
                )

            elif graf.vozlica[ vy*constants.number_of_squares[1]+vx ].oznaka == 3:
                pygame.draw.rect(
                    window,
                    colors.start_stop,
                    (
                        constants.border_width + (vx) * constants.square_width,  # x
                        constants.border_height + (vy) * constants.square_height,  # y
                        constants.square_width,  # sx
                        constants.square_height  # sy
                    )
                )


def clear_board():
    global in_progress
    for v in graf.vozlica:
        v.obiskano = False
        if v.oznaka == 2: v.oznaka = 0
        v.cas_vhoda = float('infinity')
        v.cas_izhoda = float('infinity')
    in_progress = ""



def kvadrat_na_xy(x, y):
    if x >= constants.border_width+constants.square_field_width: return None
    if y >= constants.border_height+constants.square_field_height: return None
    if x < constants.border_width: return None
    if y < constants.border_height: return None
    x -= constants.border_width
    y -= constants.border_height
    sqx = math.floor(x / constants.square_width)
    sqy = math.floor(y / constants.square_height)
    return sqx+sqy*constants.number_of_squares[0]


def dobi_sosede(k):
    # k: kvadrat

    l = []

    if k >= constants.number_of_squares[0]: l.append(k - constants.number_of_squares[0])
    # če vozlišče ni na zgornjem robu, dodaj v sosednje elemente vozlišče nad i

    if k % constants.number_of_squares[0] != 0: l.append(k - 1)
    # če vozlišče ni na levem robu, dodaj v sosednje elemente vozlišče levo od i

    if k < (constants.all_squares - constants.number_of_squares[0]): l.append(k + constants.number_of_squares[0])
    # če vozlišče ni v spodnji vrsti, dodaj v sosednjost tistega pod i

    if ((k + 1) % constants.number_of_squares[0]) != 0: l.append(k + 1)
    # če vozlišče ni na desnem robu, dodaj v sosednjost tistega desno od i

    return l



def main():

    global in_progress

    while True:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                quit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
                    if kvn is not None and kvn != constants.all_squares-1 and kvn != 0:
                        graf.vozlica[kvn].oznaci(1)
                        for sq in dobi_sosede(kvn):
                            try:
                                graf.sosednjost[sq].remove(kvn)
                            except ValueError:
                                pass

                if pygame.mouse.get_pressed()[2]:
                    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
                    if kvn is not None and kvn != constants.all_squares - 1 and kvn != 0:
                        graf.vozlica[kvn].oznaci(0)
                        for sq in dobi_sosede(kvn):
                            try:
                                graf.sosednjost[sq].append(kvn)
                            except ValueError:
                                pass

            if e.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
                    if kvn is not None and kvn != constants.all_squares - 1 and kvn != 0:
                        graf.vozlica[kvn].oznaci(1)
                        for sq in dobi_sosede(kvn):
                            try:
                                graf.sosednjost[sq].remove(kvn)
                            except ValueError:
                                pass

                if pygame.mouse.get_pressed()[2]:
                    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
                    if kvn is not None and kvn != constants.all_squares - 1 and kvn != 0:
                        graf.vozlica[kvn].oznaci(0)
                        for sq in dobi_sosede(kvn):
                            try:
                                graf.sosednjost[sq].append(kvn)
                            except ValueError:
                                pass

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    clear_board()
                    in_progress = ""

                if e.key == pygame.K_KP1:
                    if not bfs_done:
                        clear_board()
                        in_progress = "bfs"

        if in_progress == "bfs":
            if bfs_step(graf, 0, constants.all_squares-1) is True:
                in_progress = ""

        window.fill(colors.ozadje)
        narisi_kvadrate()

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
