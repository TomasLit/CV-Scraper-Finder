import os
import subprocess
import sys
import venv


venv_name = "my_virtual_environment"


def create_virtual_env():
    try:
        venv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), venv_name))
        venv.create(venv_dir, with_pip=True)
        print("VENV created")
        return venv_dir
    except Exception as e:
        print(f"Error creating virtual environment: {e}", file=sys.stderr)
        return None


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