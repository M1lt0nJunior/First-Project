from PyQt5.QtCore import *
from PyQt5.QtWidget import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineWiew
from PyQt5.QtPrintSupport import *
import sys
import sqlite3
import time
import os

class MainWindow(QMainwindow):
    def __init__(self,*args,**kwargs):
        super(Mainwindow,self).__init__(*args,**kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))




app =QApplication(sys.argsv)
if (QDialog.Accepeted == True):
   window = Mainwindow()
   window.show()
sys.exit(app.exec_())

