from dotenv import load_dotenv
import os.path
import os
import sys
from config import DOWNLOAD_PATH, VERSION_FILE
from .list import list_local
import commands as _


def use(args):
    program = args.program
    version = args.version

    if not version:
        version_file_path = _.locate_file(VERSION_FILE)

        if version_file_path:
            load_dotenv(dotenv_path=version_file_path)
            version = (os.getenv(program.upper()))

    if not version:
        print(f"Please define version or add that to {VERSION_FILE} file.\
            \nYou don't need to mention version if you have {VERSION_FILE} file at current path. \n")
        sys.exit(1)

    available_versions = list_local(args)
    if version not in available_versions:
        print(program + " version '" + version + "' is not installed.\
            \nYou can check installed versions by running 'kubenvz kubectl/kustomize/helm list local'.\n")
        sys.exit(1)

    dest_path = DOWNLOAD_PATH + program + "_" + version
    
    install_path = _.get_install_path()
    
    try:
        os.remove(install_path + program)
    except FileNotFoundError:
        pass
    os.symlink(dest_path, install_path + program)
    print(program + " version is set to " + version)
