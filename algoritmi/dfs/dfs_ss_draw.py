import graph
import time
import constants


sklad = list()
dfs_zacet = False


def dfs(graf: graph.GrafSS, start: int, stop: int):
    """Na hitro opravi cel dfs po korakih, vendar se med izvajanjem graf ne nariše na zaslonu (ni asinhrono)"""
    out = False
    while out is not None:
        out = dfs_step(graf, start, stop)


def dfs_step(graf: graph.GrafSS, start: int, stop: int):
    """Opravi en korak DFS (obravna eno polje)"""
    time.sleep(constants.SLEEP_DELAY)
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
    """Resetira nastavitve, da se lahko naredi nov DFS"""
    global dfs_zacet, sklad
    sklad.clear()
    dfs_zacet = False
