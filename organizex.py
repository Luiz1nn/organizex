from cli import create_parser
from file_processor import process_file
from utils.setup_warnings import setup_warnings

def main():
    setup_warnings()
    args = create_parser()
    process_file(args.input, args.output)

main()