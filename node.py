class Vozlisce(object):
    """Eno vozlišče grafa."""

    def __init__(self, zaporedno_stevilo: int):
        """Inicializacijska metoda. zaporedno_stevilo naj bi bil indeks tega vozlisca v seznamu vozlisc v grafu"""
        self.n = zaporedno_stevilo
        self.obiskano = False
        self.oznaka = None
        self.cas_vhoda = -1
        self.cas_izhoda = -1

    def vhod(self, cas, print_=False):
        self.cas_vhoda = cas
        if print_: print("Vozlisce", self.n, "obiskano ob", cas)

    def izhod(self, cas, print_=False):
        self.cas_izhoda = cas
        if print_: print("Izhod iz vozlisca", self.n, "ob", cas)

    def oznaci(self, stevilo: int):
        """Uporabljeno v nekaterih programih"""
        self.oznaka = stevilo
