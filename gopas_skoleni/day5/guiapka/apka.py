from PyQt6 import QtCore, QtGui,QtWidgets
from PyQt6.QtWidgets import QWidget
import okno
import sys,time

class MyDialog(QtWidgets.QDialog,okno.Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

    def vloz(self):
        time.sleep(3)
        text = self.lineEdit.text() #ctenim dokumentace zjistim ze prectu z lineeidtu metodou text()
        if (len(text)>1):
            self.listWidget.addItem(text)
            self.lineEdit.clear() #vymaze ten text z line editu kterej jsme vlozili

    def smaz(self):
        row = self.listWidget.currentRow() #to vrati index te radky na ktere jsme ; getItem() by vratilo obsah
        self.listWidget.takeItem(row)   
#takhle se vytvori apliakce
app = QtWidgets.QApplication(sys.argv)
dialog = MyDialog()
dialog.show()

app.exec() #bez podtrzitka naka pythonova
