from pipenv_manager.check_and_install import check_and_install_pipenv
from pipenv_manager.run_commands import run_pipenv_commands


def setup():
    check_and_install_pipenv()
    run_pipenv_commands()


setup()
