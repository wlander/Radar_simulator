#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:56:45 2021

@author: gravicapa
"""

#============ it's for out messange  ========================================  
class Msg_out:
    def __init__(self, out_type):  
        self.out_type = out_type
        self.file_log = "log.out"
        
    def msg(self, msg, src):
        if self.out_type=="console":
            print(msg, src)
        elif self.out_type=="log":
            try:
                #try open file for log
                print("Log to file will be here soon!")
            except: FileNotFoundError


    def set_file_log(self, fl):
        self.file_log  = fl
        
msgo = Msg_out("console") 