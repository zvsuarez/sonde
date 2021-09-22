# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_ui.ui'
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 620)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.codeBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.codeBox.setFont(font)
        self.codeBox.setIconSize(QtCore.QSize(20, 20))
        self.codeBox.setObjectName("codeBox")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.codeBox.addItem("")
        self.gridLayout.addWidget(self.codeBox, 0, 0, 1, 1)

        self.inputclearButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.inputclearButton.setFont(font)
        self.inputclearButton.setObjectName("inputclearButton")
        self.gridLayout.addWidget(self.inputclearButton, 0, 2, 1, 1)

        self.inputTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.inputTextEdit.setFont(font)
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.inputTextEdit.setAcceptRichText(False)
        self.gridLayout.addWidget(self.inputTextEdit, 1, 0, 1, 3)

        self.decodeButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.decodeButton.setFont(font)
        self.decodeButton.setIconSize(QtCore.QSize(20, 20))
        self.decodeButton.setFlat(False)
        self.decodeButton.setObjectName("decodeButton")
        self.gridLayout.addWidget(self.decodeButton, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.toolBar = QtWidgets.QToolBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.toolBar.setFont(font)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(30, 20))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.toolBar.setObjectName("toolBar")

        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setToolTipsVisible(False)
        self.menuFile.setObjectName("menuFile")

        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        MainWindow.setMenuBar(self.menubar)

        self.action_Open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Open.setFont(font)
        self.action_Open.setObjectName("action_Open")
        
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/cross-script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Quit.setFont(font)
        self.action_Quit.setObjectName("action_Quit")
        
        self.action_Cut = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/scissors-blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Cut.setIcon(icon8)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Cut.setFont(font)
        self.action_Cut.setObjectName("action_Cut")

        self.action_Copy = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/document-copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Copy.setIcon(icon9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Copy.setFont(font)
        self.action_Copy.setObjectName("action_Copy")

        self.action_Paste = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/clipboard-paste-document-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Paste.setIcon(icon10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Paste.setFont(font)
        self.action_Paste.setObjectName("action_Paste")

        self.action_Clear = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/bin-metal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Clear.setIcon(icon11)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Clear.setFont(font)
        self.action_Clear.setObjectName("action_Clear")

        self.action_Information = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Information.setIcon(icon14)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.action_Information.setFont(font)
        self.action_Information.setObjectName("action_Information")

        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Cut)
        self.toolBar.addAction(self.action_Copy)
        self.toolBar.addAction(self.action_Paste)
        self.toolBar.addAction(self.action_Information)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Quit)
        self.menuEdit.addAction(self.action_Cut)
        self.menuEdit.addAction(self.action_Copy)
        self.menuEdit.addAction(self.action_Paste)
        self.menuEdit.addAction(self.action_Clear)
        self.menuEdit.addSeparator()
        self.menuAbout.addAction(self.action_Information)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.codeBox, self.inputTextEdit)
        MainWindow.setTabOrder(self.inputTextEdit, self.decodeButton)
        MainWindow.setTabOrder(self.decodeButton, self.inputclearButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.codeBox.setItemText(0, _translate("MainWindow", "TTAA"))
        self.codeBox.setItemText(1, _translate("MainWindow", "TTBB"))
        self.codeBox.setItemText(2, _translate("MainWindow", "TTCC"))
        self.codeBox.setItemText(3, _translate("MainWindow", "TTDD"))
        self.inputclearButton.setText(_translate("MainWindow", "CLEAR"))
        self.decodeButton.setText(_translate("MainWindow", "DECODE"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_Open.setText(_translate("MainWindow", "&Open..."))
        self.action_Open.setToolTip(_translate("MainWindow", "Open a .txt file."))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Quit.setText(_translate("MainWindow", "Quit..."))
        self.action_Quit.setToolTip(_translate("MainWindow", "Quit application."))
        self.action_Quit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_Cut.setText(_translate("MainWindow", "Cut"))
        self.action_Cut.setToolTip(_translate("MainWindow", "Cut selected text."))
        self.action_Cut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_Copy.setText(_translate("MainWindow", "Copy"))
        self.action_Copy.setToolTip(_translate("MainWindow", "Copy selected text."))
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow", "Paste"))
        self.action_Paste.setToolTip(_translate("MainWindow", "Paste clipboard info."))
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_Clear.setText(_translate("MainWindow", "Clear"))
        self.action_Clear.setToolTip(_translate("MainWindow", "Clear all fields."))
        self.action_Information.setText(_translate("MainWindow", "Information"))
        self.action_Information.setToolTip(_translate("MainWindow", "About TEMPCodeur."))
import resource


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
