#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:51:04 2021

@author: gravicapa
"""

import math as mth
import numpy as np
from utils import msgo

C = 299792458

#========= it contains parameters for radar_sig ======================================= 
class Paramss:
        
    def __init__(self):
        
        self.num_sig = 10       #maximum of probing signals number
        self.dt = 1.6*10**-6    #time of sampling
        self.df = 0.625*10**6  #signal bandwith
        self.a_noise = 7        #noise (of receiver) level
        self.param_s = []       #probing signals paramter list 
        self.lymbda = 0.20 #default wavelenght
        self.kd = mth.ceil((2*self.lymbda*10**6)/(C*self.dt))
        self.bin = 2**15
        
        #default signals parameter filling
        for i in range(self.num_sig):
            self.param_s.append({'T':320*10**-6, 'B':0, 'dtt':0,
                                   'Fd':0, 'Dist':0, 'Ampl':1, 'WC':0, 'W_coef':[0],'Fsh':0, 'On':0})
            self.param_s[i]['B'] = mth.floor(self.param_s[i]['T']/self.dt)           
            self.set_wps_ham(i)
        
    # setting base signals parameter
    def set_p(self, num_sig, dt,df, a_noise, lymbda):
        self.a_noise = a_noise
        self.dt = dt
        self.df = df
        self.num_sig = num_sig  
        self.lymbda = lymbda
        self.kd = mth.ceil((2*self.lymbda*10**6)/(C*self.dt))
        
    # setting dynamic radar signals parameter     
    def set_ps(self, nums, param):
        if(nums<self.num_sig):
            self.param_s[nums]['T'] = param['T']
            self.param_s[nums]['Fd'] = param['Fd']
            self.param_s[nums]['Dist'] = param['Dist']
            self.param_s[nums]['Ampl'] = param['Ampl']
            self.param_s[nums]['dtt'] = param['dtt']
            self.param_s[nums]['Fsh'] = param['Fsh']
            self.param_s[nums]['On'] = param['On']
            self.param_s[nums]['WC'] = param['WC']
            if(param['B']==0): self.param_s[nums]['B'] = mth.floor(self.param_s[nums]['T']/self.dt)
    
        else:            
            msgo.msg("out of range nums!", "set_ps")
            
    #setting weight coeff "wc"  for probing signals      
    def set_wps(self, nums,wc):
        if(nums<self.num_s):
            self.param_s[nums]['WC'] = 1
            self.param_s[nums]['W_coef'] = wc
        else:
            msgo.msg("out of range nums!", "set_wps")
            
     #setting weight coeff "wc"  for define probing signal         
    def set_wps_ham(self, nums):
        if(nums=="all"):
            for i in range(self.num_sig): 
                self.param_s[i]['WC'] = 1
                self.param_s[i]['Wcoef'] = np.hamming(self.param_s[i]['B'])
        else:
            if(nums<self.num_sig):
                self.param_s[nums]['WC'] = 1
                self.param_s[nums]['W_coef'] = np.hamming(self.param_s[nums]['B'])
            else:
                msgo.msg("out of range nums!", "et_wps_ham")
                

#========= it contains parameters for radar_wave =======================================        

class Paramsp:
    
    def __init__(self, tvob, dvob, ww, dfi):
        
        self.cnt_imp = 0    #current radar period
        self.t_sum = 0      #sum of radar time       
        self.len_p = 32     #length azimuth pack  
        self.vb = 5
        self.pdecim = 5
        self.cnt_decim = 0
        self.cnt_p_obr = 0
        self.t_sum_p = 0
        self.dfi = dfi      #array of complex faze shift for antenna array receiver element 
        self.AzBand = 2**13
        self.AzAngleStep = 360/self.AzBand
        self.AzCnt = 0
        self.AzT = 0
        self.SSTime = 10
        self.AzNiCnt = 0
        self.AzAngle = 0
        
        #init array of wobble period time
        if(tvob==0): self.tvob = [4*10**-3]
        else: self.tvob = tvob 
        #init array of wobble of number sample
        if(dvob==0): self.dvob = [1000]
        else: self.dvob = dvob 
        #init weight azimut window (amplitude modulation of directional diagram)
        if(ww==0): self.ww = np.array([1.0/mth.sqrt(self.len_p) for i in range(self.len_p)])
        else: self.ww = ww

    def rst_t(self):
        self.t_sum = 0
        self.num_imp = 0   


class Params_proc:
    
      def __init__(self, thrp):  
          self.thrp = thrp
          
      def setp(self, thrp):      
          self.thrp = thrp

    