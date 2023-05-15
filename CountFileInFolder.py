#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 07:03:29 2023

@author: krishagni
"""

import sys, configparser, pandas as pd, os

#### Call config object #########
config_obj = configparser.ConfigParser()

#### Read Config file ###########
config_obj.read("configfile.ini")

#### Read path from input file from Config file ##############
path_of_input_folder = config_obj["input_folder_path"]["path_of_input_folder"]
path_of_output_folder = config_obj["output_folder_path"]["path_of_output_folder"]

#### Super Folders ###########
superFolderName =  os.listdir(path_of_input_folder)

superFolderPath = [os.path.join(path_of_input_folder, folder) for folder in superFolderName]

superFolder = dict(zip(superFolderName, superFolderPath))

#### Sub Folders ############

subFolderName = []

subFolderPath = []

for name,path in superFolder.items():
    subFolderName = subFolderName + [name+'/'+folder for folder in os.listdir(path)]
    subFolderPath = subFolderPath + [os.path.join(path, folder) for folder in os.listdir(path)]

#### Count Number of Files inside Sub Folder ######
subFolderFileCount = [len(os.listdir(path)) for path in subFolderPath]

subFolder =  {
                "Folder Name": subFolderName,
                'File Count': subFolderFileCount
             }

#### Writing Output ##########
df = pd.DataFrame.from_dict(subFolder)

df.to_excel(os.path.join(path_of_output_folder,'Output.xlsx'), index=False)
    