import unittest
import pandas as pd
from src.processing import planck_radiation, process_data

class TestProcessing(unittest.TestCase):

    def test_planck_radiation(self):
        # Teste básico da função planck_radiation
        frequency = 1e14  # Frequência de exemplo em Hz
        temperature = 300  # Temperatura de exemplo em K
        result = planck_radiation(frequency, temperature)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)  # A intensidade deve ser positiva

    def test_process_data(self):
        # Testa o processamento de dados
        data = pd.DataFrame({'frequency': [1e14], 'temperature': [300]})
        result = process_data(data)
        self.assertEqual(len(result), 1)
        self.assertIn('intensity', result.columns)
        self.assertGreater(result['intensity'].iloc[0], 0)

if __name__ == '__main__':
    unittest.main()
