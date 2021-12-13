# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radar_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_RadarView(object):
    def setupUi(self, form_RadarView):
        form_RadarView.setObjectName("form_RadarView")
        form_RadarView.resize(1203, 857)
        form_RadarView.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tab_View = QtWidgets.QTabWidget(form_RadarView)
        self.tab_View.setGeometry(QtCore.QRect(2, 0, 1038, 840))
        self.tab_View.setObjectName("tab_View")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gbox_Settings = QtWidgets.QGroupBox(self.tab)
        self.gbox_Settings.setGeometry(QtCore.QRect(0, 645, 276, 168))
        self.gbox_Settings.setObjectName("gbox_Settings")
        self.gbox_HS = QtWidgets.QGroupBox(self.gbox_Settings)
        self.gbox_HS.setGeometry(QtCore.QRect(210, 20, 61, 141))
        self.gbox_HS.setObjectName("gbox_HS")
        self.ledit_ThrHS = QtWidgets.QLineEdit(self.gbox_HS)
        self.ledit_ThrHS.setGeometry(QtCore.QRect(10, 36, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ledit_ThrHS.setFont(font)
        self.ledit_ThrHS.setObjectName("ledit_ThrHS")
        self.lbl_ThrHS = QtWidgets.QLabel(self.gbox_HS)
        self.lbl_ThrHS.setGeometry(QtCore.QRect(10, 20, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_ThrHS.setFont(font)
        self.lbl_ThrHS.setObjectName("lbl_ThrHS")
        self.lbl_FiltrLen = QtWidgets.QLabel(self.gbox_HS)
        self.lbl_FiltrLen.setGeometry(QtCore.QRect(10, 56, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.lbl_FiltrLen.setFont(font)
        self.lbl_FiltrLen.setObjectName("lbl_FiltrLen")
        self.ledit_FiltrLen = QtWidgets.QLineEdit(self.gbox_HS)
        self.ledit_FiltrLen.setGeometry(QtCore.QRect(10, 70, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ledit_FiltrLen.setFont(font)
        self.ledit_FiltrLen.setFrame(True)
        self.ledit_FiltrLen.setClearButtonEnabled(False)
        self.ledit_FiltrLen.setObjectName("ledit_FiltrLen")
        self.chbox_SumHS = QtWidgets.QCheckBox(self.gbox_HS)
        self.chbox_SumHS.setGeometry(QtCore.QRect(10, 90, 41, 17))
        self.chbox_SumHS.setObjectName("chbox_SumHS")
        self.groupBox_9 = QtWidgets.QGroupBox(self.gbox_Settings)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 20, 191, 141))
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.ledit_Thr = QtWidgets.QLineEdit(self.groupBox_9)
        self.ledit_Thr.setGeometry(QtCore.QRect(60, 10, 61, 20))
        self.ledit_Thr.setObjectName("ledit_Thr")
        self.lbl_Thr = QtWidgets.QLabel(self.groupBox_9)
        self.lbl_Thr.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.lbl_Thr.setObjectName("lbl_Thr")
        self.gbox_Control = QtWidgets.QGroupBox(self.tab)
        self.gbox_Control.setGeometry(QtCore.QRect(281, 645, 409, 168))
        self.gbox_Control.setObjectName("gbox_Control")
        self.gbox_SetOut = QtWidgets.QGroupBox(self.gbox_Control)
        self.gbox_SetOut.setGeometry(QtCore.QRect(9, 20, 71, 141))
        self.gbox_SetOut.setTitle("")
        self.gbox_SetOut.setObjectName("gbox_SetOut")
        self.rbttn_Input = QtWidgets.QRadioButton(self.gbox_SetOut)
        self.rbttn_Input.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.rbttn_Input.setObjectName("rbttn_Input")
        self.rbttn_SF = QtWidgets.QRadioButton(self.gbox_SetOut)
        self.rbttn_SF.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.rbttn_SF.setObjectName("rbttn_SF")
        self.rbttn_ACP = QtWidgets.QRadioButton(self.gbox_SetOut)
        self.rbttn_ACP.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbttn_ACP.setObjectName("rbttn_ACP")
        self.rbttn_Fir = QtWidgets.QRadioButton(self.gbox_SetOut)
        self.rbttn_Fir.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.rbttn_Fir.setObjectName("rbttn_Fir")
        self.rbttn_Acc = QtWidgets.QRadioButton(self.gbox_SetOut)
        self.rbttn_Acc.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.rbttn_Acc.setChecked(True)
        self.rbttn_Acc.setObjectName("rbttn_Acc")
        self.chbox_Thr = QtWidgets.QCheckBox(self.gbox_SetOut)
        self.chbox_Thr.setGeometry(QtCore.QRect(10, 110, 70, 17))
        self.chbox_Thr.setChecked(True)
        self.chbox_Thr.setObjectName("chbox_Thr")
        self.bttn_StartStop = QtWidgets.QPushButton(self.gbox_Control)
        self.bttn_StartStop.setGeometry(QtCore.QRect(268, 10, 70, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bttn_StartStop.setFont(font)
        self.bttn_StartStop.setObjectName("bttn_StartStop")
        self.bttn_Reset = QtWidgets.QPushButton(self.gbox_Control)
        self.bttn_Reset.setGeometry(QtCore.QRect(375, 10, 32, 28))
        self.bttn_Reset.setObjectName("bttn_Reset")
        self.gbox_Channel = QtWidgets.QGroupBox(self.gbox_Control)
        self.gbox_Channel.setGeometry(QtCore.QRect(164, 52, 238, 110))
        self.gbox_Channel.setObjectName("gbox_Channel")
        self.table_Channel = QtWidgets.QTableWidget(self.gbox_Channel)
        self.table_Channel.setGeometry(QtCore.QRect(6, 14, 225, 88))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_Channel.setFont(font)
        self.table_Channel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_Channel.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.table_Channel.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_Channel.setGridStyle(QtCore.Qt.SolidLine)
        self.table_Channel.setWordWrap(True)
        self.table_Channel.setRowCount(5)
        self.table_Channel.setColumnCount(11)
        self.table_Channel.setObjectName("table_Channel")
        self.table_Channel.horizontalHeader().setVisible(False)
        self.table_Channel.horizontalHeader().setDefaultSectionSize(20)
        self.table_Channel.horizontalHeader().setMinimumSectionSize(14)
        self.table_Channel.verticalHeader().setVisible(False)
        self.table_Channel.verticalHeader().setDefaultSectionSize(17)
        self.table_Channel.verticalHeader().setMinimumSectionSize(14)
        self.gbox_Log = QtWidgets.QGroupBox(self.tab)
        self.gbox_Log.setGeometry(QtCore.QRect(697, 645, 332, 168))
        self.gbox_Log.setObjectName("gbox_Log")
        self.listWidget = QtWidgets.QListWidget(self.gbox_Log)
        self.listWidget.setGeometry(QtCore.QRect(6, 16, 321, 125))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setModelColumn(0)
        self.listWidget.setObjectName("listWidget")
        self.lbl_Stat1 = QtWidgets.QLabel(self.gbox_Log)
        self.lbl_Stat1.setGeometry(QtCore.QRect(7, 140, 292, 21))
        self.lbl_Stat1.setObjectName("lbl_Stat1")
        self.bttn_ClearLog = QtWidgets.QPushButton(self.gbox_Log)
        self.bttn_ClearLog.setGeometry(QtCore.QRect(297, 142, 31, 21))
        self.bttn_ClearLog.setObjectName("bttn_ClearLog")
        self.frame_Oscill = QtWidgets.QFrame(self.tab)
        self.frame_Oscill.setGeometry(QtCore.QRect(4, 2, 1026, 320))
        self.frame_Oscill.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_Oscill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Oscill.setObjectName("frame_Oscill")
        self.frame_Oscill_2 = QtWidgets.QFrame(self.tab)
        self.frame_Oscill_2.setGeometry(QtCore.QRect(4, 323, 1026, 320))
        self.frame_Oscill_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_Oscill_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Oscill_2.setObjectName("frame_Oscill_2")
        self.ledit_Range1 = QtWidgets.QLineEdit(self.tab)
        self.ledit_Range1.setGeometry(QtCore.QRect(972, 6, 55, 18))
        self.ledit_Range1.setAutoFillBackground(False)
        self.ledit_Range1.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_Range1.setFrame(True)
        self.ledit_Range1.setClearButtonEnabled(False)
        self.ledit_Range1.setObjectName("ledit_Range1")
        self.ledit_Range2 = QtWidgets.QLineEdit(self.tab)
        self.ledit_Range2.setGeometry(QtCore.QRect(972, 299, 55, 18))
        self.ledit_Range2.setAutoFillBackground(False)
        self.ledit_Range2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_Range2.setFrame(True)
        self.ledit_Range2.setClearButtonEnabled(False)
        self.ledit_Range2.setObjectName("ledit_Range2")
        self.ledit_Range2_2 = QtWidgets.QLineEdit(self.tab)
        self.ledit_Range2_2.setGeometry(QtCore.QRect(972, 622, 55, 18))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.ledit_Range2_2.setFont(font)
        self.ledit_Range2_2.setAutoFillBackground(False)
        self.ledit_Range2_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_Range2_2.setFrame(True)
        self.ledit_Range2_2.setClearButtonEnabled(False)
        self.ledit_Range2_2.setObjectName("ledit_Range2_2")
        self.ledit_Range1_2 = QtWidgets.QLineEdit(self.tab)
        self.ledit_Range1_2.setGeometry(QtCore.QRect(972, 327, 55, 18))
        self.ledit_Range1_2.setAutoFillBackground(False)
        self.ledit_Range1_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ledit_Range1_2.setFrame(True)
        self.ledit_Range1_2.setClearButtonEnabled(False)
        self.ledit_Range1_2.setObjectName("ledit_Range1_2")
        self.lbl_OscLog = QtWidgets.QLabel(self.tab)
        self.lbl_OscLog.setGeometry(QtCore.QRect(744, 6, 221, 16))
        self.lbl_OscLog.setObjectName("lbl_OscLog")
        self.lbl_OscLog.setStyleSheet("QLabel { color : white; }")
        self.lbl_OscLog_2 = QtWidgets.QLabel(self.tab)
        self.lbl_OscLog_2.setGeometry(QtCore.QRect(744, 326, 221, 16))
        self.lbl_OscLog_2.setObjectName("lbl_OscLog_2")
        self.lbl_OscLog_2.setStyleSheet("QLabel { color : white; }")
        self.tab_View.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_Indicator = QtWidgets.QFrame(self.tab_2)
        self.frame_Indicator.setGeometry(QtCore.QRect(10, 28, 750, 750))
        self.frame_Indicator.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_Indicator.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Indicator.setMidLineWidth(1)
        self.frame_Indicator.setObjectName("frame_Indicator")
        self.frame_Data = QtWidgets.QFrame(self.tab_2)
        self.frame_Data.setGeometry(QtCore.QRect(762, 28, 266, 749))
        self.frame_Data.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_Data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Data.setObjectName("frame_Data")
        self.frame_State = QtWidgets.QFrame(self.tab_2)
        self.frame_State.setGeometry(QtCore.QRect(10, 0, 1018, 28))
        self.frame_State.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_State.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_State.setObjectName("frame_State")
        self.frame_State_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_State_2.setGeometry(QtCore.QRect(10, 777, 1018, 28))
        self.frame_State_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_State_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_State_2.setObjectName("frame_State_2")
        self.tab_View.addTab(self.tab_2, "")
        self.gbox_Simulator = QtWidgets.QGroupBox(form_RadarView)
        self.gbox_Simulator.setGeometry(QtCore.QRect(1040, 14, 160, 826))
        self.gbox_Simulator.setObjectName("gbox_Simulator")
        self.gbox_Targets = QtWidgets.QGroupBox(self.gbox_Simulator)
        self.gbox_Targets.setGeometry(QtCore.QRect(4, 20, 150, 229))
        self.gbox_Targets.setObjectName("gbox_Targets")
        self.ledit_Ampl = QtWidgets.QLineEdit(self.gbox_Targets)
        self.ledit_Ampl.setGeometry(QtCore.QRect(70, 50, 51, 20))
        self.ledit_Ampl.setObjectName("ledit_Ampl")
        self.lbl_Ampl = QtWidgets.QLabel(self.gbox_Targets)
        self.lbl_Ampl.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.lbl_Ampl.setObjectName("lbl_Ampl")
        self.ledit_Dist = QtWidgets.QLineEdit(self.gbox_Targets)
        self.ledit_Dist.setGeometry(QtCore.QRect(70, 77, 51, 20))
        self.ledit_Dist.setObjectName("ledit_Dist")
        self.ledit_Fd = QtWidgets.QLineEdit(self.gbox_Targets)
        self.ledit_Fd.setGeometry(QtCore.QRect(70, 106, 51, 20))
        self.ledit_Fd.setObjectName("ledit_Fd")
        self.ledit_Azimut = QtWidgets.QLineEdit(self.gbox_Targets)
        self.ledit_Azimut.setGeometry(QtCore.QRect(70, 135, 51, 20))
        self.ledit_Azimut.setObjectName("ledit_Azimut")
        self.ledit_AE = QtWidgets.QLineEdit(self.gbox_Targets)
        self.ledit_AE.setGeometry(QtCore.QRect(70, 164, 51, 20))
        self.ledit_AE.setObjectName("ledit_AE")
        self.lbl_Dist = QtWidgets.QLabel(self.gbox_Targets)
        self.lbl_Dist.setGeometry(QtCore.QRect(10, 80, 47, 13))
        self.lbl_Dist.setObjectName("lbl_Dist")
        self.lbl_Fd = QtWidgets.QLabel(self.gbox_Targets)
        self.lbl_Fd.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.lbl_Fd.setObjectName("lbl_Fd")
        self.lbl_Azimut = QtWidgets.QLabel(self.gbox_Targets)
        self.lbl_Azimut.setGeometry(QtCore.QRect(10, 140, 47, 13))
        self.lbl_Azimut.setObjectName("lbl_Azimut")
        self.lbl_AE = QtWidgets.QLabel(self.gbox_Targets)
        self.lbl_AE.setGeometry(QtCore.QRect(10, 170, 47, 13))
        self.lbl_AE.setObjectName("lbl_AE")
        self.rbttn_FixMode = QtWidgets.QRadioButton(self.gbox_Targets)
        self.rbttn_FixMode.setGeometry(QtCore.QRect(5, 200, 38, 17))
        self.rbttn_FixMode.setChecked(True)
        self.rbttn_FixMode.setObjectName("rbttn_FixMode")
        self.rbttn_CircleMode = QtWidgets.QRadioButton(self.gbox_Targets)
        self.rbttn_CircleMode.setGeometry(QtCore.QRect(45, 200, 41, 17))
        self.rbttn_CircleMode.setObjectName("rbttn_CircleMode")
        self.rbttn_CircleMode2 = QtWidgets.QRadioButton(self.gbox_Targets)
        self.rbttn_CircleMode2.setGeometry(QtCore.QRect(85, 200, 41, 17))
        self.rbttn_CircleMode2.setObjectName("rbttn_CircleMode2")
        self.groupBox = QtWidgets.QGroupBox(self.gbox_Targets)
        self.groupBox.setGeometry(QtCore.QRect(5, 14, 120, 31))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.chbox_TargetOn = QtWidgets.QCheckBox(self.groupBox)
        self.chbox_TargetOn.setGeometry(QtCore.QRect(10, 8, 41, 17))
        self.chbox_TargetOn.setChecked(True)
        self.chbox_TargetOn.setObjectName("chbox_TargetOn")
        self.spinbox_Target = QtWidgets.QSpinBox(self.groupBox)
        self.spinbox_Target.setGeometry(QtCore.QRect(70, 4, 42, 22))
        self.spinbox_Target.setMinimum(1)
        self.spinbox_Target.setMaximum(10)
        self.spinbox_Target.setObjectName("spinbox_Target")
        self.gbox_Noise = QtWidgets.QGroupBox(self.gbox_Simulator)
        self.gbox_Noise.setGeometry(QtCore.QRect(4, 297, 150, 48))
        self.gbox_Noise.setObjectName("gbox_Noise")
        self.lbl_AmplNoise = QtWidgets.QLabel(self.gbox_Noise)
        self.lbl_AmplNoise.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.lbl_AmplNoise.setObjectName("lbl_AmplNoise")
        self.ledit_AmplNoise = QtWidgets.QLineEdit(self.gbox_Noise)
        self.ledit_AmplNoise.setGeometry(QtCore.QRect(70, 18, 51, 20))
        self.ledit_AmplNoise.setObjectName("ledit_AmplNoise")
        self.gbox_AddParams = QtWidgets.QGroupBox(self.gbox_Simulator)
        self.gbox_AddParams.setGeometry(QtCore.QRect(4, 691, 150, 131))
        self.gbox_AddParams.setObjectName("gbox_AddParams")
        self.chbox_FdShift = QtWidgets.QCheckBox(self.gbox_AddParams)
        self.chbox_FdShift.setGeometry(QtCore.QRect(10, 20, 70, 17))
        self.chbox_FdShift.setChecked(True)
        self.chbox_FdShift.setTristate(False)
        self.chbox_FdShift.setObjectName("chbox_FdShift")
        self.dspinbox_ImitSpeed = QtWidgets.QDoubleSpinBox(self.gbox_AddParams)
        self.dspinbox_ImitSpeed.setGeometry(QtCore.QRect(60, 50, 60, 20))
        self.dspinbox_ImitSpeed.setDecimals(1)
        self.dspinbox_ImitSpeed.setMinimum(1.0)
        self.dspinbox_ImitSpeed.setMaximum(1000.0)
        self.dspinbox_ImitSpeed.setSingleStep(0.5)
        self.dspinbox_ImitSpeed.setObjectName("dspinbox_ImitSpeed")
        self.lbl_ImitSpeed = QtWidgets.QLabel(self.gbox_AddParams)
        self.lbl_ImitSpeed.setGeometry(QtCore.QRect(5, 50, 61, 20))
        self.lbl_ImitSpeed.setObjectName("lbl_ImitSpeed")
        self.spinbox_Bits = QtWidgets.QSpinBox(self.gbox_AddParams)
        self.spinbox_Bits.setGeometry(QtCore.QRect(60, 80, 42, 20))
        self.spinbox_Bits.setMinimum(8)
        self.spinbox_Bits.setMaximum(32)
        self.spinbox_Bits.setProperty("value", 16)
        self.spinbox_Bits.setObjectName("spinbox_Bits")
        self.lbl_Bits = QtWidgets.QLabel(self.gbox_AddParams)
        self.lbl_Bits.setGeometry(QtCore.QRect(10, 80, 31, 20))
        self.lbl_Bits.setObjectName("lbl_Bits")
        self.gbox_ExtraSignals = QtWidgets.QGroupBox(self.gbox_Simulator)
        self.gbox_ExtraSignals.setGeometry(QtCore.QRect(4, 351, 150, 335))
        self.gbox_ExtraSignals.setObjectName("gbox_ExtraSignals")
        self.lbl_Stat2 = QtWidgets.QLabel(form_RadarView)
        self.lbl_Stat2.setGeometry(QtCore.QRect(700, 836, 501, 18))
        self.lbl_Stat2.setObjectName("lbl_Stat2")

        self.retranslateUi(form_RadarView)
        self.tab_View.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_RadarView)

    def retranslateUi(self, form_RadarView):
        _translate = QtCore.QCoreApplication.translate
        form_RadarView.setWindowTitle(_translate("form_RadarView", "RadarView"))
        self.gbox_Settings.setTitle(_translate("form_RadarView", "Proc_Settinngs"))
        self.gbox_HS.setTitle(_translate("form_RadarView", "HS_sett"))
        self.ledit_ThrHS.setText(_translate("form_RadarView", "1.5"))
        self.lbl_ThrHS.setText(_translate("form_RadarView", "Coef_Thr"))
        self.lbl_FiltrLen.setText(_translate("form_RadarView", "Filtr len"))
        self.ledit_FiltrLen.setText(_translate("form_RadarView", "3"))
        self.chbox_SumHS.setText(_translate("form_RadarView", "sum"))
        self.ledit_Thr.setText(_translate("form_RadarView", "1.5"))
        self.lbl_Thr.setText(_translate("form_RadarView", "Coef Thr"))
        self.gbox_Control.setTitle(_translate("form_RadarView", "Control"))
        self.rbttn_Input.setText(_translate("form_RadarView", "Input"))
        self.rbttn_SF.setText(_translate("form_RadarView", "SF"))
        self.rbttn_ACP.setText(_translate("form_RadarView", "ACP"))
        self.rbttn_Fir.setText(_translate("form_RadarView", "FIR"))
        self.rbttn_Acc.setText(_translate("form_RadarView", "ACC"))
        self.chbox_Thr.setText(_translate("form_RadarView", "THR"))
        self.bttn_StartStop.setText(_translate("form_RadarView", "Start"))
        self.bttn_Reset.setText(_translate("form_RadarView", "Rst"))
        self.gbox_Channel.setTitle(_translate("form_RadarView", "Channel"))
        self.gbox_Log.setTitle(_translate("form_RadarView", "Log"))
        self.lbl_Stat1.setText(_translate("form_RadarView", "Proc: Stoped"))
        self.bttn_ClearLog.setText(_translate("form_RadarView", "Cl"))
        self.ledit_Range1.setText(_translate("form_RadarView", "20"))
        self.ledit_Range2.setText(_translate("form_RadarView", "-10"))
        self.ledit_Range2_2.setText(_translate("form_RadarView", "-10"))
        self.ledit_Range1_2.setText(_translate("form_RadarView", "20"))
        self.lbl_OscLog.setText(_translate("form_RadarView", "Log:"))
        self.lbl_OscLog_2.setText(_translate("form_RadarView", "Log:"))
        self.tab_View.setTabText(self.tab_View.indexOf(self.tab), _translate("form_RadarView", "Oscillator"))
        self.tab_View.setTabText(self.tab_View.indexOf(self.tab_2), _translate("form_RadarView", "Radar Indicator"))
        self.gbox_Simulator.setTitle(_translate("form_RadarView", "Simulator"))
        self.gbox_Targets.setTitle(_translate("form_RadarView", "Targets"))
        self.ledit_Ampl.setText(_translate("form_RadarView", "10"))
        self.lbl_Ampl.setText(_translate("form_RadarView", "Ampl"))
        self.ledit_Dist.setText(_translate("form_RadarView", "100"))
        self.ledit_Fd.setText(_translate("form_RadarView", "0"))
        self.ledit_Azimut.setText(_translate("form_RadarView", "0"))
        self.ledit_AE.setText(_translate("form_RadarView", "10"))
        self.lbl_Dist.setText(_translate("form_RadarView", "Dist"))
        self.lbl_Fd.setText(_translate("form_RadarView", "Fd"))
        self.lbl_Azimut.setText(_translate("form_RadarView", "Azimut"))
        self.lbl_AE.setText(_translate("form_RadarView", "AE"))
        self.rbttn_FixMode.setText(_translate("form_RadarView", "FM"))
        self.rbttn_CircleMode.setText(_translate("form_RadarView", "CM"))
        self.rbttn_CircleMode2.setText(_translate("form_RadarView", "CM2"))
        self.chbox_TargetOn.setText(_translate("form_RadarView", "On"))
        self.gbox_Noise.setTitle(_translate("form_RadarView", "Noise"))
        self.lbl_AmplNoise.setText(_translate("form_RadarView", "Ampl"))
        self.ledit_AmplNoise.setText(_translate("form_RadarView", "70"))
        self.gbox_AddParams.setTitle(_translate("form_RadarView", "Add_Params"))
        self.chbox_FdShift.setText(_translate("form_RadarView", "Fd_Shift"))
        self.lbl_ImitSpeed.setText(_translate("form_RadarView", "Im_speed"))
        self.lbl_Bits.setText(_translate("form_RadarView", "Bits"))
        self.gbox_ExtraSignals.setTitle(_translate("form_RadarView", "Extra_Signals"))
        self.lbl_Stat2.setText(_translate("form_RadarView", "Stat:"))

