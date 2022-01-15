#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Gestion des variables par fichier de configuration

# import modules
from ast import Return
import os
from backports import configparser
import fnmatch
from passwordManager import funcGetPassword, funcSetPassword


def funcFileExiste(fileName):
    if not os.path.isfile(fileName):
        print ("Le fichier {} n'existe pas".format(fileName))
    else:
        return True

def funcReadConfig(keyFilePath,cfgFilePath):
    keyfile = configparser.ConfigParser()
    keyfile.read(keyFilePath)
    cfgfile = configparser.ConfigParser()
    cfgfile.read(cfgFilePath)
    url = cfgfile.get("api","url")
    user_token = cfgfile.get("api","user_token")
    app_token = cfgfile.get("api","app_token")
    smtpServer = cfgfile.get("mail","smtpServer")
    exp = cfgfile.get("mail","exp")
    dst = cfgfile.get("mail","dst")
    logo = cfgfile.get("gui","logo")
    info1 = cfgfile.get("messages","info1")
    info2 = cfgfile.get("messages","info2")

    if keyfile.has_option("security","key") and cfgfile.has_option("api","user_token") and cfgfile.has_option("api","app_token"):
        #print("If")
        key = bytes(keyfile.get("security","key"),'ascii')
        #print(key.decode("ascii"))
        user_token = bytes(cfgfile.get("api","user_token"),'ascii')
        app_token = bytes(cfgfile.get("api","app_token"),'ascii')
        #print(token.decode("ascii"))
        retourToken = funcGetPassword(key,user_token,app_token)
        #print(retourToken[0])
        #print(retourToken[1])
    else:
        #print("else")
        retour = funcSetPassword()
        updateKeyFile = configparser.ConfigParser()
        updateConfigFile = configparser.ConfigParser()
        updateKeyFile['security'] = {'key': retour[0].decode("ascii")}
        with open(keyFilePath, 'w') as configfile:
            updateKeyFile.write(configfile)
        updateConfigFile['api'] = {'url' : url, 'user_token' : retour[1].decode("ascii"), 'app_token' : retour[2].decode("ascii")}
        updateConfigFile['mail'] = {'smtpServer' : smtpServer, 'exp' : exp, 'dst' : dst}
        updateConfigFile['gui'] = {'logo' : logo}
        updateConfigFile['messages'] = {'info1' : info1, 'info2' : info2}
        with open(cfgFilePath,'w') as configFile2:
            updateConfigFile.write(configFile2)
    return "toto"