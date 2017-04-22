import unittest
from app.parimpar import verificarnumero

class Testpar(unittest.TestCase):
    def test_tipo_numero(self):
        self.assertEquals(verificarnumero(4),'par')
        self.assertEquals(verificarnumero(5),'impar')

if __name__ == '__main__':
    unittest.main()
