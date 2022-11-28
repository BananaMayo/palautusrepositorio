import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)
    
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        pekoni = Tuote("Pekoni", 2)
        self.kori.lisaa_tuote(pekoni)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisäämisen_jälkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        pekoni = Tuote("Pekoni", 2)
        self.kori.lisaa_tuote(pekoni)
        self.assertEqual(self.kori.hinta(), 5)
    
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisäämisen_jälkeen_ostoskorissa_on_2_tuotteen_summa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.hinta(), 3)
        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
    
    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        pekoni = Tuote("Pekoni", 2)
        self.kori.lisaa_tuote(pekoni)   
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_ostoksen_jolla_sama_nimi_kuin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 2)