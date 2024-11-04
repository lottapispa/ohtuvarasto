import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus_ja_saldo(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_liian_pieni_tilavuus(self):
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_uudella_varastolla_vaara_saldo(self):
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisaa_alle_0(self):
        self.varasto.lisaa_varastoon(-1)
        # ei tapahdu mitään
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        # varastossa pitäisi olla 10
        self.assertEqual(self.varasto.saldo, 10)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_ota_mitaan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 5)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 5)

    def test_ottaa_liikaa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(7)
        # varastossa pitäisi olla 0, sieltä voidaan ottaa vain 5
        self.assertEqual(self.varasto.saldo, 0)
        self.assertEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_str(self):
        self.varasto.lisaa_varastoon(6)
        self.assertEqual(self.varasto.__str__(), "saldo = 6, vielä tilaa 4")


