import argparse
from processing import read_payload, process_data
from detection import detect_anomalies

def main():
    parser = argparse.ArgumentParser(description='Ferramenta de Análise de Sinais Eletromagnéticos')
    parser.add_argument('payload', type=str, help='Caminho para o arquivo de dados (CSV)')
    args = parser.parse_args()
    
    # Ler dados do payload
    data = read_payload(args.payload)
    
    # Processar os dados
    processed_data = process_data(data)
    
    # Detectar anomalias
    anomalies = detect_anomalies(processed_data)
    
    # Mostrar resultados
    print("Dados Processados:")
    print(processed_data)
    print("Anomalias Detectadas:")
    print(anomalies)

if __name__ == "__main__":
    main()
