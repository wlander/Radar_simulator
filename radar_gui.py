# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radar_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtChart import QPolarChart, QChartView, QValueAxis, QScatterSeries
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QPainter, QPen, QFont, QColor
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import Qt
import pyqtgraph as pg
#import matplotlib.pyplot as plt
import numpy as np
import math as mth
from radar_form import*
from radar_frontend import my_radar 

#=================================================================================

class Radar_GUI(QtWidgets.QMainWindow, Ui_form_RadarView):
    
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        
        self.setupUi(self)
        
        # init plots
        self.plot1 = pg.PlotWidget(self.frame_Oscill)
        self.plot1.setGeometry(QtCore.QRect(2, 2, 1024, 318))
        self.plot2 = pg.PlotWidget(self.frame_Oscill_2)
        self.plot2.setGeometry(QtCore.QRect(2, 2, 1024, 318))
        
        x = np.arange(len(my_radar.out_acc))           
        self.plot1.plot(x, my_radar.out_acc, pen = "g", clear = False)      
        self.plot1.plot(x, my_radar.out_thr[1], pen = "b", clear = False)       
        self.plot2.plot(x, my_radar.hspeed_acc, pen = "g", clear = False)      
        self.plot2.plot(x, my_radar.out_thr_hs[1], pen = "b", clear = False)      
        self.plot1.setYRange(-20,20)
        self.plot2.setYRange(-20,20)        
        self.plot1.show()                
        self.plot2.show()
        
        self.polar = QPolarChart()
        self.polar.setBackgroundBrush(QColor(255, 255, 255, 0))
        
        chartView = QChartView(self.polar)
        chartView.setStyleSheet('background-color: black')
        
        layout = QVBoxLayout()
        layout.addWidget(chartView)
        self.frame_Indicator.setLayout(layout)
        
        axisy = QValueAxis()
        #axisy.setStyleSheet('color: red')
        axisy.setRange(0,450)
        axisy.setTickCount(4)
        #axisy.setMinorTickCount(2)
        self.polar.setAxisY(axisy)
                      
        axisx = QValueAxis()
        axisx.setRange(0,360)
        axisx.setTickCount(5)
        #axisx.setMinorTickCount(8)
        self.polar.setAxisX(axisx)

        self.polar_series = QScatterSeries()
        self.polar_series.setMarkerSize(3.0)
        self.polar_series0 = QScatterSeries()
        self.polar_series0.setMarkerSize(5.0)        
        
        self.polar_series.append(0, 0)
        self.polar_series.append(360, 450)    
        
        for i in range(0,360,10):
            self.polar_series.append(i, i)
        
        self.polar.addSeries(self.polar_series)                      
        self.polar_series0.append(0, 0);
        self.polar_series0.append(360, 450)      
        self.polar.addSeries(self.polar_series0)  
            
        # init imitator
        self.imit_timer = QtCore.QTimer()
        self.dspinbox_ImitSpeed.setValue(my_radar.time_imit)
        
        #self.table_Channel.setItem(1,1, QTableWidgetItem('33'))
                                   
        for i in range(5):
            for j in range(11): self.table_Channel.setItem(i,j, QTableWidgetItem(str((i*11)+j+1)))
        
        #----- init params from GUI -----------------------------------------
        a = float(self.ledit_Ampl.text())
        if(my_radar.dB): a = 20*mth.log10(my_radar.param_s.bin/my_radar.get_targets(0,'Ampl'))
        self.ledit_Ampl.setText(str(mth.floor(a)))
        self.ledit_Dist.setText(str(my_radar.get_targets(0,'Dist')))
        self.ledit_Fd.setText(str(my_radar.get_targets(0,'Fd')))
        self.chbox_TargetOn.setCheckState(my_radar.get_targets(0,'On'))
        self.chbox_FdShift.setCheckState(my_radar.get_targets(0,'Fsh'))
        self.ledit_Thr.setText(str(my_radar.thr_params['coef']))
        self.ledit_ThrHS.setText(str(my_radar.thr_hs))
        #--------------------------------------------------------------------         
        self.callback_init()
        
        
    def callback_init(self):
        
        self.imit_timer.timeout.connect(self. handler_imit_timer)
        self.bttn_StartStop.clicked.connect(self.callb_bttn_start_stop)
        self.dspinbox_ImitSpeed.valueChanged.connect(self.callb_imit_speed_changed)
        self.ledit_FiltrLen.editingFinished.connect(self.callb_filtr_hs_changed)
        self.ledit_Thr.editingFinished.connect(self.callb_Thr_changed)
        self.ledit_ThrHS.editingFinished.connect(self.callb_ThrHS_changed)
        
        self.ledit_Range1.editingFinished.connect(self.callb_Range1_changed)
        self.ledit_Range2.editingFinished.connect(self.callb_Range1_changed)
        self.ledit_Range1_2.editingFinished.connect(self.callb_Range2_changed)
        self.ledit_Range2_2.editingFinished.connect(self.callb_Range2_changed)
        self.chbox_FdShift.stateChanged.connect(self.callb_FdShift_changed)
        self.chbox_SumHS.stateChanged.connect(self.callb_SumHS_changed)
        
        #---------- targetts settings ------------------------------------
        self.ledit_Ampl.editingFinished.connect(self.callb_Ampl_changed)
        self.ledit_Dist.editingFinished.connect(self.callb_Dist_changed)
        self.ledit_Fd.editingFinished.connect(self.callb_Fd_changed)
        self.spinbox_Target.valueChanged.connect(self.callb_Target_changed)
        self.chbox_TargetOn.stateChanged.connect(self.callb_TargetOn_changed)
        #-----------------------------------------------------------------
    
        self.bttn_Reset.clicked.connect(self.callb_bttn_reset)      
    
    
    def callb_SumHS_changed(self):
        my_radar.UnionEnabled = int(self.chbox_SumHS.isChecked())
        
    def callb_FdShift_changed(self):
        my_radar.set_targets(self.spinbox_Target.value()-1,'Fsh', int(self.chbox_FdShift.isChecked()))

    #------- callback GUI functions -----------------------------------------
    def callb_Range1_changed(self):
        self.plot1.setYRange(int(self.ledit_Range1.text()),int(self.ledit_Range2.text()))
    
    def callb_Range2_changed(self):
        self.plot2.setYRange(int(self.ledit_Range1_2.text()),int(self.ledit_Range2_2.text()))
        
    def callb_bttn_start_stop(self):
        
        if(my_radar.fl_start_stop == False):
            self.bttn_StartStop.setText('Stop')
            my_radar.fl_start_stop = True
            self.imit_timer.start(my_radar.time_imit)
        else:
            self.bttn_StartStop.setText('Start')
            my_radar.fl_start_stop = False           
            self.imit_timer.stop()

    def callb_imit_speed_changed(self):
        self.imit_timer.stop()
        my_radar.time_imit = self.dspinbox_ImitSpeed.value()
        self.imit_timer.start(mth.floor(my_radar.time_imit))
            
    def callb_Thr_changed(self):
        my_radar.thr_params['coef'] = float(self.ledit_Thr.text())


    def callb_Ampl_changed(self):
        a = float(self.ledit_Ampl.text())
        if(my_radar.dB): a = (my_radar.param_s.bin/(10**(a/20)))
        my_radar.set_targets(self.spinbox_Target.value()-1,'Ampl', a)
    def callb_Dist_changed(self):
        my_radar.set_targets(self.spinbox_Target.value()-1,'Dist', int(self.ledit_Dist.text()))
    def callb_Fd_changed(self):
        my_radar.set_targets(self.spinbox_Target.value()-1,'Fd', int(self.ledit_Fd.text()))
     
    def callb_Target_changed(self):
        self.ledit_Ampl.setText(str(my_radar.get_targets(self.spinbox_Target.value()-1,'Ampl')))
        self.ledit_Dist.setText(str(my_radar.get_targets(self.spinbox_Target.value()-1,'Dist')))
        self.ledit_Fd.setText(str(my_radar.get_targets(self.spinbox_Target.value()-1,'Fd'))) 
        self.chbox_TargetOn.setCheckState(my_radar.get_targets(self.spinbox_Target.value()-1,'On'))
        self.chbox_FdShift.setCheckState(my_radar.get_targets(self.spinbox_Target.value()-1,'Fsh'))
        
    def callb_TargetOn_changed(self): 
        my_radar.set_targets(self.spinbox_Target.value()-1,'On', self.chbox_TargetOn.checkState())              

    def callb_bttn_reset(self):
        my_radar.reset()
        self.polar_series.clear()
        
