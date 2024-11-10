import argparse

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Organize financial data into an XLSX file.')
    parser.add_argument('--input', type=str, required=True, help='Caminho do arquivo de entrada (XLSX)')
    parser.add_argument('--output', type=str, required=True, help='Caminho do arquivo de saída (XLS)')
    return parser