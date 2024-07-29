import pandas as pd
import numpy as np

# Constantes
h = 6.626e-34  # Constante de Planck (J·s)
c = 3.0e8      # Velocidade da luz (m/s)
k_B = 1.381e-23  # Constante de Boltzmann (J/K)

def planck_radiation(frequency, temperature):
    """Calcula a radiação de corpo negro usando a fórmula de Planck."""
    return (8 * np.pi * h * frequency**3) / (c**3 * (np.exp(h * frequency / (k_B * temperature)) - 1))

def read_payload(file_path):
    """Lê o payload a partir de um arquivo CSV."""
    return pd.read_csv(file_path)

def process_data(data):
    """Processa os dados do payload e calcula a intensidade da radiação."""
    results = []
    for index, row in data.iterrows():
        frequency = row['frequency']
        temperature = row['temperature']
        intensity = planck_radiation(frequency, temperature)
        results.append({'frequency': frequency, 'temperature': temperature, 'intensity': intensity})
    return pd.DataFrame(results)
