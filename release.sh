#!/bin/bash
pip install pyinstaller
wget -nc https://raw.githubusercontent.com/amoffat/sh/master/sh.py
pyinstaller --clean --noconfirm --hidden-import sh --onefile --name setup-git main.py