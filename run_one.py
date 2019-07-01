# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from widget_new import Ui_Form
from PyQt5.QtCore import pyqtSignal, Qt


class MyMainWindow(QMainWindow, Ui_Form):

    printSignal_run = pyqtSignal(list)
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #run按钮需要的信号链接
        self.run_Button.clicked.connect(self.emitPrintSignal_run)
        self.printSignal_run.connect(self.printResult_run)

    def emitPrintSignal_run(self):
        #计算结果，例如：
        run_list=[]
        run_list.append(-1*self.doubleSpinBox_min.value())
        run_list.append(self.doubleSpinBox_max.value())
        run_list.append(self.comboBox_way.currentText())
        run_list.append(self.spinBox_pointnumber.value())
        self.printSignal_run.emit(run_list)
    def printResult_run(self,list):
        # list中的元素按顺序为：体积变化上下限、取点方式、取点个数
        self.resultLabel_volume.setText("Volume scale:  "+str(list[0])+"~"+str(list[1]))
        self.resultLabel_pointway.setText("Point method: "+str(list[2]))
        self.resultLabel_pointnumber.setText("Point number: "+str(list[3]))

        # 打印最终结果，暂时没有算法，简单分类讨论
        if (list[2]=="Uniform point"):
            self.resultLabel_run.setText("The result of the Uniform point:\n ……")
        elif(list[2]=="Chebyshev point"):
            self.resultLabel_run.setText("The result of the Chebyshev point:\n ……")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
