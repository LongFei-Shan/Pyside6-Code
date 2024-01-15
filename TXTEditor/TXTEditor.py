from PySide6 import QtCore
from PySide6 import QtGui
from PySide6.QtWidgets import QFileDialog, QMessageBox
import sys
from TxTEditorUI import MainUI
from PySide6.QtWidgets import QApplication
from FontUI import FontInfo, FontUI


class TxTEditor(MainUI):
    def __init__(self):
        super().__init__()
        self.open_action.triggered.connect(self.__open_file)
        self.plain_text_edit.textChanged.connect(self.__count_character)
        self.save_action.triggered.connect(self.__save_as)
        self.plain_text_edit.cursorPositionChanged.connect(self.__get_plain_text_cursor_position)
        self.font_action.triggered.connect(self.__font_ui)
        # 信号
        self.font_info = FontInfo()
        self.font_info.font_signal.connect(self.__change_text_style)

    def closeEvent(self, event):
        info = QMessageBox.information(self, "提示", "是否退出？", QMessageBox.Yes | QMessageBox.No)
        if info == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

    def __font_ui(self):
        self.font_ui = FontUI(self.font_info)
        self.font_ui.show()

    def __get_plain_text_cursor_position(self):
        tc = self.plain_text_edit.textCursor()
        column_number = tc.positionInBlock()
        row_number = tc.blockNumber()
        self.column_number_label.setText(f"{row_number}:{column_number}")

    @QtCore.Slot(str, str, str)
    def __change_text_style(self, font_family, font_size, font_color):
        self.plain_text_edit.setStyleSheet("QPlainTextEdit#plain_text_edit{font-family:%s;font-size:%spx;color:%s;}"
                                           %(font_family, font_size, font_color))

    def __save_as(self):
        filePath, fileType = QFileDialog.getSaveFileName(self, "保存文件", "./", "All File (*);; TxT File(*.txt);; PY File(*.py)")
        if fileType == '' or filePath == '':
            pass
        else:
            plain_text = self.plain_text_edit.toPlainText()
            with open(filePath, 'w', encoding="utf-8") as fp:
                fp.write(plain_text)

    def __count_character(self):
        plain_text = self.plain_text_edit.toPlainText()
        plain_text = "".join(plain_text.split())
        character_number = len(plain_text)
        self.character_number_label.setText(f"{character_number}字符")

    def __open_file(self):
        file_path = QFileDialog.getOpenFileName(self, "选择文件", "./", "All File (*);; TxT File(*.txt);; PY File(*.py)")
        if file_path[0] == '' or file_path[1] == '':
            pass
        else:
            with open(file_path[0], "r", encoding="utf-8") as fp:
                file_content = fp.read()
            self.plain_text_edit.setPlainText(file_content)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	windows = TxTEditor()
	windows.show()
	sys.exit(app.exec())