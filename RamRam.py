
import PyQt5.QtCore
import PyQt5.uic
import PyQt5.QtGui
from PyQt5.QtWidgets import *
import sys
from RamEditor import RamEditor

class RamRam(QMainWindow):
    def __init__(self):
        super(RamRam, self).__init__()
        PyQt5.uic.loadUi('ui/WelcomeForm.ui', self)
        #self.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint) 
        self.setWindowIcon(PyQt5.QtGui.QIcon('balloon.svg')) 

        self.developedBy()
        
        #btnWelcomeEnter
        self.btnWelcomeEnter = self.findChild(QPushButton, 'btnWelcomeEnter') # Find the button
        self.textUserName = self.findChild(QLineEdit, 'textUserName') # Find the button

        #self.textUserName.clicked.connect(self.printButtonPressed)
        self.textUserName.returnPressed.connect(self.btnWelcomeEnter.click)
        self.btnWelcomeEnter.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.show()

    def developedBy(self):
        developedby = self.findChild(QLabel, 'developedby') # Find the button
        developedby.setText("<a href='https://github.com/eashvinee'>github:eashvinee</a>")
        developedby.setOpenExternalLinks(True)


    def printButtonPressed(self):
        print('Welcome button Click ....')
        dictRamRam={}
        dictRamRam["ramRamClass"]= self

        textUserName=self.textUserName.text()
        self.textUserName.setText("")

        if(textUserName.strip()):
            dictRamRam["nameLabel"]= textUserName
            #print(dictRamRam)
            #print("Your Name is: "+textUserName)
            self.hide()
            self.ramEditor= RamEditor(dictRamRam)
        else:
            QMessageBox.about(self, "Alert", "Please enter name.")
            print("Please enter name: ")

        
        #textUserName
        #dictRamRam.push("txtUserName",   )
        # This is executed when the button is pressed
        #print('Input text:' + self.input.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RamRam()
    app.exec_()
