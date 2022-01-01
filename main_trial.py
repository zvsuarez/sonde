from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMainWindow
from PyQt5.QtWinExtras import QtWin
import PyQt5.QtCore as ptcore
from PyQt5.uic import loadUi
from main_ui import Ui_MainWindow
from result import Ui_Dialog
from cryptography.fernet import Fernet
import os
import datetime
import resource
import parameters

# Window Dialogs
class QuitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/quit_menu.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        self.buttonBox.accepted.connect(lambda: app.quit())
        file.close()

class ClearDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/clear_menu.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class InfoDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/information_menu.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('Information')
        self.setWindowFlag(ptcore.Qt.WindowContextHelpButtonHint, False)
        self.setFixedSize(570, 495)
        file.close()

class UnsupportedDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/unsupported_error.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(480, 140)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class TextFilledDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/textfilled_error.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(440, 140)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class FormatDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/format_error.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class CodeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/code_error.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setFixedSize(380, 130)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class ExpireDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/expired_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WARNING!')
        self.setFixedSize(560, 450)
        self.setWindowFlag(ptcore.Qt.WindowContextHelpButtonHint, False)
        file.close()

class IntroDialog0(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex0_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class IntroDialog1(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex1_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class IntroDialog2(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex2_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class IntroDialog3(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex3_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class IntroDialog4(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex4_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

class IntroDialog5(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        file = ptcore.QFile(':/ui/ui/introex5_window.ui')
        file.open(ptcore.QFile.ReadOnly)
        loadUi(file, self)
        self.setWindowTitle('WELCOME!')
        self.setFixedSize(490, 180)
        self.setWindowFlag(ptcore.Qt.FramelessWindowHint)
        file.close()

# Temp code integration
# {
#   obscured
# }

# Pressure code integration
# {
#   obscured
# }

# Cryptography class
# {
#   obscured
# }

class Expiration:
    def __init__(self):
        self.expiredialog = ExpireDialog()
        self.introdialog0 = IntroDialog0()
        self.introdialog1 = IntroDialog1()
        self.introdialog2 = IntroDialog2()
        self.introdialog3 = IntroDialog3()
        self.introdialog4 = IntroDialog4()
        self.introdialog5 = IntroDialog5()

    def trial(self):
        #obscured variable
        #target_dir = #directory
        #trial_txt = #hardcoded_file
        today = datetime.date.today()
        try:
            if not os.path.isdir(target_dir):
                os.mkdir(target_dir)
                if not os.path.isfile(target_dir+trial_txt):
                    with open(target_dir+trial_txt, 'a') as f:
                        f.write(str(today))
                    #Crypto.gen_dir(Crypto())
                    with open(target_dir+trial_txt, 'r') as g:
                        data = g.read()
                    return data
            if os.path.isdir(target_dir):
                if not os.path.isfile(target_dir+trial_txt):
                    with open(target_dir+trial_txt, 'a') as f:
                        f.write(str(today))
                    #Crypto.gen_dir(Crypto())
                    with open(target_dir+trial_txt, 'r') as g:
                        data = g.read()
                    return data
                if os.path.isfile(target_dir+trial_txt):
                    #Crypto.decrypt(Crypto())
                    with open(target_dir+trial_txt, 'r') as f:
                        data = f.read()
                    return data
        except:
            pass

    def expiration(self):
        date_recorded = self.trial()
        date_expiry = datetime.date.fromisoformat(date_recorded) + datetime.timedelta(days=5)
        today = datetime.date.today()
        interval = str(date_expiry - today)[0]
        if date_expiry >= today:
            if int(interval) == 0:
                self.introdialog0.exec_()
            if int(interval) == 1:
                self.introdialog1.exec_()
            if int(interval) == 2:
                self.introdialog2.exec_()
            if int(interval) == 3:
                self.introdialog3.exec_()
            if int(interval) == 4:
                self.introdialog4.exec_()
            if int(interval) == 5:
                self.introdialog5.exec_()
            #Crypto.encrypt(Crypto())
        else:
            self.expiredialog.exec_()
            #Crypto.encrypt(Crypto())
            return True

myappid = 'com.sonde.app'
QtWin.setCurrentProcessExplicitAppUserModelID(myappid)

# Main window
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Sonde v.1a')
        self.resize(1024, 728)
        self.connect_signals()
        self.detect_text()
        QApplication.clipboard().dataChanged.connect(self.clipboard)
        self.inputTextEdit.selectionChanged.connect(self.detect_selection)
        self.detect_clipboard()
        self.check_expiration()

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

    def code_dialog(self):
        dialog = CodeDialog(self)
        dialog.exec_()

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
                    self.unsupported_dialog()
            if len(text) >= 1:
                self.textfilled_dialog()
            else:
                pass
        else:
            pass

    def open_decode_result(self, data, *args):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window, data, *args)
        self.window.show()

# Clean string input
    def clean_string(self, string):
        strip = string.strip('\n')
        clean = ' '.join(strip.split())
        return clean

# Decode function
    def decode(self):
        code = ['TTAA', 'TTBB', 'TTCC', 'TTDD', 'PPAA', 'PPBB', 'PPCC', 'PPDD']
        input_decode = self.inputTextEdit.toPlainText()
        clean_str = self.clean_string(input_decode)
        if not(input_decode[:12].isnumeric()) and input_decode[0] != '/':
            self.format_dialog()
        if input_decode[:12].isnumeric() or input_decode[0] == '/':
            if clean_str.split()[1] not in code:
                self.code_dialog()
            else:
                if clean_str.split()[1] == self.codeBox.currentText():
                    if clean_str.split()[1][:2] == 'TT':
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
                    if clean_str.split()[1][:2] == 'PP':
                        if clean_str.split()[1] == 'PPAA':
                            data = Prescode(clean_str)
                            data.PPAC_main()
                            data.tab_AA()
                            try:
                                dataset = data.setDataAC()
                                self.open_decode_result(dataset, data.setArgsAC_row(), data.setArgsAC_col())
                                data.clear_AC()
                            except IndexError:
                                dataset = data.setDataInvalid()
                                self.open_decode_result(dataset, 1, 1)
                        if clean_str.split()[1] == 'PPBB':
                            data = Prescode(clean_str)
                            data.PPBD_main()
                            data.tab_BD()
                            try:
                                dataset = data.setDataBD()
                                self.open_decode_result(dataset, data.setArgsBD_row(), data.setArgsBD_col())
                                data.clear_BD()
                            except IndexError:
                                dataset = data.setDataInvalid()
                                self.open_decode_result(dataset, 1, 1)
                        if clean_str.split()[1] == 'PPCC':
                            data = Prescode(clean_str)
                            data.PPAC_main()
                            data.tab_CC()
                            try:
                                dataset = data.setDataAC()
                                self.open_decode_result(dataset, data.setArgsAC_row(), data.setArgsAC_col())
                                data.clear_AC()
                            except IndexError:
                                dataset = data.setDataInvalid()
                                self.open_decode_result(dataset, 1, 1)
                        if clean_str.split()[1] == 'PPDD':
                            data = Prescode(clean_str)
                            data.PPBD_main()
                            data.tab_BD()
                            try:
                                dataset = data.setDataBD()
                                self.open_decode_result(dataset, data.setArgsBD_row(), data.setArgsBD_col())
                                data.clear_BD()
                            except IndexError:
                                dataset = data.setDataInvalid()
                                self.open_decode_result(dataset, 1, 1)
                else:
                    self.code_dialog()
        else:
            pass

    def check_expiration(self):
        if Expiration.expiration(Expiration()) == True:
            self.action_Open.setEnabled(False)
            self.action_Clear.setEnabled(False)
            self.action_Cut.setEnabled(False)
            self.action_Copy.setEnabled(False)
            self.action_Paste.setEnabled(False)
            self.action_Information.setEnabled(False)
            self.decodeButton.setEnabled(False)
            self.inputclearButton.setEnabled(False)
            self.codeBox.setEnabled(False)
            self.inputTextEdit.setEnabled(False)
        else:
            pass


app = QApplication([])
app.setStyle('Fusion')
app.setStyleSheet("""
QPushButton#decodeButton:hover {
    background-color: #007500; 
    color: white;
} 
QPushButton#inputclearButton:hover { 
    background-color: #a80000; 
    color: white;
}
""")
window = MainWindow()
verification = Expiration()
window.show()
verification.expiration()
app.exec_()