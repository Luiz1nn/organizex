from cli import create_parser
from file_processor import process_file
from utils import ensure_normalizations, setup_warnings


__version__ = "1.6.0"


def main():
    print(f"Versão do projeto: {__version__}")
    setup_warnings()
    ensure_normalizations()
    args = create_parser()
    process_file(args.input, args.output)


main()
