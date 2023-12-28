from cx_Freeze import setup, Executable
from sys import platform

if platform == 'Win32':
    base = 'Win32Gui'
else:
    base = None

setup(
    name='calcuterm',
    version='1.0',
    description='Ricardo Gameiro - Final Project for CS50',
    options={'build_exe':{'includes': ['tkinter']}},
    executables=[Executable('home.py', base=base)
    ],
)