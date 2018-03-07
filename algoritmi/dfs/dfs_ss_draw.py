import graph
import time
from shortest_path_sim import constants


sklad = list()
dfs_zacet = False


def dfs(graf: graph.GrafSS, start: int, stop: int):
    out = False
    while out is not None:
        out = dfs_step(graf, start, stop)


def dfs_step(graf: graph.GrafSS, start: int, stop: int):
    time.sleep(constants.sleep_delay)
    global dfs_zacet, sklad
    if not dfs_zacet:
        sklad.append(graf.vozlica[start])
        dfs_zacet = True
        return False
    else:
        if sklad:
            vozl = sklad.pop()
            vozl.oznaci(2)
            if vozl.n == stop:
                sklad.clear()
                return True
            for v in graf.sosednjost[vozl.n]:
                if not graf.vozlica[v].obiskano:
                    sklad.append(graf.vozlica[v])
                    graf.vozlica[v].obiskano = True
            return False
        return None


def reset():
    global dfs_zacet, sklad
    sklad.clear()
    dfs_zacet = False



# def dfs(graf: graph.GrafMS, v: int):
#     global cas
#     cas += 1
#     graf.vozlisca[v].vhod(cas, True)
#     graf.vozlisca[v].obiskano = True
#     for i in range(graf.velikost):
#         if graf.sosednjost[v][i] and not graf.vozlisca[i].obiskano:
#             dfs(graf, i)
#     cas += 1
#     graf.vozlisca[v].izhod(cas, True)
