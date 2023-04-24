import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ['OS'], 'Includes': ['tkinter']}

base = None
if sys.plataform == 'Win32':
    base = 'Win32GUI'

setup(
    name = 'Primeiro executável',
    version = '0.001',
    description = 'Primeiro teste do programa',
    options = {'build.exe': build_exe_options},
    executables = [Executable('app.py', base=base)]
)
