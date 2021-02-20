
import PyQt5.QtCore
import PyQt5.uic
from PyQt5.QtWidgets import *
import sys
from RamEditor import RamEditor

class RamRam(QMainWindow):
    def __init__(self):
        super(RamRam, self).__init__()
        PyQt5.uic.loadUi('ui/WelcomeForm.ui', self)
        #self.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint) 

        #btnWelcomeEnter
        self.btnWelcomeEnter = self.findChild(QPushButton, 'btnWelcomeEnter') # Find the button
        self.textUserName = self.findChild(QLineEdit, 'textUserName') # Find the button


        self.btnWelcomeEnter.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        
        #self.button = self.findChild(QtWidgets.QPushButton, 'printButton') # Find the button
        #self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        #self.input = self.findChild(QtWidgets.QLineEdit, 'input')

        self.show()

    def printButtonPressed(self):
        print('Welcome button Click ....')
        dictRamRam={}
        dictRamRam["ramRamClass"]= self

        textUserName=self.textUserName.text()

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
