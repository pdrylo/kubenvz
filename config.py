import os

VERSION = "0.5.0"
DOWNLOAD_PATH = os.environ.get('TERRA_PATH', os.environ.get('HOME') + "/.kubenvz") + "/"
VERSION_FILE = ".kubenvz-version"
