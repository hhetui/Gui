# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget_new.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(819, 493)
        self.groupBox_input = QtWidgets.QGroupBox(Form)
        self.groupBox_input.setGeometry(QtCore.QRect(50, 20, 391, 441))
        self.groupBox_input.setStyleSheet("")
        self.groupBox_input.setObjectName("groupBox_input")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_input)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 301, 30))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_volume = QtWidgets.QLabel(self.layoutWidget)
        self.label_volume.setObjectName("label_volume")
        self.horizontalLayout.addWidget(self.label_volume)
        self.label_negative = QtWidgets.QLabel(self.layoutWidget)
        self.label_negative.setObjectName("label_negative")
        self.horizontalLayout.addWidget(self.label_negative)
        self.doubleSpinBox_min = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_min.setObjectName("doubleSpinBox_min")
        self.horizontalLayout.addWidget(self.doubleSpinBox_min)
        self.label_to = QtWidgets.QLabel(self.layoutWidget)
        self.label_to.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_to.setObjectName("label_to")
        self.horizontalLayout.addWidget(self.label_to)
        self.doubleSpinBox_max = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_max.setObjectName("doubleSpinBox_max")
        self.horizontalLayout.addWidget(self.doubleSpinBox_max)
        self.run_Button = QtWidgets.QPushButton(self.groupBox_input)
        self.run_Button.setGeometry(QtCore.QRect(150, 350, 61, 28))
        self.run_Button.setObjectName("run_Button")
        self.widget = QtWidgets.QWidget(self.groupBox_input)
        self.widget.setGeometry(QtCore.QRect(30, 150, 291, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_way = QtWidgets.QLabel(self.widget)
        self.label_way.setObjectName("label_way")
        self.horizontalLayout_2.addWidget(self.label_way)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox_way = QtWidgets.QComboBox(self.widget)
        self.comboBox_way.setObjectName("comboBox_way")
        self.comboBox_way.addItem("")
        self.comboBox_way.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_way)
        self.widget1 = QtWidgets.QWidget(self.groupBox_input)
        self.widget1.setGeometry(QtCore.QRect(30, 240, 241, 23))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_number = QtWidgets.QLabel(self.widget1)
        self.label_number.setObjectName("label_number")
        self.horizontalLayout_3.addWidget(self.label_number)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.spinBox_pointnumber = QtWidgets.QSpinBox(self.widget1)
        self.spinBox_pointnumber.setObjectName("spinBox_pointnumber")
        self.horizontalLayout_3.addWidget(self.spinBox_pointnumber)
        self.groupBox_output = QtWidgets.QGroupBox(Form)
        self.groupBox_output.setGeometry(QtCore.QRect(470, 20, 331, 441))
        self.groupBox_output.setObjectName("groupBox_output")
        self.resultLabel_volume = QtWidgets.QLabel(self.groupBox_output)
        self.resultLabel_volume.setGeometry(QtCore.QRect(30, 60, 271, 41))
        self.resultLabel_volume.setMouseTracking(True)
        self.resultLabel_volume.setObjectName("resultLabel_volume")
        self.resultLabel_pointway = QtWidgets.QLabel(self.groupBox_output)
        self.resultLabel_pointway.setGeometry(QtCore.QRect(30, 140, 271, 51))
        self.resultLabel_pointway.setObjectName("resultLabel_pointway")
        self.resultLabel_pointnumber = QtWidgets.QLabel(self.groupBox_output)
        self.resultLabel_pointnumber.setGeometry(QtCore.QRect(30, 220, 271, 41))
        self.resultLabel_pointnumber.setObjectName("resultLabel_pointnumber")
        self.resultLabel_run = QtWidgets.QLabel(self.groupBox_output)
        self.resultLabel_run.setGeometry(QtCore.QRect(30, 290, 271, 91))
        self.resultLabel_run.setObjectName("resultLabel_run")
        self.groupBox_output.raise_()
        self.groupBox_input.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_input.setTitle(_translate("Form", "input"))
        self.label_volume.setText(_translate("Form", "Volume scale："))
        self.label_negative.setText(_translate("Form", "-"))
        self.label_to.setText(_translate("Form", "~"))
        self.run_Button.setText(_translate("Form", "run"))
        self.label_way.setText(_translate("Form", "Take point way："))
        self.comboBox_way.setItemText(0, _translate("Form", "Uniform point"))
        self.comboBox_way.setItemText(1, _translate("Form", "Chebyshev point"))
        self.label_number.setText(_translate("Form", "Point number："))
        self.groupBox_output.setTitle(_translate("Form", "output"))
        self.resultLabel_volume.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.resultLabel_pointway.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.resultLabel_pointnumber.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.resultLabel_run.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))

