import os

VERSION = "0.4.0-12b5708"
DOWNLOAD_PATH = os.environ.get('TERRA_PATH', os.environ.get('HOME') + "/.kubenvz") + "/"
VERSION_FILE = ".kubenvz-version"
