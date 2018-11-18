#!/usr/bin/env python3

import os
from sh.contrib import git

print("== Git Setup for starters! ==")

user = input('Your Name: ')
mail = input('Your Email: ')

print("Configure git...")
git.config('--global', 'user.name', user)
git.config('--global', 'user.email', mail)
print("Generate SSH Key...")
os.system('ssh-keygen -t ed25519 -C "'+mail+'"')