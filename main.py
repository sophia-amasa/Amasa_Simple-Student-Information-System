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

        self.displayStudentButton = self.findChild(QPushButton, "pushButton")
        self.displayStudentButton.clicked.connect(self.gotoDisplayStudentScreen)
        
        self.addStudentButton = self.findChild(QPushButton, "pushButton_2")
        self.addStudentButton.clicked.connect(self.gotoAddStudentScreen)

        self.searchButton = self.findChild(QPushButton, "pushButton_5")
        self.searchButton.clicked.connect(self.gotoSearchStudentScreen)

    def gotoDisplayStudentScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)   
    def gotoAddStudentScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
    def gotoSearchStudentScreen(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

class displayStudentScreen(QDialog): #UI for the screen for displaying list of students
    def __init__(self):
        super(displayStudentScreen, self).__init__()
        loadUi("displayStudent.ui", self)

        self.xButton = self.findChild(QPushButton, "pushButton_3")
        self.xButton.clicked.connect(self.mainMenu)

        self.loaddata()

    def mainMenu(self): #Function to go back to main menu
        self.clear()
        self.loaddata()
        widget.setCurrentIndex(widget.currentIndex()-1)

    def loaddata(self): #Function to display students on table
        sort_stud = sorted(data)
        row=0
        self.tableWidget.setRowCount(len(data))
        for student in sort_stud:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student[0]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(student[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(student[4]))
            row=row+1
        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)

    def clear(self): #Function for clearing table
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        
class addStudentScreen(QDialog): #UI for the screen for adding students
    def __init__(self):
        super(addStudentScreen, self).__init__()
        loadUi("addStudent.ui", self)
        
        self.idTextEdit = self.findChild(QTextEdit, "textEdit")
        self.nameTextEdit = self.findChild(QTextEdit, "textEdit_2")
        self.courseTextEdit = self.findChild(QTextEdit, "textEdit_3")
        self.yearComboBox = self.findChild(QComboBox, "comboBox_2")
        self.genderComboBox = self.findChild(QComboBox, "comboBox")

        self.label = self.findChild(QLabel, "label_7")
        
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.xButton = self.findChild(QPushButton, "pushButton_2")

        self.correct = True

        self.addButton.clicked.connect(self.addStudent)
        self.xButton.clicked.connect(self.mainMenu)
        
    def addStudent(self): #Function for adding students
        student_info = []
        
        while self.correct:
            id_num = self.idTextEdit.toPlainText()
            try:
                int_id1 = int(id_num[0:4])
                int_id2 = int(id_num[5:])
            except:
                self.ErrorPopup()
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

            self.label.setText(f'Student Added')

            data.append(student_info)
            updateFile()
            self.correct = False
            
    def ErrorPopup(self):#Function to open Error Pop-up
        self.showError = ErrorWindow()
        self.showError.show()
        
    def mainMenu(self): #Function to go back to main menu
        widget.setCurrentIndex(widget.currentIndex()-2)
        
class ErrorWindow(QDialog): #UI for Error Pop-up
    def __init__(self):
        super(ErrorWindow,self).__init__()
        loadUi("errorPopup.ui", self)
        
class edit(QDialog):#UI for the screen for editing students
    def __init__(self):
        super(edit, self).__init__()
        loadUi("edit.ui", self)
        
        self.idTextEdit = self.findChild(QTextEdit, "textEdit")
        self.nameTextEdit = self.findChild(QTextEdit, "textEdit_2")
        self.courseTextEdit = self.findChild(QTextEdit, "textEdit_3")
        self.yearComboBox = self.findChild(QComboBox, "comboBox_2")
        self.genderComboBox = self.findChild(QComboBox, "comboBox")

        self.stud_list=[]
        self.addPlainText()
        self.correct = True

        self.label = self.findChild(QLabel, "label_7")
        
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.xButton = self.findChild(QPushButton, "pushButton_2")

        self.addButton.clicked.connect(self.editStudent)
        self.xButton.clicked.connect(self.goBack)

    def addPlainText(self): #Function for inserting data to screen
        self.stud_list = search(0, info[0])
        self.idTextEdit.setPlainText(self.stud_list[0])
        self.nameTextEdit.setPlainText(self.stud_list[1])
        self.courseTextEdit.setPlainText(self.stud_list[2])
        
    def editStudent(self): #Function for editing students
        
        student_info = []

        while self.correct:
            id_num = self.idTextEdit.toPlainText()
            try:
                int_id1 = int(id_num[0:4])
                int_id2 = int(id_num[5:])
            except:
                self.ErrorPopup()
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

            self.label.setText(f'Student Added')

            data.append(student_info)
            data.remove(self.stud_list)
            updateFile()
            self.correct = False
            
    def ErrorPopup(self): #Function to open Error Pop-up
        self.showError = ErrorWindow()
        self.showError.show()
        
    def goBack(self): #Function to go back to another screen
        self.idTextEdit.clear()
        self.nameTextEdit.clear()
        self.courseTextEdit.clear()
        info.remove(info[0])
        widget.setCurrentIndex(widget.currentIndex()-1)
    
class searchStudentScreen(QDialog):#UI for the screen for searching students
    def __init__(self):
        super(searchStudentScreen, self).__init__()
        loadUi("searchStudent.ui", self)
        
        self.idTextEdit = self.findChild(QTextEdit, "textEdit_6")
        self.searchButton = self.findChild(QPushButton, "pushButton_2")
        self.xButton = self.findChild(QPushButton, "pushButton_3")
        self.editButton = self.findChild(QPushButton, "pushButton_4")
        self.deleteButton = self.findChild(QPushButton, "pushButton_5")

        self.headerLabel = self.findChild(QLabel, "label_3")
        self.studInfoLabel = self.findChild(QLabel, "label_4")

        self.xButton.clicked.connect(self.mainMenu)
        self.searchButton.clicked.connect(self.searchStudent)
        self.editButton.clicked.connect(self.edit_student)
        self.deleteButton.clicked.connect(self.deleteStudent)
        
        self.hidden = True
        self.editButton.hide()
        self.deleteButton.hide()

    def searchStudent(self): #Function for searching students
        str_student = ''
        str_header = ''
        info = self.idTextEdit.toPlainText()
        sublist = search(0, info)
        if sublist is None:
            self.headerLabel.setText('Student not Found')
        else:
            for element in header[0]:
                str_header = str_header + ' ' + element
            for element in sublist:
                str_student = str_student + ' ' + element
            
            self.headerLabel.setText(str_header)
            self.studInfoLabel.setText(str_student)

            if self.hidden:
                self.editButton.show()
                self.deleteButton.show()
                self.hidden = False

    def edit_student(self): #Function for editing students
        idInfo = self.idTextEdit.toPlainText()
        info.append(idInfo)
        
        Edit = edit()
        widget.addWidget(Edit)
        
        widget.setCurrentIndex(widget.currentIndex()+1)

    def deleteStudent(self): #Function for deleting students
        info = self.idTextEdit.toPlainText()
        stud_list = search(0, info)
        data.remove(stud_list)
        updateFile()

    def mainMenu(self): #Function to go back to main menu
        self.idTextEdit.setText('')
        self.headerLabel.setText('')
        self.studInfoLabel.setText('')
        self.hidden = True
        self.editButton.hide()
        self.deleteButton.hide()
        widget.setCurrentIndex(widget.currentIndex()-3)
        
openFile()
        
app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()

mainwindow = MainWindow()
displayStudent = displayStudentScreen()
addStudent = addStudentScreen()
searchStudent = searchStudentScreen()

widget.addWidget(mainwindow)
widget.addWidget(displayStudent)
widget.addWidget(addStudent)
widget.addWidget(searchStudent)

widget.setFixedHeight(500)
widget.setFixedWidth(1000)
widget.show()
