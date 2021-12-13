#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:20:31 2021

@author: gravicapa
"""

import math as mth
import numpy as np
from numba import jit
import radar_params as rp
import bisect as bs
from utils import msgo

class Threshold:
    
    def __init__(self, params):
        self.mx = params['mx']
        self.win = params['win']
        self.stat = params['stat']
        self.p_coef = params['coef']

    #@jit
    def sum_filter(self, data, lf):
        if(len(data)>(lf*4)):
            out = np.zeros(len(data))
            for i in range(len(data)-lf):
                out[i+lf] = sum(data[i:i+lf])/mth.sqrt(lf)                
            return out
        else: msgo.msg("error elements number!", "from filter class HyperSpeedAccum")
        
        return 0
    
    #@jit    
    def maximator(self, data):
        if(len(data)>(self.mx*2) and self.mx>0 and self.mx<10):
            return np.array([max(data[i:i+self.mx]) for i in range(0,len(data),self.mx)])
        else:
            msgo.msg("contitions: data>0 0<mx<10", "class Threshold def maximator")
            print("mx:", self.mx, "win: ", self.win, "stat: ", self.stat, "coef: ", self.p_coef)
        
    #@jit
    def ord_stat(self, data):
        if(len(data)>(self.win*2) and self.win>0 and self.win<len(data)/2 and self.stat<self.win):
            
            offs_left = self.win-self.stat
            offs_right = self.win-offs_left        
            fifo = np.sort(data[0:self.win]).tolist()     
            out = np.zeros(len(data))

            for i in range(len(data)-self.win):
                out[offs_left+i] = fifo[self.stat]
                place = bs.bisect(fifo,data[i])
                del fifo[place-1]
                bs.insort(fifo, data[i+self.win])
           
            for i in range(offs_left): out[i] = out[offs_left]
            for i in range(offs_right): out[len(data)-offs_right+i] = out[len(data)-offs_right-1]
            
            return out
        else:
            msgo.msg("contitions: data>0 0<win<len(data)/2", "class Threshold def ord_stat") 
            print("mx:", self.mx, "win: ", self.win, "stat: ", self.stat, "coef: ", self.p_coef, "data: ", len(data))
        
        return 0
    
    #@jit
    def interp(self, data, n, nd):        
        out = np.repeat(data,n)
        if(len(out)>nd): return out[:nd] 
        else:  return out
    
    #@jit    
    def thr_mult(self, data):
        return np.multiply(data, self.p_coef)
        
    #@jit
    def comp_thresh(self, data, thr_data):
        out = []     
        for i in range(len(data)):
            if (data[i]>thr_data[i]): out.append(i)
        return out
      #return np.where(data>thr_data)
    
    
    def det_thr(self, data):
        
        data_proc = self.maximator(data)
        data_proc = self.ord_stat(data_proc)
        data_proc = self.interp(data_proc,self.mx, len(data))   
        thr_proc = self.thr_mult(data_proc)
        return [self.comp_thresh(data, thr_proc), thr_proc, data_proc]
    
    
class Radar_proc:
    
    def __init__(self, params_s, params_p, params_proc):
        
        if(isinstance(params_s, rp.Paramss) and isinstance(params_p, rp.Paramsp) and isinstance(params_proc, rp.Params_proc)):
            self.params_s = params_s
            self.paramsp = params_p
            self.params_proc = params_proc
            self.Thr = Threshold(self.params_proc.thrp)
        else:
            msgo.msg("Error type", "class Radar_proc def init")
    
    #@jit        
    def fir_fft(self, data, iresp):
        if(len(data)==0 or len(iresp)==0): 
            msgo.print("len=0", "fir_fft") 
            return -1
        else:   
            #here zeros added to data until nearest power of two and multyple frequency area of impulse response 
            nn = len(data)+len(iresp)
            n_2log = 2**(np.ceil(np.log2(nn)))
            ip = np.array(iresp)
            ip = np.append(np.zeros((n_2log-len(ip)).astype(int)),ip, axis=0)
            coeffs = np.fft.fft(ip)
            in_d = np.copy(data)
            in_d = np.append(in_d,np.zeros((n_2log-len(data)).astype(int)))                        
            df = np.fft.fft(in_d)
            df = np.fft.ifft(np.multiply(df,coeffs))
            df = df[0:len(data)]
            
            return df
        
    #@jit    
    def inco_accumi(self, data_p, step):
        
        out = np.zeros(step)
        for i in range(self.paramsp.len_p):
            out += np.multiply(abs(data_p[i]),self.paramsp.ww[i])
        
        return out
  
    def inco_knn(self, data_p, step, koef):
        out = np.zeros(step)
         
        mtr_list = []
        nn = self.paramsp.len_p/self.paramsp.vb
            
        for k in range(self.paramsp.vb): #ni vb 
            in_mtr = np.array([[], []])
            for i in range(step): #nkd
                for j in range(nn): #even vb in data
                    in_mtr[j][i] = data_p[j*self.paramsp.vb+k][i]
        
            mtr_list.append(in_mtr) 
        
        #HERE STOPED!!!
        #for in_mtr[i][j]
        return out
         
    
    def pulse_couple(self, data_p, step):

        out = []
        nn = self.paramsp.len_p/self.paramsp.vb
         
        for k in range(self.paramsp.vb): #ni vb 
            pc_out = np.array([0.0+0.0j for i in range(step)])
            for i in range(step): #nkd
                for j in range(nn): #even vb in data
                    pc_out[i] += np.conj(data_p[j*self.paramsp.vb+k][i])        
        
            out.append(pc_out)
  
        return out
    
    
    def thr_det(self, data):       
        return self.Thr.det_thr(data)   
        