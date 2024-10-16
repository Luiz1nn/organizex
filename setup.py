import subprocess
import sys

def install_requirements():
    try:
        with open('requirements.txt') as f:
            requirements = f.read().splitlines()
        
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', *requirements])
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"An error occurred during installation: {e}")

install_requirements()