#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:45:51 2021

@author: elturayev
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
class Oyna(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.start()
    def start(self):
        self.a=0
        self.b=0
        self.label1=QtWidgets.QLabel(self)
        self.label1.setText("1 - O'yinchi:")
        self.label1.setGeometry(50,100,100,40)
        self.label1.setFont(QFont("Times",18))
        self.label1.adjustSize()
        self.label2=QtWidgets.QLabel(self)
        self.label2.setText("2 - O'yinchi:")
        self.label2.setGeometry(50,150,100,40)
        self.label2.setFont(QFont("Times",18))
        self.label2.adjustSize()
        self.edit1=QtWidgets.QLineEdit(self)
        self.edit1.setGeometry(220,98,160,35)
        self.edit1.setFont(QFont("Times",18))
        self.edit2=QtWidgets.QLineEdit(self)
        self.edit2.setGeometry(220,148,160,35)
        self.edit2.setFont(QFont("Times",18))
        self.next=QtWidgets.QPushButton("Next")
        self.next.setFont(QFont("Times",18))
        self.vbox=QtWidgets.QVBoxLayout(self)
        self.vbox.addStretch()
        self.vbox.addWidget(self.next)
        self.setLayout(self.vbox)
        self.b1=QtWidgets.QPushButton(self)
        self.b2=QtWidgets.QPushButton(self)
        self.b3=QtWidgets.QPushButton(self)
        self.b4=QtWidgets.QPushButton(self)
        self.b5=QtWidgets.QPushButton(self)
        self.b6=QtWidgets.QPushButton(self)
        self.b7=QtWidgets.QPushButton(self)
        self.b8=QtWidgets.QPushButton(self)
        self.b9=QtWidgets.QPushButton(self)
        self.l1=QtWidgets.QTextBrowser(self)
        self.l=QtWidgets.QTextBrowser(self)
        self.l.setGeometry(0,0,400,45)
        self.l.setText("     X va O o'yiniga xush kelibsiz!")
        self.l.setFont(QFont("Times",18))
        self.next.clicked.connect(self.boshlash)
    def boshlash(self):
        if (self.edit1.text()=='' and self.edit2.text()=='') or (self.edit1.text()!='' and self.edit2.text()=='') or (self.edit1.text()=='' and self.edit2.text()!=''):
            self.next.setEnabled(True)
        else:
            ism=self.edit1.text()
            ism1=self.edit2.text()
            self.l1.setGeometry(0,0,400,30)
            self.l1.setText(f"   {ism} - X          {ism1} - O")
            self.l1.setFont(QFont("Times",15))
    
            self.next.setEnabled(False)
            self.label1.close()
            self.label2.close()
            self.edit1.close()
            self.edit2.close()
            self.l.close()
            self.b1.setGeometry(50,40,90,90)
            self.b2.setGeometry(150,40,90,90)
            self.b3.setGeometry(250,40,90,90)
            self.b4.setGeometry(50,150,90,90)
            self.b5.setGeometry(150,150,90,90)
            self.b6.setGeometry(250,150,90,90)
            self.b7.setGeometry(50,260,90,90)
            self.b8.setGeometry(150,260,90,90)
            self.b9.setGeometry(250,260,90,90)
            self.b1.clicked.connect(self.bos)
            self.b1.setCheckable(True)
            self.b2.clicked.connect(self.bos)
            self.b2.setCheckable(True)
            self.b3.clicked.connect(self.bos)
            self.b3.setCheckable(True)
            self.b4.clicked.connect(self.bos)
            self.b4.setCheckable(True)
    
            self.b5.clicked.connect(self.bos)
            self.b5.setCheckable(True)
    
            self.b6.clicked.connect(self.bos)
            self.b6.setCheckable(True)
    
            self.b7.clicked.connect(self.bos)
            self.b7.setCheckable(True)
    
            self.b8.clicked.connect(self.bos)
            self.b8.setCheckable(True)
    
            self.b9.clicked.connect(self.bos)
            self.b9.setCheckable(True)

    def bos(self):
        if self.b1.isChecked() and self.a==0:
            self.b1.setText("X")
            self.b1.setFont(QFont("Times",40))
            self.b1.setCheckable(True)
            self.b1.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b1.isChecked() and self.a==1:
            self.b1.setText("O")
            self.b1.setFont(QFont("Times",40))
            self.b1.setCheckable(True)
            self.b1.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b2.isChecked() and self.a==0:
            self.b2.setText("X")
            self.b2.setFont(QFont("Times",40))
            self.b2.setCheckable(True)
            self.b2.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b2.isChecked() and self.a==1:
            self.b2.setText("O")
            self.b2.setFont(QFont("Times",40))
            self.b2.setCheckable(True)
            self.b2.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b3.isChecked() and self.a==0:
            self.b3.setText("X")
            self.b3.setFont(QFont("Times",40))
            self.b3.setCheckable(True)
            self.b3.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b3.isChecked() and self.a==1:
            self.b3.setText("O")
            self.b3.setFont(QFont("Times",40))
            self.b3.setCheckable(True)
            self.b3.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b4.isChecked() and self.a==0:
            self.b4.setText("X")
            self.b4.setFont(QFont("Times",40))
            self.b4.setCheckable(True)
            self.b4.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b4.isChecked() and self.a==1:
            self.b4.setText("O")
            self.b4.setFont(QFont("Times",40))
            self.b4.setCheckable(True)
            self.b4.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b5.isChecked() and self.a==0:
            self.b5.setText("X")
            self.b5.setFont(QFont("Times",40))
            self.b5.setCheckable(True)
            self.b5.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b5.isChecked() and self.a==1:
            self.b5.setText("O")
            self.b5.setFont(QFont("Times",40))
            self.b5.setCheckable(True)
            self.b5.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b6.isChecked() and self.a==0:
            self.b6.setText("X")
            self.b6.setFont(QFont("Times",40))
            self.b6.setCheckable(True)
            self.b6.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b6.isChecked() and self.a==1:
            self.b6.setText("O")
            self.b6.setFont(QFont("Times",40))
            self.b6.setCheckable(True)
            self.b6.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b7.isChecked() and self.a==0:
            self.b7.setText("X")
            self.b7.setFont(QFont("Times",40))
            self.b7.setCheckable(True)
            self.b7.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b7.isChecked() and self.a==1:
            self.b7.setText("O")
            self.b7.setFont(QFont("Times",40))
            self.b7.setCheckable(True)
            self.b7.setCheckable(False)
            self.b=self.b+1
            self.a=0
        if self.b8.isChecked() and self.a==0:
            self.b8.setText("X")
            self.b8.setFont(QFont("Times",40))
            self.b8.setCheckable(True)
            self.b8.setCheckable(False)
            self.b=self.b+1
            self.a=1
        elif self.b8.isChecked() and self.a==1:
            self.b8.setText("O")
            self.b8.setFont(QFont("Times",40))
            self.b8.setCheckable(True)
            self.b8.setCheckable(False)
            self.a=0
        if self.b9.isChecked() and self.a==0:
            self.b9.setText("X")
            self.b9.setFont(QFont("Times",40))
            self.b9.setCheckable(True)
            self.b9.setCheckable(False)
            self.a=1
            self.b=self.b+1
        elif self.b9.isChecked() and self.a==1:
            self.b9.setText("O")
            self.b9.setFont(QFont("Times",40))
            self.b9.setCheckable(True)
            self.b9.setCheckable(False)
            self.a=0
            self.b=self.b+1

        if self.b1.text()==self.b2.text() and self.b2.text()==self.b3.text():
            if self.b1.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b1.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b4.text()==self.b5.text() and self.b5.text()==self.b6.text():
            if self.b4.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b4.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b7.text()==self.b8.text() and self.b8.text()==self.b9.text():
            if self.b7.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b7.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b1.text()==self.b4.text() and self.b4.text()==self.b7.text():
            if self.b7.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b7.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b2.text()==self.b5.text() and self.b5.text()==self.b8.text():
            if self.b2.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b2.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b3.text()==self.b6.text() and self.b6.text()==self.b9.text():
            if self.b3.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b3.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b1.text()==self.b5.text() and self.b5.text()==self.b9.text():
            if self.b1.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b1.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b3.text()==self.b5.text() and self.b5.text()==self.b7.text():
            if self.b7.text()=='X':
                bir=self.edit1.text()
                QMessageBox.about(self,"Win",f"{bir} yutdi")
            if self.b7.text()=='O':
                ikki=self.edit2.text()
                QMessageBox.about(self,"Win",f"{ikki} yutdi")
        if self.b==9:
            ikki=self.edit2.text()
            bir=self.edit1.text()
            QMessageBox.about(self,"Precedent",f"{bir} va {ikki} durrang!")

app=QtWidgets.QApplication(sys.argv)
ob=Oyna()
ob.show()
ob.setGeometry(400,350,400,450)
ob.setWindowTitle("O'yin - X va O")
sys.exit(app.exec_())
