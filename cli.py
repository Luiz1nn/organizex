import argparse
import os


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Organize financial data into an XLSX file.')
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Caminho do arquivo de entrada (XLSX)'
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='Caminho do arquivo de saída (XLS)'
    )

    args = parser.parse_args()

    input_ext = os.path.splitext(args.input)[1].lower()
    output_ext = os.path.splitext(args.output)[1].lower()

    if input_ext != '.xlsx':
        raise ValueError(
            f"O arquivo de entrada deve ser um arquivo .xlsx (recebido: {args.input})")

    if output_ext != '.xls':
        raise ValueError(
            f"O arquivo de saída deve ser um arquivo .xls (recebido: {args.output})")

    return args
