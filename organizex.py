from cli import create_parser
from file_processor import process_file
from utils import ensure_categories, ensure_normalizations, setup_warnings


__version__ = "1.7.0"


def main():
    print(f"Versão do projeto: {__version__}")
    setup_warnings()
    ensure_normalizations()
    ensure_categories()
    args = create_parser()
    process_file(args.input, args.output)


main()
