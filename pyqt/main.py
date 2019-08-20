# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:46:40 2019

@author: Hossain
"""

# Always copy the *.ui file to the C:\Users\Hossain\AppData\Local\Continuum\anaconda3\ directory

# Fix qt import error
# Include this file before import PyQt5 

import sys
import os
from PyQt5 import QtGui, uic, QtWidgets
import copy_file

ui_file = 'cricket_scorer.ui'

# qtCreatorFile = "cricket_scorer.ui" # Enter file here.
qtCreatorFile = os.path.join(os.path.dirname(sys.executable), ui_file)
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

copy_file.copy_to_anaconda3(ui_file) # Required to run in spyder without ERROR!

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    # Skeleton function
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        # Start calling new functions below
#        self.calc_tax_button.clicked.connect(self.CalculateTax)
#    
#    def CalculateTax(self):
#        price = int(self.price_box.toPlainText())
#        tax = (self.tax_rate.value())
#        total_price = price  + ((tax / 100) * price)
#        total_price_string = "The total price with tax is: " + str(total_price)
#        self.results_window.setText(total_price_string)

# Main method
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
