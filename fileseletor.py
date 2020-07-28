import sys
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog


app=QApplication(sys.argv)

widget=QWidget()

def openFile():
    option=QFileDialog.Options()
    file=QFileDialog.getOpenFileName(widget,"Open Single File","Default File","All Files(*)",options=option)
    locations=file[0]
    print(locations)
    return locations