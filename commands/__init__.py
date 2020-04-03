import os

from typing import Union

from .list import list_local, list_remote
from .install import install
from .uninstall import uninstall
from .use import use


def locate_file(file: str) -> Union[str, bool]:
    dir: str = os.path.realpath('.')

    while dir:
        if os.path.exists(f"{dir}/{file}"):
            return f"{dir}/{file}"

        if dir != '/':
            dir = os.path.dirname(dir)
        else:
            return False


def get_install_path() -> str:
    install_path = ""

    for dir in ['bin', '.bin', '.local/bin']:
        if os.path.exists(f"{os.getenv('HOME')}/{dir}"):
            print(f"Trying to install in the following path: {os.getenv('HOME')}/{dir}/")

            if not os.access(f"{os.getenv('HOME')}/{dir}", os.W_OK):
                print(f"Warning: Path {os.getenv('HOME')}/{dir}/ is not writeable. Trying other possible paths.")
            else:
                install_path = f"{os.getenv('HOME')}/{dir}/"
                break
            
    if install_path == "":
        install_path = "/usr/local/bin"

        print(f"Trying default path: {install_path}")

        if not os.access(install_path, os.W_OK):
            print(f"Error: User doesn't have write permission of {install_path} directory.\
                \n\nRun below command to grant permission and rerun 'kubenvz install' command.\
                \nsudo chown -R $(whoami) {install_path}\n")
            exit(1)

    return install_path
