from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from ui_config import Ui_MainWindow     # MAIN_UI
from decode_window import Ui_Dialog     # DECODE_RESULT_UI
import os
import datetime
# Resource qrc
import resource                         # ICON_RESOURCE
# Decode backend
import temp_class                       # DECODE_BACKEND

# Quit dialog
class QuitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/quit_menu.ui', self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.buttonBox.accepted.connect(lambda: app.quit())

# Clear dialog
class ClearDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/clear_menu.ui', self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(Qt.FramelessWindowHint)

# Information dialog
class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/information_menu.ui', self)
        self.setWindowTitle('Information')
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(570, 500)
        #self.setWindowIcon()

# Unsupported dialog
class UnsupportedDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/unsupported_error.ui', self)
        self.setFixedSize(500, 160)
        self.setWindowFlag(Qt.FramelessWindowHint)

# Text filled dialog
class TextFilledDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/textfilled_error.ui', self)
        self.setFixedSize(440, 140)
        self.setWindowFlag(Qt.FramelessWindowHint)

# Format error dialog
class FormatDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/format_error.ui', self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(Qt.FramelessWindowHint)

class TempcodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/tempcode_error.ui', self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(Qt.FramelessWindowHint)

class ExpireDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/expired_window.ui', self)
        self.setWindowTitle('WARNING!')
        self.setFixedSize(400, 320)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

class IntroDialog1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/introex1_window.ui', self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(Qt.FramelessWindowHint)

class IntroDialog2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/introex2_window.ui', self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(Qt.FramelessWindowHint)

class IntroDialog3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/introex3_window.ui', self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(Qt.FramelessWindowHint)

