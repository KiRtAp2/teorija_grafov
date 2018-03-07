import math
import pygame
import graph
from algoritmi.bfs.bfs_ss_draw import bfs_step
from algoritmi.dfs.dfs_ss_draw import dfs_step
from shortest_path_sim import constants, colors
from sys import exit as quit
import algoritmi.bfs.bfs_ss_draw as bfs_
import algoritmi.dfs.dfs_ss_draw as dfs_


def dobi_sosede(k: int):
    """Vrne vse celice, ki so zraven k. To niso celice, ki jih lahko obiščemo iz k!"""
    # k: kvadrat

    l = []

    if k >= constants.NUM_OF_SQUARES[0]: l.append(k - constants.NUM_OF_SQUARES[0])
    # če vozlišče ni na zgornjem robu, dodaj v sosednje elemente vozlišče nad i

    if k % constants.NUM_OF_SQUARES[0] != 0: l.append(k - 1)
    # če vozlišče ni na levem robu, dodaj v sosednje elemente vozlišče levo od i

    if k < (constants.ALL_SQUARES - constants.NUM_OF_SQUARES[0]): l.append(k + constants.NUM_OF_SQUARES[0])
    # če vozlišče ni v spodnji vrsti, dodaj v sosednjost tistega pod i

    if ((k + 1) % constants.NUM_OF_SQUARES[0]) != 0: l.append(k + 1)
    # če vozlišče ni na desnem robu, dodaj v sosednjost tistega desno od i

    return l


# ustvari seznam sosednjosti
seznam_sosednjosti = []
for i in range(constants.ALL_SQUARES):
    """ konstruira posamezne sosednje elemente """
    l = dobi_sosede(i)
    seznam_sosednjosti.append(l)


# ustvari graf, okno ipd.
window = pygame.display.set_mode((constants.WWIDTH, constants.WHEIGHT))
graf = graph.GrafSS(constants.ALL_SQUARES, seznam_sosednjosti)
in_progress = ""
graf.vozlica[0].oznaci(3)
graf.vozlica[-1].oznaci(3)


def narisi_kvadrate():
    """Funkcija pobarva del zaslona glede na oznako posameznega vozlišča"""
    for vx in range(constants.NUM_OF_SQUARES[0]):
        for vy in range(constants.NUM_OF_SQUARES[1]):
            barva = (0, 0, 0)
            oznaka = graf.vozlica[vy * constants.NUM_OF_SQUARES[1] + vx].oznaka
            if (oznaka is None) or (oznaka == 0):
                barva = colors.KVADRAT
            elif oznaka == 1:
                barva = colors.POBARVAN
            elif oznaka == 2:
                barva = colors.OBISKAN
            elif oznaka == 3:
                barva = colors.START_STOP
            pygame.draw.rect(
                window,
                barva,
                (
                    constants.BORDER_WIDTH + vx * constants.SQUARE_WIDTH,  # x
                    constants.BORDER_HEIGHT + vy * constants.SQUARE_HEIGHT,  # y
                    constants.SQUARE_WIDTH,  # sx
                    constants.SQUARE_HEIGHT  # sy
                )
            )


def clear_board():
    """Počisti polje"""
    global in_progress
    for v in graf.vozlica:
        v.obiskano = False
        if v.oznaka == 2: v.oznaka = 0
        v.cas_vhoda = float('infinity')
        v.cas_izhoda = float('infinity')
    in_progress = ""
    bfs_.reset()
    dfs_.reset()
    graf.vozlica[0].oznaci(3)
    graf.vozlica[-1].oznaci(3)


def kvadrat_na_xy(x, y):
    """Vrne n celice, ki je na pooziciji x, y"""
    if x >= constants.BORDER_WIDTH+constants.SQUARE_FIELD_WIDTH: return None
    if y >= constants.BORDER_HEIGHT+constants.SQUARE_FIELD_HEIGHT: return None
    if x < constants.BORDER_WIDTH: return None
    if y < constants.BORDER_HEIGHT: return None
    x -= constants.BORDER_WIDTH
    y -= constants.BORDER_HEIGHT
    sqx = math.floor(x / constants.SQUARE_WIDTH)
    sqy = math.floor(y / constants.SQUARE_HEIGHT)
    return int(sqx+sqy*constants.NUM_OF_SQUARES[0])


def leva_miska():
    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
    if kvn is not None and kvn != constants.ALL_SQUARES - 1 and kvn != 0:
        graf.vozlica[kvn].oznaci(1)
        for sq in dobi_sosede(kvn):
            try:
                graf.sosednjost[sq].remove(kvn)
            except ValueError:
                pass
                # ValueError se pojavi, ko poskusimo klikniti na celico, ki je že pravilno označena


def desna_miska():
    kvn = kvadrat_na_xy(*pygame.mouse.get_pos())
    if kvn is not None and kvn != constants.ALL_SQUARES - 1 and kvn != 0:
        graf.vozlica[kvn].oznaci(0)
        for sq in dobi_sosede(kvn):
            try:
                graf.sosednjost[sq].append(kvn)
            except ValueError:
                pass
                # ValueError se pojavi, ko poskusimo klikniti na celico, ki je že pravilno označena


def uporaba_miske():
    if pygame.mouse.get_pressed()[0]:  # Levi gumb miške
        leva_miska()

    if pygame.mouse.get_pressed()[2]:  # desni gumb miške
        desna_miska()


def main():

    global in_progress

    while True:

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                quit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                uporaba_miske()

            if e.type == pygame.MOUSEMOTION:
                uporaba_miske()

            if e.type == pygame.KEYDOWN:

                if e.key == pygame.K_r:
                    clear_board()
                    in_progress = ""

                if e.key == pygame.K_KP1:
                    clear_board()
                    in_progress = "bfs"

                if e.key == pygame.K_KP2:
                    clear_board()
                    in_progress = "dfs"

        if in_progress == "bfs":
            if bfs_step(graf, 0, constants.ALL_SQUARES-1) is True:
                in_progress = ""
        elif in_progress == "dfs":
            if dfs_step(graf, 0, constants.ALL_SQUARES-1) is True:
                in_progress = ""

        window.fill(colors.OZADJE)
        narisi_kvadrate()

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
