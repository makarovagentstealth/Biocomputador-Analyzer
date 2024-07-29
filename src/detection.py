def detect_anomalies(processed_data, threshold=100):
    """Detecta anomalias nos dados processados com base em um limiar de intensidade."""
    anomalies = processed_data[processed_data['intensity'] > threshold]
    return anomalies
