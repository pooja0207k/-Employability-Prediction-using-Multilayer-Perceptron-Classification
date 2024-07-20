import sys
import os
from employability import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.mntrset)
     self.ui.pushButton_2.clicked.connect(self.crtcsv)
     self.ui.pushButton_3.clicked.connect(self.mlpc)
     self.ui.pushButton_4.clicked.connect(self.knn1)
     self.ui.pushButton_5.clicked.connect(self.acti)
     

  def mntrset(self):
    os.system("python mentservices1.py")

  def crtcsv(self):
    os.system("python createcsv1.py")

  def mlpc(self):
    os.system("python -W ignore mlpc1.py")

  def knn1(self):
    os.system("python -W ignore knn1.py")

  def acti(self):
    os.system("python activities1.py")
	


          
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
