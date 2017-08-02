# -*- coding: utf-8 -*-
import sys,os, shutil
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from _subprocess import INFINITE

class PopUp (QWidget):
    def __init__(self, message):
        super(PopUp, self).__init__()
        self.resize(QSize(100, 100))
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        #widget
        messageLabel = QLabel(message)
        messageLabel.setObjectName("popUpMessage")
        # layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(messageLabel)
        self.setLayout(mainLayout)
        #paths
        rootPath=os.path.abspath(os.curdir)
        self.rootPath=rootPath.replace('\\','/')
        self.stylePath=self.rootPath+'/stylesheet.qss'
        #stylesheet
#         stylesheetFile=QFile(self.stylePath)
#         stylesheetFile.open(QFile.ReadOnly)
#         self.setStyleSheet(QLatin1String(stylesheetFile.readAll()))
        with open('stylesheet.qss', 'r') as file:
            self.setStyleSheet(file.read())
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()

class Rename(QWidget):
    def __init__(self):
        super(Rename,self).__init__()
        self.resize(QSize(650,600))
        # Create widgets     
        pathLabel=QLabel("Path:")
        self.pathEdit=QLineEdit()
        self.pathEdit.setObjectName("pathEdit")
        self.pathEdit.setText("/Users")
        self.addPathBtn=QPushButton('Edit')
        self.addPathBtn.setObjectName("pathButton")
        self.openPathBtn=QPushButton('Open')
        self.openPathBtn.setObjectName("pathButton")
        self.helpBtn = QPushButton("Help")
        self.helpBtn.setObjectName("pathButton")
        self.tableWidget=QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Original Name", "New Name"])
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        #self.tableWidget.horizontalHeader().set(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #self.tableWidget.horizontalHeader().setResizeMode(1,QHeaderView.ResizeToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.horizontalScrollBar().setEnabled(True)
        self.tableWidget.verticalScrollBar().setEnabled(True)
        self.copyNumLabel = QLabel("Copy Number:")
        self.copyNumEdit=QSpinBox()
        self.copyNumEdit.setRange(0,10000)
        self.newNameLabel = QLabel("New Name:")
        self.newNameEdit=QLineEdit()
        self.newNameEdit.setPlaceholderText("Please Enter New Name Here")
        self.formatLabel = QLabel("File Format:")
        self.formatEdit=QLineEdit()
        self.formatEdit.setPlaceholderText("Please Enter File Format Here")
        self.startNumLabel = QLabel("Start Number:")
        self.startNumEdit=QSpinBox()
        self.startNumEdit.setRange(0,10000)
        self.stepLabel = QLabel("Step Size:")
        self.stepEdit=QSpinBox()
        self.stepEdit.setRange(1,10000)
        self.bitsLabel = QLabel("Bits:")
        self.bitsEdit=QSpinBox()    
        self.bitsEdit.setRange(0,10000)
        self.confirmBtn=QPushButton("Rename")
        self.copyBtn=QPushButton("Copy")
        self.resetBtn=QPushButton("Reset")
        self.confirmBtn.setObjectName("button")
        self.resetBtn.setObjectName("button")
        self.houdiniCheckBox = QCheckBox("For Houdini")  
        # Set layouts
        mainLayout=QVBoxLayout()
        pathBarLayout = QHBoxLayout()
        pathBarLayout.addWidget(pathLabel)
        pathBarLayout.addWidget(self.pathEdit)
        pathBarLayout.addWidget(self.addPathBtn)
        pathBarLayout.addWidget(self.openPathBtn)
        pathBarLayout.addWidget(self.helpBtn)
        pathBarLayout.setContentsMargins(0, 0, 0, 10)
        newNameLayout = QHBoxLayout()
        newNameLayout.addWidget(self.newNameLabel)
        newNameLayout.addWidget(self.newNameEdit)
        newNameLayout.addWidget(self.houdiniCheckBox)
        newNameLayout.setContentsMargins(0, 10, 0, 0)
        formatLayout = QHBoxLayout()
        formatLayout.addWidget(self.formatLabel)
        formatLayout.addWidget(self.formatEdit)
        formatLayout.setContentsMargins(0, 0, 0, 10)
        copyNumLayout = QHBoxLayout()
        copyNumLayout.addWidget(self.copyNumLabel)
        copyNumLayout.addWidget(self.copyNumEdit)
        startNumLayout = QHBoxLayout()
        startNumLayout.addWidget(self.startNumLabel)
        startNumLayout.addWidget(self.startNumEdit)
        stepLayout = QHBoxLayout()
        stepLayout.addWidget(self.stepLabel)
        stepLayout.addWidget(self.stepEdit)
        bitsLayout = QHBoxLayout()
        bitsLayout.addWidget(self.bitsLabel)
        bitsLayout.addWidget(self.bitsEdit)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.confirmBtn)
        buttonLayout.addWidget(self.copyBtn)
        buttonLayout.addWidget(self.resetBtn)
        buttonLayout.setContentsMargins(0, 10, 0, 0)
        copyNumStepLayout = QHBoxLayout()
        copyNumStepLayout.addLayout(copyNumLayout)
        copyNumStepLayout.addLayout(stepLayout)
        startNumBitsLayout = QHBoxLayout()
        startNumBitsLayout.addLayout(startNumLayout)
        startNumBitsLayout.addLayout(bitsLayout)
        mainLayout.addLayout(pathBarLayout)
        mainLayout.addWidget(self.tableWidget)
        mainLayout.addLayout(newNameLayout)
        mainLayout.addLayout(formatLayout)
        mainLayout.addLayout(copyNumStepLayout)
        mainLayout.addLayout(startNumBitsLayout)
        mainLayout.addLayout(buttonLayout)
        mainLayout.setContentsMargins(15, 15, 15, 15)
        #mainLayout.addWidget(self.tabWidget)
        self.setLayout(mainLayout)
        # Load popup windows
        self.noPathPopUp = PopUp("Current Path Does Not Exist!")
        self.missingInfoPopUp = PopUp("Make sure file name and format are both filled out!")
        self.noSelectedPopUp = PopUp("Make sure you have selected at least one file!")
        self.renameSuccessPopUp = PopUp("File(s) successfully renamed!")
        self.copySuccessPopUp = PopUp("File(s) successfully copied!")
        self.errorPopUp = PopUp("An error occurred during the process, make sure the format is appropriate and the name is available!")
        self.missingNamePopUp = PopUp("Make sure file format is filled out!")
        #paths
        rootPath=os.path.abspath(os.curdir)
        self.rootPath=rootPath.replace('\\','/')
        self.helpPath = self.rootPath + '/Help_rename.txt'
        self.stylePath=self.rootPath+'/stylesheet.qss'

        # Load styleSheet
