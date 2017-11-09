import node


class GrafSS(object):
    """Implementacija grafa z uporabo seznama sosednjosti"""

    def __init__(self, stevilo_vozlisc: int, seznam_sosednjosti: list):
        # velikost grafa je dobro imeti shranjeno v spominu, da ni treba vsakič znova šteti vozlišč
        self.velikost = stevilo_vozlisc

        # ustvari seznam vozlišč
        self.vozlica = [node.Vozlisce(x) for x in range(stevilo_vozlisc)]

        # seznam sosednjosti je v naslednji obliki:
        # [
        #  [v, v, v, ...]  # vozlisca, sosednja vozliscu 0
        #  [v, v, v, ...]  # vozlisca, sosednja vozliscu 1
        #  [v, v, v, ...]  # vozlisca, sosednja vozliscu 2
        #  ...
        # ]
        # v: int
        self.sosednjost = seznam_sosednjosti

    def get_povezave_na(self, vozl):
        """Vrne tuple števil vseh vozlišč, ki so sosednja vozlišču s številom vozl"""
        return tuple(self.sosednjost[vozl])


class GrafMS(object):
    """Implementacija grafa z uporabo matrike sosednjosti"""

    def __init__(self, stevilo_vozlisc: int, matrika_sosodnjosti: list):
        self.velikost = stevilo_vozlisc
        self.vozlisca = [node.Vozlisce(x) for x in range(stevilo_vozlisc)]

        # matrika sosednjosti ima naslednji izgled:
        # [
        #   [1,0,0,0,1,0,1, ...]  # na mestih i, kjer je v matriki 1, je vozlisce 0 sosednjo vozliscu i
        #   [1,0,0,0,1,0,1, ...]  # na mestih i, kjer je v matriki 1, je vozlisce 1 sosednjo vozliscu i
        #   [1,0,0,0,1,0,1, ...]  # na mestih i, kjer je v matriki 1, je vozlisce 2 sosednjo vozliscu i
        #   ...
        # ]
        # len(sosednjost) = n
        # len(sosednjost[i]) = n
        self.sosednjost = matrika_sosodnjosti

    def get_povezave_na(self, vozl):
        """Vrne tuple števil vseh vozlišč, ki so sosednja vozlišču s številom vozl"""
        return (i for i, ps in self.sosednjost[vozl] if ps > 0)
