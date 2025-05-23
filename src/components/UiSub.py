# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/sub_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        # 设置可扩展的大小策略
        MainWindow.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) 
        self.Sub_window = QtWidgets.QWidget(MainWindow)
        self.Sub_window.setObjectName("Sub_window")
        self.Sub_window.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout = QtWidgets.QGridLayout(self.Sub_window)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.main_body = QtWidgets.QVBoxLayout()
        self.main_body.setObjectName("main_body")
        self.main_body.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint) 


        # 第一行 
        self.hl_top = QtWidgets.QHBoxLayout()
        self.hl_top.setObjectName("hl_top")
        self.hl_top.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint) 

        self.label_0 = QtWidgets.QLabel(self.Sub_window)
        self.label_0.setObjectName("label_0")
        self.label_0.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # 设置为可扩展
        self.label_0.setMinimumWidth(10)  # 设置最小宽度为10像素
        self.hl_top.addWidget(self.label_0)
        
        self.line = QtWidgets.QFrame(self.Sub_window)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.hl_top.addWidget(self.line)

        self.comboBox_1 = QtWidgets.QComboBox(self.Sub_window)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.comboBox_1.setMinimumWidth(50)  # 设置最小宽度为50像素
        self.hl_top.addWidget(self.comboBox_1)

        self.comboBox_2 = QtWidgets.QComboBox(self.Sub_window)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.comboBox_2.setMinimumWidth(50)  # 设置最小宽度为50像素
        self.hl_top.addWidget(self.comboBox_2)

        self.line_2 = QtWidgets.QFrame(self.Sub_window)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hl_top.addWidget(self.line_2)

        self.checkBox_1 = QtWidgets.QCheckBox(self.Sub_window)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.hl_top.addWidget(self.checkBox_1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.Sub_window)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.hl_top.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.Sub_window)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.hl_top.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.Sub_window)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_4.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.hl_top.addWidget(self.checkBox_4)

        self.hl_top.setStretch(0, 10)
        self.hl_top.setStretch(2, 3)
        self.hl_top.setStretch(3, 3)
        self.hl_top.setStretch(5, 1)
        self.hl_top.setStretch(6, 1)
        self.hl_top.setStretch(7, 1)
        self.hl_top.setStretch(8, 1)
        self.hl_top.setStretch(9, 1)
        self.main_body.addLayout(self.hl_top)

        # 表格项
        self.tableWidget_medium = QtWidgets.QTableWidget(self.Sub_window)
        self.tableWidget_medium.setObjectName("tableWidget_medium")
        self.tableWidget_medium.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # 设置为可扩展
        
        self.main_body.addWidget(self.tableWidget_medium)
        

        """添加底部状态栏""" 
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setStyleSheet("QStatusBar::item { border: none; }")
        self.statusbar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        # 创建按钮
        self.statusbar_left_button = QtWidgets.QPushButton("🔆")
        self.statusbar_button1 = QtWidgets.QPushButton("◀️ (prev)")
        self.statusbar_button2 = QtWidgets.QPushButton("▶️ (next)")

        # 创建标签
        self.label_bottom = QtWidgets.QLabel()
        self.label_bottom.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  # 设置为可扩展
        self.label_bottom.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)  # 设置右居中对齐
        self.label_bottom.setMinimumWidth(1)

        # 正确添加组件的方式：注意，addWidget & addPermanentWidget 的区别
        self.statusbar.addWidget(self.statusbar_left_button)       # 普通部件（左对齐）addWidget
        self.statusbar.addWidget(self.label_bottom)                # 普通部件（左对齐）addWidget
        self.statusbar.addPermanentWidget(self.statusbar_button1)  # 永久部件（右对齐）addPermanentWidget
        self.statusbar.addPermanentWidget(self.statusbar_button2)  # 永久部件（右对齐）addPermanentWidget
        

        # 设置布局方向
        self.statusbar.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStatusBar(self.statusbar)


        self.main_body.setStretch(0, 0)
        self.main_body.setStretch(1, 10)
        
        self.gridLayout.addLayout(self.main_body, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.Sub_window)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_0.setText(_translate("MainWindow", "提示框"))