#         stylesheetFile=QFile(self.stylePath)
#         stylesheetFile.open(QFile.ReadOnly)
#         self.setStyleSheet(QLatin1String(stylesheetFile.readAll()))
        with open('stylesheet.qss', 'r') as file:
            self.setStyleSheet(file.read())
        # Set functions
        self.confirmBtn.clicked.connect(self.confirmBtnFunc)
        self.copyBtn.clicked.connect(self.copyBtnFunc)
        self.resetBtn.clicked.connect(self.resetBtnFunc)
        self.helpBtn.clicked.connect(self.helpBtnFunc)
        self.addPathBtn.clicked.connect(self.addPathBtnFunc)
        self.openPathBtn.clicked.connect(self.openPathBtnFunc)
        self.newNameEdit.textChanged.connect(self.refreshName)
        self.formatEdit.textChanged.connect(self.refreshFormat)
        self.stepEdit.valueChanged.connect(self.refreshStep)
        self.bitsEdit.valueChanged.connect(self.refreshBits)
        self.startNumEdit.valueChanged.connect(self.refreshStartNum)
        self.tableWidget.cellClicked.connect(self.updateNameFunc)
        self.houdiniCheckBox.toggled.connect(self.refreshHoudini)
    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Escape:
            self.close()
        elif event.key()==Qt.Key_Enter or event.key()==Qt.Key_Return:
            oriPath=str(self.pathEdit.text())
            if not os.path.exists(oriPath):
                self.noPathPopUp.show()
                return
            self.refreshTable()
    def helpBtnFunc(self):
        os.open(self.helpPath)
    def copyBtnFunc(self):
        if not self.tableWidget.selectedIndexes(): 
            self.noSelectedPopUp.show()
            return
        if self.houdiniCheckBox.isChecked():
            if not self.newNameEdit.text() or not self.formatEdit.text():
                self.missingInfoPopUp.show()
                return
        else:
            if not self.formatEdit.text():
                self.missingNamePopUp.show()
                return
        curPath=str(self.pathEdit.text())
        item = self.tableWidget.selectedIndexes()[0]
        currRow = item.row()
        if currRow==-1:return
        curItem=str(self.tableWidget.cellWidget(currRow,0).objectName())
        newName = self.newNameEdit.text()
        startNum = self.startNumEdit.text()
        fileFormat = self.formatEdit.text()
        bits = self.bitsEdit.text()
        bits = int(bits)
        stepSize = self.stepEdit.text()
        stepSize = int(stepSize)
        for i in range(self.copyNumEdit.value()):
            startNum = str(startNum)
            newNum = startNum.zfill(bits)
            if self.houdiniCheckBox.isChecked():
                newVersion = newName + "." + newNum + "." + fileFormat
            else:
                newVersion = newName + newNum + "." + fileFormat   
            curNewName = curPath + "/" + str(newVersion)
            shutil.copy2(curItem, curNewName)
            startNum = int(startNum)
            startNum += stepSize
        self.copySuccessPopUp.show()
        self.refreshTable()
    def confirmBtnFunc(self):
        if not self.tableWidget.selectedIndexes(): 
            self.noSelectedPopUp.show()
            return
        if self.houdiniCheckBox.isChecked():
            if not self.newNameEdit.text() or not self.formatEdit.text():
                self.missingInfoPopUp.show()
                return
        else:
            if not self.formatEdit.text():
                self.missingNamePopUp.show()
                return
        curPath=str(self.pathEdit.text())
        for item in self.tableWidget.selectedIndexes():
            currRow = item.row()
            if currRow==-1:return
            curItem=str(self.tableWidget.cellWidget(currRow,0).objectName())
            curNewName = curPath + "/" + str(self.tableWidget.cellWidget(currRow, 1).objectName())
            try:
                os.rename(curItem, curNewName)
            except:
                self.errorPopUp.show()
                return
        self.renameSuccessPopUp.show()
        self.refreshTable()
    def resetBtnFunc(self):
        self.tableWidget.clearSelection()
        self.newNameEdit.clear()
        self.formatEdit.clear()
        self.newNameEdit.setPlaceholderText("Please Enter New Name Here")
        self.formatEdit.setPlaceholderText("Please Enter File Format Here")
        self.stepEdit.setValue(1)
        self.bitsEdit.setValue(0)
        self.startNumEdit.setValue(0)
        self.copyNumEdit.setValue(0)
        self.updateNameFunc()
    def addPathBtnFunc(self):
        oriPath=str(self.pathEdit.text())
        tarPath=QFileDialog.getExistingDirectory(directory=oriPath,caption="Please select a path",options=QFileDialog.ShowDirsOnly)
        if not tarPath or tarPath==oriPath:return
        self.pathEdit.setText(tarPath)
        self.refreshTable()
    def refreshHoudini(self):
        self.updateNameFunc()
    def refreshBits(self):
        self.updateNameFunc()
    def refreshStartNum(self):
        self.updateNameFunc()
    def refreshStep(self):
        self.updateNameFunc()
    def refreshName(self):
        self.updateNameFunc()
    def refreshFormat(self):
        self.updateNameFunc()
    def updateNameFunc(self):
        #first, clear the column
        self.tableWidget.removeColumn(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Original Name", "New Name"])
        newName = self.newNameEdit.text()
        startNum = self.startNumEdit.text()
        fileFormat = self.formatEdit.text()
        bits = self.bitsEdit.text()
        bits = int(bits)
        stepSize = self.stepEdit.text()
        stepSize = int(stepSize)
        for item in self.tableWidget.selectedIndexes():
            indexNum = item.row()
            startNum = str(startNum)
            newNum = startNum.zfill(bits)
            if self.houdiniCheckBox.isChecked():
                newVersion = newName + "." + newNum + "." + fileFormat
            else:
                newVersion = newName + newNum + "." + fileFormat        
            nameLabel=QLabel(newVersion)
            rowLayout=QHBoxLayout()
            rowLayout.addWidget(nameLabel)
            rowWidget=QWidget()
            rowWidget.setLayout(rowLayout)
            rowLayout.setContentsMargins(10, 0, 10, 0)
            rowLayout.setSpacing(0)
            rowWidget.setStyleSheet("background:transparent")
            rowWidget.setObjectName(newVersion)
            self.tableWidget.setCellWidget(indexNum,1,rowWidget)
            #update number
            startNum = int(startNum)
            startNum += stepSize
    def openPathBtnFunc(self):
        oriPath=str(self.pathEdit.text())
        if not os.path.exists(oriPath):
            #open pop up window
            self.noPathPopUp.show()
            return
        #os.startfile(oriPath)
        os.popen(oriPath)
    def refreshTable(self):
        curPath=str(self.pathEdit.text())
        if not curPath:return
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        curFiles=[item for item in os.listdir(curPath.replace("\\", "/"))]
        if not curFiles:return
        rowCount=len(curFiles)
        self.tableWidget.setRowCount(rowCount)
        fileList=[]
        #Fill original names
        for row in range(rowCount):
            curItem=curPath+"/"+curFiles[row]
            fileInfor=QFileInfo(curItem)
            iconLabel=QLabel()
            iconLabel.setFixedSize(QSize(20,20))
            nameLabel=QLabel(curFiles[row])
            rowLayout=QHBoxLayout()
            rowLayout.addWidget(iconLabel)
            rowLayout.addWidget(nameLabel)
            rowWidget=QWidget()
            rowWidget.setLayout(rowLayout)
            rowLayout.setContentsMargins(0, 0, 0, 0)
            rowLayout.setSpacing(0)
            rowWidget.setStyleSheet("background:transparent")
            rowWidget.setObjectName(curItem)
            if fileInfor.isFile():
                iconProvider=QFileIconProvider()
                fileIcon=QIcon(iconProvider.icon(fileInfor))
                iconLabel.setPixmap(QPixmap(fileIcon.pixmap(QSize(18,18))))
                fileList.append(rowWidget)
        if fileList:
            i=0
            for i,item in enumerate(fileList):
                rowWidget=fileList[i]
                self.tableWidget.setCellWidget(i,0,rowWidget)  
if __name__ == "__main__":
    app=QApplication(sys.argv)
    rename=Rename()
    rename.showNormal()
    sys.exit(app.exec_())