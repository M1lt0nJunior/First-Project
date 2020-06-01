#from PyQt5 import uic,QtWidgets

import qt
import sys

from interface import *

def funcao_principal():
    print("teste")


    app=QtWidgets.QApplication([])
    formulario=uic.loadUi("formulario.ui")
    formulario.btnSave.clicked.connect(funcao_principal)

    formulario.show()
    app.exec()