import graph

cas = 0


def dfs(graf: graph.GrafMS, v: int):
    global cas
    cas += 1
    graf.vozlisca[v].vhod(cas, True)
    graf.vozlisca[v].obiskano = True
    for i in range(graf.velikost):
        if graf.sosednjost[v][i] and not graf.vozlisca[i].obiskano:
            dfs(graf, i)
    cas += 1
    graf.vozlisca[v].izhod(cas, True)


def main():
    print("Napisi stevilo vozlisc in stevilo povezav med njimi, locano s presledkom: ")
    n, m = (int(x) for x in input().split())
    print("Napisi vse povezave v formatu 'vozlisce1 vozlisce2'")
    matrika = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a, b = (int(x) for x in input().split())
        matrika[a][b] = 1
        matrika[b][a] = 1
    graf = graph.GrafMS(n, matrika)
    print("DFS začenjam v vozlišču 0...")
    dfs(graf, 0)


if __name__ == '__main__':
    main()