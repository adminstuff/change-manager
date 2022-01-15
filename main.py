#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import modules
import os
from readConfigFile import funcFileExiste, funcReadConfig

execPath = os.getcwd()
execFilePath = __file__
cfgFilePath = execPath+'\\config.ini'
keyFilePath = execPath+'\\.key'

if funcFileExiste(cfgFilePath) == True and funcFileExiste(keyFilePath) == True:
    print(funcReadConfig(keyFilePath,cfgFilePath))
    print("fin")