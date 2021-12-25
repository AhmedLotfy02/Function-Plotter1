from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog
from Plot import *
from PopUpMess import *
import sys

class UI(QDialog ):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('app.ui', self)        
        self.plotButton.clicked.connect(self.on_click)
 
    def on_click(self):
        try:
            p1=Plot(self.func.text(),self.minValue.text(),self.maxValue.text())
            p1.plotFunction()
            
        except ValueError as err:
            err_message = err.args[0]
            PopUpMessage(self, err_message)
            return
                


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    currWindow.show()
    sys.exit(application.exec_())