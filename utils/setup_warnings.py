import warnings


def setup_warnings():
    warnings.filterwarnings("ignore", category=UserWarning)
