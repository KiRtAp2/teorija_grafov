import queue
import graph
import time

vrsta = queue.Queue()
bfs_done = False


def bfs(graf: graph.GrafSS, start: int, stop: int):
    out = False
    while out is not None:
        out = bfs_step(graf, start, stop)


def reset():
    global bfs_done, vrsta
    bfs_done = False
    vrsta = queue.Queue()


def bfs_step(graf: graph.GrafSS, start: int, stop: int):
    #time.sleep(0)  # za bojlši izgled
    global bfs_done, vrsta
    if not bfs_done:
        vrsta.put(graf.vozlica[start])
        bfs_done = True
        return False
    else:
        if not vrsta.qsize() == 0:
            vozl = vrsta.get()
            vozl.oznaci(2)
            if vozl.n == stop:
                vrsta = queue.Queue()
                return True
            for v in graf.sosednjost[vozl.n]:
                if not graf.vozlica[v].obiskano:
                    vrsta.put(graf.vozlica[v])
                    graf.vozlica[v].obiskano = True
            return False
        return None
