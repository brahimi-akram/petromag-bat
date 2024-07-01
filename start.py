import os
import subprocess
import sys

def activate_virtualenv():
    # Determine the path to the virtual environment activation script
    if sys.platform.startswith('win'):
        activate_script = os.path.join('venv', 'Scripts', 'activate.bat')
    else:
        activate_script = os.path.join('venv', 'bin', 'activate')

    return activate_script

def main():
    activate_script = activate_virtualenv()

    # Construct the command to activate the virtual environment and run the Django server
    if sys.platform.startswith('win'):
        command = command = f'cmd /k "{activate_script} && python manage.py runserver"'
    else:
        command = f'source {activate_script} && python manage.py runserver 0.0.0.0:8000'

    # Run the command
    subprocess.run(command, shell=True, check=True)

if __name__ == '__main__':
    main()