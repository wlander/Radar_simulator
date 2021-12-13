import math as mth
import numpy as np
import random as rnd
from numba import jit
import radar_params as rp
from utils import msgo

C = 299792458

#========= make base signal (periodic, probing signals and etc) =======================================        

class Radar_sig:
    
    def __init__(self, params):
        self.psig = []                        #init 
        self.params = params                  #it creates class of parameters
        self.psig_formula = self.lfm_formula  #default formula for making probing signal sample 
       

    # func calculate lfm sample  
    #@jit
    def lfm_formula(self, df,dt,ts,fd,tsum,B):
        s = np.zeros(B)
        for k in range(B):
            s[k] = ((mth.pi*df*(k*dt-(ts-dt)/2)**2)/ts)+(mth.pi*fd*tsum) 
        return np.array([mth.cos(s[i])+mth.sin(s[i])*1j for i in range(B)])
    
    # func makes list probing signals according self.params.params_s  
    #@jit
    def psig_gen(self, t_sum):
        self.psig.clear()
        
        # making probing signals list
        for i in range(self.params.num_sig):
            
            self.psig.append(self.lfm_formula(self.params.df, self.params.dt, self.params.param_s[i]['T'], self.params.param_s[i]['Fd'], t_sum, self.params.param_s[i]['B']))
            
            #applying of weight window by fft 
            if(self.params.param_s[i]['WC']!=0):
                
                if(len(self.params.param_s[i]['W_coef'])==len(self.psig[i])):
                    self.psig[i] = self.psig[i]*self.params.param_s[i]['W_coef'] #np.fft.ifft((np.fft.fft(self.psig[i])*(self.params.param_s[i]['WC']+0j)))
                else:
                    msgo.msg("out of range nums!", "psig_gen") 
                    
            self.psig[i]*=self.params.param_s[i]['Ampl']  
        
                    
    # func makes periodic signal with freq vobulation from "vob" time list and weight window "w"                     
    #@njit
    def s_gen(self, f, n, dt, vob, wc):
        
        w = 2*mth.pi*f
        dw = 2*mth.pi*(1/dt)
        
        k = 0  
        tp = 0                                     
        s = np.array([0 for i in range(n)], 'float64')
        if(wc==0): ww = np.array([0 for i in range(n)], 'float64')
        else: ww = wc
        
        for i in range(n):                
            fs = i*w*tp+dw
            s[i] = (mth.cos(fs)+mth.sin(fs)*1j)*ww
            tp = tp+vob[k]
            if(k>=len(vob)): k = 0
       
        return s   
               
#========= it makes impulse wave and azimut packet =======================================        

class Radar_wave(Radar_sig):
         
    def __init__(self, params_s, params_p):
    
        if(isinstance(params_s, rp.Paramss) and isinstance(params_p, rp.Paramsp)):
            
            super().__init__(params_s)
        
            self.paramsp = params_p 
        else:
            msgo.msg("Error type", "class Radar_wave def init")
            
        self.p = []     
        self.pw = []
        self.pww = []            
        for i in range(self.paramsp.len_p):
            self.pw.append(0)
            
    #making one radar period for one reciever channel 
    #@jit
    def dist_gen(self, dist, ch):

        T = self.paramsp.tvob[mth.floor(self.paramsp.cnt_imp%len(self.paramsp.tvob))]     
        s = np.array([((rnd.random()-0.5)+(rnd.random()-0.5)*1j)*self.params.a_noise for i in range(dist)])
     
        self.psig_gen(self.paramsp.t_sum)
        for i in range(self.params.num_sig):
            
            if(self.params.param_s[i]['On']):
                
                d = self.params.param_s[i]['Dist']
                st = self.params.param_s[i]['B']
                
                if (self.params.param_s[i]['Fsh']==0 and (self.paramsp.cnt_imp%self.paramsp.len_p)==0): #self.paramsp.cnt_decim==0): 
                    self.paramsp.t_sum_p = 0
                    
                #print("kd: ", self.params.kd)             
                d_sh = self.paramsp.t_sum_p*self.params.param_s[i]['Fd'] #accum signal shift                 
                #print("d_sh: ", d_sh)              
                kd_sh = mth.floor(d_sh/self.params.kd) #
                #print("kd_sh: ", kd_sh)  
                #Shifting of distance by Fd
                d = d+kd_sh
                #leaking to the next sample
                csh = (d_sh-(kd_sh*self.params.kd))/self.params.kd #leaking coeff          
                #print("csh: ", csh)
                    
                if(csh>0.01):
                    sig = np.array([0.0+0.0j for i in range(st+1)])
                    for k in range(st): sig[k+1] = self.psig[i][k]*complex(csh)
                    for k in range(st): sig[k] += self.psig[i][k]
                    st+=1

                else:
                    sig = self.psig[i]  
                          
                for k in range(st):
                    if((d+k)<dist): s[d+k] += sig[k]
                    else: break
                
                
                
        if(self.paramsp.dfi!=0): #if there is directional diagramm for antenna aray
            s = s*self.paramsp.dfi[ch]            
        
        self.paramsp.t_sum+=T 
        self.paramsp.t_sum_p+=T
        self.paramsp.cnt_imp += 1
        
        self.paramsp.AzT += T
        self.paramsp.AzCnt = mth.floor(self.paramsp.AzT/(self.paramsp.SSTime/self.paramsp.AzBand))
        self.paramsp.AzNiCnt +=1
        self.paramsp.AzAngle = self.paramsp.AzCnt*self.paramsp.AzAngleStep
        
        if(self.paramsp.AzCnt>self.paramsp.AzBand): 
            self.paramsp.AzCnt = 0
            self.paramsp.AzT = 0
            self.paramsp.AzNiCnt = 0
            self.paramsp.AzAngle = 0
            
        #print("dist_gen imp: ", self.paramsp.cnt_imp)

        return s    
    
    #making set radar period (azimuth pack) for one reciever channel     
    #@jit
    def p_gen(self, num_imp, ch):
        
        self.p = []
        k = 0
        
        for i in range(num_imp):
            self.p.append(self.dist_gen(self.paramsp.dvob[k],ch)*self.paramsp.ww[i])
            k = k+1
            if(k>=len(self.paramsp.dvob)): k = 0
            
        return self.p
    
    #making set radar period (azimuth pack) for one reciever channel  
    #with rotation of "fifo" 
    #@jit
    def p_win(self, ch):

        for i in range(self.paramsp.len_p-1): self.pw[(self.paramsp.len_p-1)-i] = self.pw[(self.paramsp.len_p-1)-i-1]
        
        imp_vob = mth.floor(self.paramsp.cnt_imp%len(self.paramsp.dvob))
        self.pw[0] = self.dist_gen(self.paramsp.dvob[imp_vob], ch)
        
        for i in range(self.paramsp.len_p):
            self.pw[i] = np.multiply(self.pw[i],self.paramsp.ww[i])
        
        return self.pw
    
        
        