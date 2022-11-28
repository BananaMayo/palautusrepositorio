from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for a in self.kori:
            maara += a.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for a in self.kori:
            hinta += a.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for a in self.kori:
            if a.tuotteen_nimi() == lisattava.nimi():
                a.muuta_lukumaaraa(1)
                return
        osto = Ostos(lisattava)
        self.kori.append(osto)

    def poista_tuote(self, poistettava: Tuote):
        for a in self.kori:
            if a.tuotteen_nimi() == poistettava.nimi():
                if a.lukumaara()>1:
                    a.muuta_lukumaaraa(-1)
                else:
                    self.kori.remove(a)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
