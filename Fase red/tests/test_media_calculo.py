import unittest
from media_calculo import calcula_media

class TestMediaCalculo(unittest.TestCase):
    def test_calculo_media_basico(self):
        """Verifica se a média de 5, 7, e 9 é 7.0"""
        self.assertEqual(calcula_media(5, 7, 9), 7.0)

    def test_todas_notas_zero(self):
        """Verifica se a média de 0, 0, e 0 é 0"""
        self.assertEqual(calcula_media(0, 0, 0), 0)

    def test_notas_maximas(self):
        """Verifica se a média de 10, 10, e 10 é 10"""
        self.assertEqual(calcula_media(10, 10, 10), 10)

    def test_notas_decimais(self):
        """Verifica se a média de 5.5, 6.5, e 7.5 é aproximadamente 6.5"""
        self.assertAlmostEqual(calcula_media(5.5, 6.5, 7.5), 6.5)
