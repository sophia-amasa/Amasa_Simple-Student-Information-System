#Amasa, Sophia Nicolette C.
#CCC151 CS2
#Simple Student Information System

import sys
import csv
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QPushButton, QTextEdit, QLabel, QComboBox, QMessageBox

data = []
info = []
header = []

def openFile(): #Function to open csv file
    with open("Student_info.csv",newline="") as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row)
        header.append(data[0])
        data.remove(header[0])
         
def updateFile(): #Function to update csv file
    with open("Student_info.csv","w",newline="") as f:
        Writer=csv.writer(f)
        Writer.writerows(header)
        Writer.writerows(data)
        print("File has been updated")
        
def search(index, info): #Function for searching using ID No.
    for sublist in data:
        if sublist[index] == info:
            return sublist

class MainWindow(QMainWindow): #UI for Main Window
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("mainWindow.ui", self)

        self.idTextEdit = self.findChild(QTextEdit, "textEdit")
        
        self.searchButton = self.findChild(QPushButton, "pushButton")
        self.searchButton.clicked.connect(self.searchStudent)
        
        self.editButton = self.findChild(QPushButton, "pushButton_2")
        self.editButton.clicked.connect(self.editStudent)
        
        self.deleteButton = self.findChild(QPushButton, "pushButton_3")
        self.deleteButton.clicked.connect(self.deleteStudent)
        
        self.addButton = self.findChild(QPushButton, "pushButton_4")
        self.addButton.clicked.connect(self.gotoAddStudentScreen)

        self.clearButton = self.findChild(QPushButton, "pushButton_5")
        self.clearButton.clicked.connect(self.clearStudents)

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

        self.tableWidget.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.allStudents()

    def gotoAddStudentScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def clearStudents(self): #Function to clear search box
        self.idTextEdit.setPlainText("")
        self.allStudents()
        
    def display(self, row, student): #Function to display
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(student[3]))  
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
        
    def on_selectionChanged(self, selected, deselected): #Function for getting item when clicked
        for ix in selected.indexes():
            if info:
                info.remove(info[0])
            it = self.tableWidget.item(ix.row(), ix.column())
            self.it_text = it.text()
            info.append(search(ix.column(), self.it_text))

    def Popup(self, text): #Function to open Pop-up
        self.showPopup = PopupWindow()
        self.showPopup.label.setText(text)
        self.showPopup.show()
        
    def allStudents(self): #Function to display all students on table
        data.sort()
        row=0
        self.tableWidget.setRowCount(len(data))
        for student in data:
            self.display(row, student)
            row=row+1

    def editStudent(self): #Function for editing students
        addStudent.addPlainText()
        addStudent.correct = True
        addStudent.edit = True
        
        widget.setCurrentIndex(widget.currentIndex()+1)
            
    def searchStudent(self): #Function for searching students
        info = self.idTextEdit.toPlainText()
        sublist = search(0, info)
        if sublist is None:
            self.Popup('Student not Found')
        else:
            self.display(0, sublist)
            self.tableWidget.setRowCount(1)

    def deleteStudent(self): #Function for deleting students
        stud_list = info[0]
        data.remove(stud_list)
        updateFile()
        self.allStudents()
        self.Popup('Student Deleted')

class addStudentScreen(QDialog): #UI for the screen for adding students
    def __init__(self):
        super(addStudentScreen, self).__init__()
        loadUi("addStudent.ui", self)
        
        self.idTextEdit = self.findChild(QTextEdit, "textEdit")
        self.nameTextEdit = self.findChild(QTextEdit, "textEdit_2")
        self.courseTextEdit = self.findChild(QTextEdit, "textEdit_3")
        self.yearComboBox = self.findChild(QComboBox, "comboBox_2")
        self.genderComboBox = self.findChild(QComboBox, "comboBox")
        
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.xButton = self.findChild(QPushButton, "pushButton_2")

        self.correct = True
        self.edit = False

        self.addButton.clicked.connect(self.addStudent)
        self.xButton.clicked.connect(self.mainMenu)
    
    def Popup(self, text): #Function to open Pop-up
        self.showPopup = PopupWindow()
        self.showPopup.label.setText(text)
        self.showPopup.show()
        
    def addPlainText(self): #Function for inserting data to screen
        self.stud_list = info[0]
        self.idTextEdit.setPlainText(self.stud_list[0])
        self.nameTextEdit.setPlainText(self.stud_list[1])
        self.courseTextEdit.setPlainText(self.stud_list[2])
        self.yearComboBox.setCurrentText(self.stud_list[3])
        self.genderComboBox.setCurrentText(self.stud_list[4])
        
    def addStudent(self): #Function for adding students
        student_info = []
        
        while self.correct:
            id_num = self.idTextEdit.toPlainText()
            try:
                int_id1 = int(id_num[0:4])
                int_id2 = int(id_num[5:])
            except:
                self.Popup('Enter a Number')
                break
            student_info.append(id_num)

            name = self.nameTextEdit.toPlainText()
            student_info.append(name)

            course = self.courseTextEdit.toPlainText()
            student_info.append(course)

            year_level = self.yearComboBox.currentText()
            student_info.append(year_level)

            gender = self.genderComboBox.currentText()
            student_info.append(gender)
        
            self.idTextEdit.setPlainText("")
            self.nameTextEdit.setPlainText("")
            self.courseTextEdit.setPlainText("")

            data.append(student_info)
            if self.edit:
                data.remove(self.stud_list)
                self.edit = False
            updateFile()
            
            self.correct = False
            self.Popup('Student Added')
            
    def mainMenu(self): #Function to go back to main menu
        if info:
            info.remove(info[0])
        mainwindow.allStudents()
        widget.setCurrentIndex(widget.currentIndex()-1)

class PopupWindow(QDialog): #UI for Pop-up
    def __init__(self):
        super(PopupWindow,self).__init__()
        loadUi("Popup.ui", self)
        
        self.label = self.findChild(QLabel, "label")

openFile()
        
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()

mainwindow = MainWindow()
widget.addWidget(mainwindow)

addStudent = addStudentScreen()
widget.addWidget(addStudent)

widget.setFixedHeight(600)
widget.setFixedWidth(1000)
widget.show()

        
