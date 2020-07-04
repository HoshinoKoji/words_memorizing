import os, sys
from PyQt5 import QtCore, QtGui
import PyQt5.QtWidgets as QtWidgets

from UI.mainwindow import Ui_MainWindow
from UI.manage_wordbooks import Ui_Dialog

import WordbookCore

RECORD_WORDBOOK = None
RECORD_WORDBOOK_LIST = []
record_dialog = None
record_dialog_ui = None

def replaceInvalidCharacters(string):
    new_string = string[:]
    for char in ('*', '?', '/', '\\'):
        new_string = new_string.replace(char, '_')
    return new_string

def RECORD_GET_WORDBOOKS():
    wordbook_list = []
    try:
        fileList = os.listdir('./.data')
        for filename in fileList:
            if filename[filename.rfind('.'):] == '.wordbook' and os.path.isfile(f'./.data/{filename}'):
                try:
                    wordbook_list.append(WordbookCore.GET_WORDBOOK_FROM_FILE(
                        f'./.data/{filename}'))
                except:
                    QtWidgets.QMessageBox.warning(
                        None, '错误', f'该数据文件或已损坏：\n{filename}', QtWidgets.QDialogButtonBox.Ok)
    except FileNotFoundError:
        os.mkdir('./.data/')

    record_dialog_ui.tableWidget.setRowCount(len(wordbook_list))
    for i in range(len(wordbook_list)):
        record_dialog_ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(wordbook_list[i].getName()))
        record_dialog_ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(len(wordbook_list[i].getWords()))))
        record_dialog_ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(wordbook_list[i].getTime()))
    return wordbook_list

def RECORD_CHOOSE_WORDBOOK():
    global RECORD_WORDBOOK, record_dialog, record_dialog_ui
    index = record_dialog_ui.tableWidget.currentRow()
    if index != -1:
        RECORD_WORDBOOK = RECORD_WORDBOOK_LIST[index]
        # print(RECORD_WORDBOOK)
        
        record_dialog.destroy()
        record_dialog = None
        record_dialog_ui = None

        MainUI.record_label_status.setText(f'当前状态：选中单词本\"{RECORD_WORDBOOK.getName()}\"')

def RECORD_CREATE_WORDBOOK():
    global RECORD_WORDBOOK_LIST
    name = QtWidgets.QInputDialog.getText(record_dialog, '输入', '输入单词本名称：')
    if name[1]:
        if name[0] not in [wordbook.getName() for wordbook in RECORD_WORDBOOK_LIST]:
            new_wordbook = WordbookCore.Wordbook(replaceInvalidCharacters(name[0]))
            new_wordbook.save()
            RECORD_WORDBOOK_LIST = RECORD_GET_WORDBOOKS()
        else:
            QtWidgets.QMessageBox.warning(None, '错误', f'以"{name[0]}"命名的单词本已存在！')

def RECORD_DELETE_WORDBOOK():
    global RECORD_WORDBOOK_LIST
    index = record_dialog_ui.tableWidget.currentRow()
    try:
        os.remove(f'./.data/{RECORD_WORDBOOK_LIST[index].getName()}.wordbook')
        RECORD_WORDBOOK_LIST = RECORD_GET_WORDBOOKS()
    except:
        pass

def RECORD_MANAGE_QUIT():
    global record_dialog, record_dialog_ui
    record_dialog.destroy()
    record_dialog = None
    record_dialog_ui = None

def RECORD_MANAGE_WORDBOOKS():
    global record_dialog, record_dialog_ui, RECORD_WORDBOOK, RECORD_WORDBOOK_LIST
    
    RECORD_WORDBOOK = None
    record_dialog = QtWidgets.QDialog(MainWindow)
    record_dialog_ui = Ui_Dialog()
    record_dialog_ui.setupUi(record_dialog)
    record_dialog_ui.button_choose.clicked.connect(RECORD_CHOOSE_WORDBOOK)
    record_dialog_ui.button_create.clicked.connect(RECORD_CREATE_WORDBOOK)
    record_dialog_ui.button_delete.clicked.connect(RECORD_DELETE_WORDBOOK)
    record_dialog_ui.button_quit.clicked.connect(RECORD_MANAGE_QUIT)
    record_dialog.show()
    
    RECORD_WORDBOOK_LIST = RECORD_GET_WORDBOOKS()

def RECORD_ADD_WORD():
    if RECORD_WORDBOOK:
        new_word = {
            'id': RECORD_WORDBOOK.currentID + 1,
            'spelling': MainUI.record_text_word.text(),
            'meaning': MainUI.record_text_meaning.toPlainText(),
            'example': MainUI.record_text_example.toPlainText()
        }
        RECORD_WORDBOOK.addWord(new_word)
        MainUI.record_text_word.setText('')
        MainUI.record_text_meaning.setPlainText('')
        MainUI.record_text_example.setPlainText('')
        MainUI.record_label_status.setText(f'当前状态：已添加单词\"{new_word["spelling"]}\"')
        MainUI.record_text_word.setFocus()
    else:
        QtWidgets.QMessageBox.warning(None, '错误', '未选择单词本！')

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    
    MainUI = Ui_MainWindow()
    MainUI.setupUi(MainWindow)

    # icon = QtGui.QIcon()
    # iconfile = GetPath(os.path.join("assets", "icon_128x128.ico"))

    # icon.addPixmap(QtGui.QPixmap(iconfile), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    # MainWindow.setWindowIcon(icon)
    
    MainUI.record_button_manage.clicked.connect(RECORD_MANAGE_WORDBOOKS)
    MainUI.record_button_record.clicked.connect(RECORD_ADD_WORD)
    
    MainWindow.show()
    sys.exit(app.exec())