class IntroDialog4(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/introex4_window.ui', self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(Qt.FramelessWindowHint)

class IntroDialog5(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/introex5_window.ui', self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(Qt.FramelessWindowHint)


# Temp code integration class
# {
#       OBSCURED CLASS
# }

with open('styles.qss', 'r') as f:
    styles = f.read()

# Main window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('TEMPCodeur')
        #self.setWindowIcon(QIcon('ui/icons/32x32.png'))
        self.resize(1024, 728)
        self.connect_signals()
        self.detect_text()
        QApplication.clipboard().dataChanged.connect(self.clipboard)
        self.inputTextEdit.selectionChanged.connect(self.detect_selection)
        self.detect_clipboard()
        self.expiration()

    def connect_signals(self):
        self.action_Open.triggered.connect(self.open_dialog)
        self.action_Clear.triggered.connect(self.clear_dialog)
        self.action_Information.triggered.connect(self.info_dialog)
        self.action_Quit.triggered.connect(self.quit_dialog)
        self.inputclearButton.clicked.connect(self.clear_dialog)
        self.inputTextEdit.textChanged.connect(self.detect_text)
        self.decodeButton.clicked.connect(self.decode)
        self.action_Paste.triggered.connect(self.Paste)
        self.action_Cut.triggered.connect(self.Cut)
        self.action_Copy.triggered.connect(self.Copy)

    def detect_text(self):
        text = self.inputTextEdit.toPlainText()
        if len(text) == 0:
            self.inputclearButton.setEnabled(False)
            self.action_Clear.setEnabled(False)
            self.decodeButton.setEnabled(False)
            self.action_Cut.setEnabled(False)
            self.action_Copy.setEnabled(False)
        if len(text) >= 1:
            self.inputclearButton.setEnabled(True)
            self.action_Clear.setEnabled(True)
            self.decodeButton.setEnabled(True)
            self.action_Cut.setEnabled(True)
            self.action_Copy.setEnabled(True)

    def clipboard(self):
        clip_text = QApplication.clipboard().text()
        return clip_text

    def detect_clipboard(self):
        clip_text = self.clipboard()
        if len(clip_text) < 1:
            self.action_Paste.setEnabled(False)
        if len(clip_text) > 1:
            self.action_Paste.setEnabled(True)
    
    def detect_selection(self):
        cursor = self.inputTextEdit.textCursor()
        return cursor

    def Paste(self):
        clip_text = self.clipboard()
        self.inputTextEdit.insertPlainText(clip_text)

    def Cut(self):
        cursor_cut = self.detect_selection()
        cursor_text = cursor_cut.selectedText()
        QApplication.clipboard().setText(str(cursor_text))
        text_replace = str(cursor_text).replace(str(cursor_text),'')
        self.inputTextEdit.insertPlainText(text_replace)

    def Copy(self):
        cursor_copy = self.detect_selection()
        cursor_text = cursor_copy.selectedText()
        QApplication.clipboard().setText(str(cursor_text))

    def clear_dialog(self):
        dialog = ClearDialog(self)
        dialog.buttonBox.accepted.connect(self.clear_dialog_clear)
        dialog.exec_()

    def clear_dialog_clear(self):
        self.inputTextEdit.clear()
    
    def info_dialog(self):
        dialog = InfoDialog(self)
        dialog.exec_()

    def quit_dialog(self):
        dialog = QuitDialog(self)
        dialog.exec_()

    def unsupported_dialog(self):
        dialog = UnsupportedDialog(self)
        dialog.exec_()
    
    def textfilled_dialog(self):
        dialog = TextFilledDialog(self)
        dialog.exec_()

    def format_dialog(self):
        dialog = FormatDialog(self)
        dialog.exec_()

    def tempcode_dialog(self):
        dialog = TempcodeDialog(self)
        dialog.exec_()
    
    def expired_dialog(self):
        dialog = ExpireDialog(self)
        dialog.exec_()

    def intro_dialog1(self):
        dialog = IntroDialog1(self)
        dialog.exec_()

    def intro_dialog2(self):
        dialog = IntroDialog2(self)
        dialog.exec_()

    def intro_dialog3(self):
        dialog = IntroDialog3(self)
        dialog.exec_()

    def intro_dialog4(self):
        dialog = IntroDialog4(self)
        dialog.exec_()
    
    def intro_dialog5(self):
        dialog = IntroDialog5(self)
        dialog.exec_()

    # {
    #   OBSCURED FUNCTIONS
    # }

    def open_dialog(self):
        dialog = QFileDialog()
        dialog_exec = dialog.getOpenFileName(self, 'Open Text File...', os.getcwd(), "Text Files (*.txt)")
        if dialog_exec[0].endswith('.txt'):
            text = self.inputTextEdit.toPlainText()
            if len(text) == 0:
                try:
                    with open(dialog_exec[0], 'r') as f:
                        data = f.read()
                        self.inputTextEdit.setPlainText(data)
                except UnicodeDecodeError: 
                    self.unsupported_dialog()   # dialog error showing codec charmap
            if len(text) >= 1:
                self.textfilled_dialog()    # dialog showing existing chars
            else:
                pass
        else:
            pass

    def open_decode_result(self, data, *args):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, data, *args)
        self.window.show()

# Clean string
    def clean_string(self, string):
        strip = string.strip('\n')
        clean = ' '.join(strip.split())
        return clean

# Decode function
    def decode(self):
        temp_code = ['TTAA', 'TTBB', 'TTCC', 'TTDD']
        input_decode = self.inputTextEdit.toPlainText()
        clean_str = self.clean_string(input_decode)
        if not(input_decode[:12].isnumeric()) and input_decode[0] != '/':
            self.format_dialog()
        if input_decode[:12].isnumeric() or input_decode[0] == '/':
            if clean_str.split()[1] not in temp_code:
                self.tempcode_dialog()
            else:
                if clean_str.split()[1] == self.codeBox.currentText():
                    if clean_str.split()[1] == 'TTAA':
                        data = Tempcode(clean_str)
                        data.TTAC_main()
                        data.tab_AA()
                        try:
                            dataset = data.setDataAC()
                            self.open_decode_result(dataset, data.setArgsAC_row(), data.setArgsAC_col())
                            data.clear_AC()
                        except IndexError:
                            dataset = data.setDataInvalid()
                            self.open_decode_result(dataset, 1, 1)
                        #print(dataset)
                    if clean_str.split()[1] == 'TTBB':
                        data = Tempcode(clean_str)
                        data.TTBB_main()
                        data.tab_BB()
                        try:
                            dataset = data.setDataBB()
                            self.open_decode_result(dataset, data.setArgsBB_row(), data.setArgsBB_col())
                            data.clear_BB()
                        except IndexError:
                            dataset = data.setDataInvalid()
                            self.open_decode_result(dataset, 1, 1)
                    if clean_str.split()[1] == 'TTCC':
                        data = Tempcode(clean_str)
                        data.TTAC_main()
                        data.tab_CC()
                        try:
                            dataset = data.setDataAC()
                            self.open_decode_result(dataset, data.setArgsAC_row(), data.setArgsAC_col())
                            data.clear_AC()
                        except IndexError:
                            dataset = data.setDataInvalid()
                            self.open_decode_result(dataset, 1, 1)
                    if clean_str.split()[1] == 'TTDD':
                        data = Tempcode(clean_str)
                        data.TTDD_main()
                        data.tab_DD()
                        try:
                            dataset = data.setDataDD()
                            self.open_decode_result(dataset, data.setArgsDD_row(), data.setArgsDD_col())
                            data.clear_DD()
                        except IndexError:
                            dataset = data.setDataInvalid()
                            self.open_decode_result(dataset, 1, 1)
                    else:
                        pass
                else:
                    self.tempcode_dialog()
        else:
            pass
            #return print(clean_str.split()[1])

app = QApplication([])
app.setStyle('Fusion')
app.setStyleSheet(styles)
window = MainWindow()
window.show()
app.exec_()