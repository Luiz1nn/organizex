from pipenv_manager import check_and_install_pipenv, run_pipenv_commands


def setup():
    check_and_install_pipenv()
    run_pipenv_commands()


setup()
