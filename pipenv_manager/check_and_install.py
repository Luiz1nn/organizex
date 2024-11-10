import subprocess
import sys


def check_and_install_pipenv():
    """Verifica se o pipenv está instalado, e caso não, instala-o."""

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", "pipenv"])
    except subprocess.CalledProcessError:
        print("pipenv não está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pipenv"])

