import subprocess

def run_pipenv_commands():
    """Executa o comando pipenv shell e pipenv install."""

    try:
        subprocess.check_call(["pipenv", "shell"])
    except subprocess.CalledProcessError:
        print("Erro ao tentar executar pipenv shell.")

    try:
        subprocess.check_call(["pipenv", "install"])
    except subprocess.CalledProcessError:
        print("Erro ao tentar executar pipenv install.")

