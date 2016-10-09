import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
 
servidorUi = uic.loadUiType("servidor2.ui")[0] #Se carga la interfaz de tipo ui del servidor
 
class Servidor(QtGui.QMainWindow, servidorUi):

 	def __init__(self, parent=None):#Constructor de la ventana
 		QtGui.QMainWindow.__init__(self, parent)
 		self.setupUi(self)#Inicializa la interfaz del tipo ui
 		self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch) #Como su nombre lo dice estira a las columnas horizontales para adaptarse a la widget
 		self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch) #Lo mismo para las verticales
 		self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #Cuando las celdas son bastantes, la scrollbar aparece, este basicamente las hace desaparecer
 		self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #Tambien las verticales (Con las de 20 columnas, 20 filas, aparecía)
   	
#Inicia la aplicacion.
def main():
    app = QtGui.QApplication(sys.argv)
    win = Servidor()
    win.show()
    app.exec_()
    
main()
