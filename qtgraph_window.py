#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 14:57:44 2021

@author: gravicapa
"""

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTimer
import pyqtgraph as pg
import numpy as np
from radar_frontend import my_radar  
 
class MyPlot(pg.PlotWidget):        
    def mousePressEvent(self, event):                    
        print("MyPlot widget clicked: x=", event.pos().x(), "; y=", event.pos().y())
 
 
class MyWindow(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
 
        self.setWindowTitle("pyqtgraph example 1: Simple usage")
        
        self.vbox = QtWidgets.QVBoxLayout()       
        self.plot = MyPlot(self)      
        self.plot.show()
        
        x = np.arange(len(my_radar.out_acc))  
        
        y = my_radar.out_acc
        self.plot.plot(x, y, pen = "g", clear = False)      
        y = my_radar.out_thr[1]
        self.plot.plot(x, y, pen = "b", clear = False)
       
        y = my_radar.hspeed_acc
        self.plot.plot(x, y, pen = "r", clear = False)
        y = my_radar.out_thr_hs[1]
        self.plot.plot(x, y, pen = "w", clear = False)
        
        #y = my_radar.az_p[0].real
        #self.plot.plot(x, y, pen = "g", clear = False)
        
        self.vbox.addWidget(self.plot)       
        self.setLayout(self.vbox)
        self.setMinimumHeight(300)
        self.setMinimumWidth(1030)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.Handler)
        self.timer.start(40)
        
        
    def Handler(self):

        my_radar.run()        
        x = np.arange(len(my_radar.out_acc))
        
        y = my_radar.out_acc
        self.plot.plot(x, y, pen = "g", clear = True)       
        y = my_radar.out_thr[1]
        self.plot.plot(x, y, pen = "b", clear = False)
        
        y = my_radar.hspeed_acc 
        self.plot.plot(x, y, pen = "r", clear = False)         
        y = my_radar.out_thr_hs[1]
        self.plot.plot(x, y, pen = "w", clear = False)
        
        #y = my_radar.az_p[0].real
        #self.plot.plot(x, y, pen = "g", clear = True)        
        
        #print("Handler")
        
    def mousePressEvent(self, event):   
        
        my_radar.run()        
        x = np.arange(len(my_radar.out_acc))
        
        y = my_radar.out_acc
        self.plot.plot(x, y, pen = "g", clear = True)
        y = my_radar.out_thr[1]
        self.plot.plot(x, y, pen = "r", clear = False)         
        
        print("MyWindow clicked")     
        event.accept()

 
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
 
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())


    
