from setuptools import setup, find_packages

APP = ['main.py']
DATA_FILES = ['bot.png']
APP_NAME = 'Бот Alex'
OPTIONS = {
    'argv_emulation' : True,
    'packages' : ['certifi']
}

setup(
    name = APP_NAME,
    packages = find_packages(),
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app' : OPTIONS},
    setup_requires = ['py2app']
)