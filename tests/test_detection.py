import unittest
import pandas as pd
from src.detection import detect_anomalies

class TestDetection(unittest.TestCase):

    def test_detect_anomalies(self):
        # Testa a detecção de anomalias
        data = pd.DataFrame({
            'frequency': [1e14, 1e14],
            'temperature': [300, 300],
            'intensity': [50, 150]
        })
        threshold = 100
        result = detect_anomalies(data, threshold)
        self.assertEqual(len(result), 1)
        self.assertEqual(result['intensity'].iloc[0], 150)
        self.assertGreater(result['intensity'].iloc[0], threshold)

if __name__ == '__main__':
    unittest.main()
