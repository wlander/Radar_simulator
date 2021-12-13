#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 13:12:41 2021

@author: gravicapa
"""

import numpy as np
#import matplotlib.pyplot as plt
import math as mth
import radar_wave as rw
import radar_proc as rproc
import radar_params as rparam
import bisect as bs
from utils import msgo
from pathlib import Path

#time vobulation set
vbb = [0.0035, 0.0045, 0.004, 0.0037, 0.0043] #Vobulation set
#distance vjbulation set
dvb = [1000, 1000, 1000, 1000, 1000]
#default parameters of probing signals list
sz = [{'T':320*10**-6, 'B':0, 'dtt':0,'Fd':30000, 'Dist':100, 'Ampl':1, 'WC':0, 'Fsh':1, 'On':0},
        {'T':320*10**-6, 'B':0, 'dtt':0,'Fd':300, 'Dist':300, 'Ampl':5, 'WC':0, 'Fsh':0, 'On':0},
        {'T':320*10**-6, 'B':0, 'dtt':0,'Fd':0, 'Dist':600, 'Ampl':10, 'WC':0, 'Fsh':0, 'On':0}]
path_w = Path(Path.cwd(),'az_w.dat')
#lenght of azimut packet
NP = 32


class Radar:
    
    def __init__(self):
        
        #parameters for threshold signals dedector
        self.thr_params = {'mx':3, 'win':15, 'stat':8, 'coef':1.65}
        
        #create instance of parameters of probing signals
        self.param_s = rparam.Paramss()
        #create instance of parameters of pack
        self.params_p = rparam.Paramsp(vbb,dvb,0,0)
        #parameters of processing
        self.params_proc = rparam.Params_proc(self.thr_params)
        #set parameters for probing signals
        for i in range(len(sz)): 
            self.param_s.set_ps(i,sz[i])            
            self.param_s.set_wps_ham(i)
        
        #create instance of simulator radar response signals for antenna array
        self.imit = rw.Radar_wave(self.param_s, self.params_p)
        #impulse response for fir
        self.ir = np.conj(self.imit.lfm_formula(self.param_s.df,self.param_s.dt,sz[0]['T'],0,0,mth.floor(sz[0]['T']/self.param_s.dt)))
        #create processing instance
        self.proc = rproc.Radar_proc(self.param_s, self.params_p, self.params_proc)
               
        f = open(path_w)
        l = [line.strip() for line in f]
        f.close()
        self.params_p.ww = [float(line.replace(",", "")) for line in l]
        
        #create and init azimut packet
        for i in range(NP):
            self.az_p = self.imit.p_win(0)
            
        #create buffer for fir result
        self.out_fir_p = [] 
        #create buffer for accum result
        self.out_acc = np.array([])
        #create buffer for result data list
        self.out_thr = []
        
        self.union_thr = set()
        self.UnionEnabled = False
        self.CntRev = 0
        self.dB = True
        
        self.time_imit = 4
        self.fl_start_stop = False
        
        self.accum_det = {'curr_az':0, 'cnt_i':0, 'accum_det':[0,0], 'cnt_det':[0,0], 'p_rev':[0,0], 'pr_det':[0,0]}
        
#-------- for hyper speed -------------------------
        self.LF = 3
        self.thr_hs = 1.37
#--------------------------------------------------        
         
        #self.test_data = self.imit.dist_gen(1000, 0)
        for i in range(self.params_p.pdecim): self.run()         
         
    def run(self):
        
        self.az_p = self.imit.p_win(0)
        self.out_fir_p.clear()
        for k in range(NP):
            self.out_fir_p.append(self.proc.fir_fft(self.az_p[k], self.ir))
        
        self.params_p.cnt_decim+=1

        if(self.params_p.cnt_decim==(self.params_p.pdecim-1)): 
        
            self.out_acc = self.proc.inco_accumi(self.out_fir_p, dvb[0]) 
            self.proc.Thr.p_coef = self.thr_params['coef']
            self.out_thr = self.proc.thr_det(self.out_acc)
            #self.out_acc = self.out_acc-self.out_thr[2]
            #mn = min(self.out_acc)+0.01
            #self.out_acc = self.out_acc-mn
            #self.out_thr = self.proc.thr_det(self.out_acc)         
            
            self.hspeed_acc = self.proc.Thr.sum_filter(self.out_acc, self.LF)
            self.proc.Thr.p_coef = self.thr_hs
            self.out_thr_hs = self.proc.thr_det(self.hspeed_acc)
            #self.hspeed_acc = self.hspeed_acc-self.out_thr_hs[2]
            #mn = min(self.hspeed_acc)+0.01
            #self.hspeed_acc = self.hspeed_acc-mn
            #self.out_thr_hs = self.proc.thr_det(self.hspeed_acc)
            
            if self.UnionEnabled:
                self.union_thr = set(self.out_thr[0]) | set(self.out_thr_hs[0])
                self.out_thr[0].clear()
                
                for s in self.union_thr:
                    self.out_thr[0].append(s)
                
            #self.union_thr.add(self.out_thr[0])
            #self.union_thr.add(self.out_thr_hs[0])
            
            if(self.params_p.AzCnt < self.accum_det['curr_az']): self.CntRev+=1  
            
            self.accum_det['cnt_i'] +=1  
            
            #accumulate detection of signals
            self.calc_middle_t(0)
            self.calc_middle_t(1)
            
            if(self.params_p.AzCnt < self.accum_det['curr_az']):  self.accum_det['cnt_i'] = 0 
             
            self.accum_det['curr_az'] = self.params_p.AzCnt
            
            self.params_p.cnt_decim = 0
            
            self.params_p.cnt_p_obr+=1

        
    def set_targets(self,num,t_type, val):
        if(num<self.param_s.num_sig): self.param_s.param_s[num][t_type] = val
        else: msgo.msg("out of range num!", "class Radar, def set_targets")
        
    def get_targets(self,num,t_type):
        if(num<self.param_s.num_sig): return self.param_s.param_s[num][t_type]
        else: msgo.msg("out of range num!", "class Radar, def set_targets")
        return 0
    
    def reset(self):
        self.params_p.t_sum = 0
        self.params_p.t_sum_p = 0
        self.params_p.cnt_imp = 0
        self.params_p.cnt_p_obr = 0
        #self.params_p.cnt_decim = 0
        self.CntRev = 0
        self.accum_det = {'curr_az':0, 'cnt_i':0, 'accum_det':[0,0], 'cnt_det':[0,0], 'p_rev':[0,0], 'pr_det':[0,0]}
    
        self.params_p.AzT = 0
        self.params_p.AzCnt = 0
        self.params_p.AzNiCnt = 0
        
    def calc_middle_t(self, n):
        
        if(n==0): 
            self.accum_det['cnt_det'][n] += len(self.out_thr[0])
            if(len(self.out_thr[0])>0): self.accum_det['pr_det'][n]+=1
        else: 
            self.accum_det['cnt_det'][n] += len(self.out_thr_hs[0])
            if(len(self.out_thr_hs[0])>0): self.accum_det['pr_det'][n]+=1

        if(self.params_p.AzCnt < self.accum_det['curr_az']):
            self.accum_det['accum_det'][n] += self.accum_det['cnt_det'][n]
            self.accum_det['p_rev'][n] = float('{:.2f}'.format((self.accum_det['pr_det'][n]/self.accum_det['cnt_i'])))
            self.accum_det['cnt_det'][n] = 0
            self.accum_det['pr_det'][n] = 0      
 
            
#=================== creating instance of Radar================================                     
my_radar = Radar()
#==============================================================================


