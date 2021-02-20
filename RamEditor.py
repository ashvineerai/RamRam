
#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class RamEditor(QWidget):
    def __init__(self, dictRamRam):
        self.dictRamRam=dictRamRam
        super(RamEditor, self).__init__()
        PyQt5.uic.loadUi('ui/EditorRamForm.ui', self)
        print("Ram Ram Editor")
        #print(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setWindowFlags( Qt.WindowCloseButtonHint )

        #btnWelcomeEnter
        self.editorRam = self.findChild(QTextEdit, 'editorRam') # Find the button
        #print(dir(self.editorRam ))
        self.editorRam.keyPressEvent=self.typingRam
        #self.editorRam.textChanged.connect(self.typingRam)
        self.lblCount = self.findChild(QLabel, 'lblCount') # Find the button
        self.lblCount.setText(self.dictRamRam['nameLabel'])
        #self.btnWelcomeEnter.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!
        
        self.show()

        
    def typingRam(self, event):
        newChar=event.text()
        text=self.editorRam.toPlainText()
        if(len(text) == 0):
            text="R"
        else:    
            lastChar = text[-1]
            if(lastChar == " "):
                text=text+"R"

            if(lastChar == "R"):
                text=text+"a"

            if(lastChar == "a"):
                text=text+"m"

            if(lastChar == "m"):
                text=text+" "

        #text=text+newChar
        self.editorRam.setText(text)
        #print("Key Press:"+newChar)
        event.accept()
        return
        #pass

    def closeEvent(self, event):
        #print('close event clicked ....')

        quit_msg = "Are you Hindu?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.dictRamRam["ramRamClass"].show()
            #print('OKKKKK ....')
        else:
            #print('Nooooo ....')
            event.ignore() 


