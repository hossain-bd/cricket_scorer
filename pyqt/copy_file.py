# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:26:07 2019

@author: Hossain
"""

# copy_file.py

from shutil import copyfile
import os

def current_dir():
    #path = os.environ['PATH']
    directory = os.path.dirname(__file__) + '\\'
    print('DEBUG: Current directory {}'.format(directory))
    return directory

def copy_to_anaconda3(ui_file):
    cur_dir = current_dir()
    file = cur_dir + ui_file
    target_dir = 'C:\\Users\\Hossain\\AppData\\Local\\Continuum\\anaconda3\\' + ui_file
    print('DEBUG: Copying file: {} To: {}'.format(file, target_dir))
    copyfile(file, target_dir)
    
def copy_to_main(ui_file):
    cur_dir = current_dir()
    file = cur_dir + ui_file
    target_dir = cur_dir + 'dist\\main\\' + ui_file
    print('DEBUG: Copying file: {} To: {}'.format(file, target_dir))
    copyfile(file, target_dir)
