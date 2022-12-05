class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = None

    def miinus(self, arvo, viime_komento):
        self.tulos = self.tulos - arvo
        self.edellinen = viime_komento

    def plus(self, arvo, viime_komento):
        self.tulos = self.tulos + arvo
        self.edellinen = viime_komento

    def nollaa(self, viime_komento):
        self.tulos = 0
        self.edellinen = viime_komento

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        if self.edellinen != None:
            self.edellinen.kumoa()
        self.edellinen = None
