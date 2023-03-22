import os
import sys
import subprocess
import venv


venv_name = "my_virtual_environment"


def create_virtual_env():
    if not os.path.exists(venv_name):
        venv.create(venv_name, with_pip=True)
        print(f"Virtual environment '{venv_name}' created.")
    else:
        pass    


def activate_venv():
    if not os.environ.get("VIRTUAL_ENV"):
        activate_script = os.path.join(os.getcwd(), venv_name, "Scripts", "activate.bat")
        subprocess.call(f"call {activate_script}", shell=True)
        print(f"Virtual environment '{venv_name}' activated.")
    else:
        pass


def install_modules():
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()

    installed_packages = subprocess.check_output(
        [f"{venv_name}/Scripts/python", "-m", "pip", "freeze"]
        )

    packages_to_install = set(requirements) - set(installed_packages)

    if packages_to_install:
        subprocess.call([f"{venv_name}/Scripts/pip", "install", "-r", "requirements.txt"])
        print(f"Virtual environment '{venv_name}' created and activated.")
    else:
        pass


def main():
    if sys.version_info >= (3, 3):
        create_virtual_env()
        activate_venv()
        install_modules()
        print('It looks like everything is done, Sir!')
main()

