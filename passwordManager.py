#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import modules
from cryptography import fernet
from cryptography.fernet import Fernet

def funcGetPassword(key, user_token, app_token):
    return (Fernet(key).decrypt(user_token).decode("ascii")), (Fernet(key).decrypt(app_token).decode("ascii"))

def funcSetPassword():
    user_token = input("Entrer le user token API : \n")
    app_token = input("Entrer le app token API : \n")
    newkey = Fernet.generate_key()
    newUserToken = Fernet(newkey).encrypt(user_token.encode())
    newAppToken = Fernet(newkey).encrypt(app_token.encode())
    return [newkey,newUserToken,newAppToken]

