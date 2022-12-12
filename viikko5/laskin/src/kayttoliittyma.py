from enum import Enum
from tkinter import ttk, constants, StringVar
from sovelluslogiikka import Sovelluslogiikka

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka),
            Komento.KUMOA: Kumoa(sovelluslogiikka)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)
    
class Summa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self.viime_syote = 0
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.viime_syote = int(self.lue_syote())
        self.sovelluslogiikka.plus(self.viime_syote, self)
    
    def kumoa(self):
        self.sovelluslogiikka.miinus(self.viime_syote, 0)
        self.viime_syote = 0

class Erotus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka, lue_syote):
        self.viime_syote = 0
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.viime_syote = int(self.lue_syote())
        self.sovelluslogiikka.miinus(self.viime_syote, self)
    
    def kumoa(self):
        self.sovelluslogiikka.plus(self.viime_syote, 0)
        self.viime_syote = 0

class Nollaus:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        self.edellinen_arvo = 0

    def suorita(self):
        self.edellinen_arvo = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa(self)

class Kumoa:
    def __init__(self, sovelluslogiikka: Sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.kumoa()