#------------ for HS ---------------------------------------------------------
    def callb_ThrHS_changed(self):
        my_radar.thr_hs = float(self.ledit_ThrHS.text())  
    
    def callb_filtr_hs_changed(self):    
        my_radar.LF = int(self.ledit_FiltrLen.text())
#-----------------------------------------------------------------------------
    
#------------- imitator timer callback ---------------------------------------
    def handler_imit_timer(self):
        
        #az_last = my_radar.params_p.AzAngle
        
        my_radar.run()  
        
        if(my_radar.params_p.cnt_decim==0):
            
            if(self.tab_View.currentIndex()==0):
                x = np.arange(len(my_radar.out_acc)) 
                if(self.rbttn_Acc.isChecked()):    
                    self.plot1.plot(x, my_radar.out_acc, pen = "g", clear = True)      
                    self.plot1.plot(x, my_radar.out_thr[1], pen = "b", clear = False)
                
                    self.plot2.plot(x, my_radar.hspeed_acc, pen = "g", clear = True)      
                    self.plot2.plot(x, my_radar.out_thr_hs[1], pen = "b", clear = False)
                elif(self.rbttn_Fir.isChecked()):
                   #self.plot2.plot(x, 0, pen = "b", clear = True)
                   self.plot1.plot(x, my_radar.out_fir_p[0].real, pen = "g", clear = True) 
                   
                elif(self.rbttn_Input.isChecked()):
                   self.plot1.plot(x, my_radar.az_p[0].real, pen = "g", clear = True)
                   
                self.accum_det = {'curr_az':0, 'cnt_i':0, 'accum_det':[0,0], 'cnt_det':[0,0]}
               
                str_out = "Proc: Azimut: " + str(my_radar.params_p.AzCnt) + " Rev: " + str(my_radar.CntRev)
                self.lbl_Stat1.setText(str_out) 
                
                str_out = "Log:  Det: " + str(my_radar.accum_det['cnt_det'][0])
                str_out = str_out  + " SumDet: "+str(my_radar.accum_det['accum_det'][0])   
                str_out = str_out  + " p/r: "+str(my_radar.accum_det['p_rev'][0])   
                self.lbl_OscLog.setText(str_out)
        
                str_out = "Log:  Det: " + str(my_radar.accum_det['cnt_det'][1])
                str_out = str_out  + " SumDet: "+str(my_radar.accum_det['accum_det'][1])
                str_out = str_out  + " p/r: "+str(my_radar.accum_det['p_rev'][1]) 
                self.lbl_OscLog_2.setText(str_out)
            
            az_cur = my_radar.params_p.AzAngle
            
            az_clear = az_cur+4.0
            #else: az_clear = az_cur+(360-az_last)+az_cur           
            if(az_clear>360): az_clear = 360  
            
            for j in range(self.polar_series.count()):
                if(self.polar_series.at(j).x()>=(az_cur) and self.polar_series.at(j).x()<(az_clear)): self.polar_series.remove(j)
             
            if(az_clear>360): 
                az_clear = az_clear - 360            
                for j in range(self.polar_series.count()):
                    if(self.polar_series.at(j).x()>=(0) and self.polar_series.at(j).x()<=(az_clear)): self.polar_series.remove(j)
                
            
            #clear last azimut position
            for i in range(len(my_radar.out_thr[0])):
                self.polar_series.append(my_radar.params_p.AzAngle, my_radar.out_thr[0][i]*0.48);
        
            self.polar_series0.clear()
            self.polar_series0.append(0, 0);
            self.polar_series0.append(360, 450);
    
            for i in range(7):
                self.polar_series0.append(my_radar.params_p.AzAngle+i-3,450)  
                      
#====================================================================================== 
        
if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Radar_GUI()
    w.show()
    app.exec()

#=======================================================================================    
