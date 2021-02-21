
#import PyQt5.QtCore
from PyQt5.QtCore import *
import PyQt5.uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import threading
import time
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
        self.lblUserName = self.findChild(QLabel, 'lblUserName') # Find the button
        self.lblWordCount = self.findChild(QLabel, 'lblWordCount') # Find the button
        self.lblCountDown = self.findChild(QLabel, 'lblCountDown') # Find the button

        #Thread start here
        wcthread=threading.Thread( target=self.countDown, args=(1,))
        wcthread.start()


        
        self.lblUserName.setText(self.dictRamRam['nameLabel'])
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
        wordString=text.split()
        wordCount=len(wordString)
        self.lblWordCount.setText("{:02d}".format(wordCount))

        self.editorRam.setText(text)
        #print("Key Press:"+newChar)
        event.accept()
        return
        #pass

    def countDown(self, obj):
        countVal=0
        while True:
            self.lblCountDown.setText(self.countDownTimer(countVal))
            countVal=countVal+1
            time.sleep(1)   

    def countDownTimer(self, countVal):
        #print(str(countVal))
        hrs=int(countVal/(60*60))
        strTime="00:00:00"     
        if(hrs > 0):
            mint=int(countVal-(hrs*60*60)/60)     
            secs=countVal-hrs*60*60-mint*60
            strTime="{:02d}:{:02d}:{:02d}".format(hrs, mint, secs)
        else:
            mint=int(countVal/60)     
            if(mint > 0):
                secs=countVal-(hrs*60*60)-(mint*60)     
                strTime="00:{:02d}:{:02d}".format(mint, secs)
            else:
                strTime="00:00:{:02d}".format( countVal)
        #print(strTime)
        return strTime


    def closeEvent(self, event):
        #print('close event clicked ....')

        quit_msg = "Are you Hindu?"
        reply = QMessageBox.question(self, 'Message', quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            self.dictRamRam["ramRamClass"].show()
            #print('OKKKKK ....')
        else:
            #print('Nooooo ....')
            event.ignore() 


