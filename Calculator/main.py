# This Python file uses the following encoding: utf-8
import sys
import MainUI
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QRegularExpression, Qt
from PySide6.QtGui import QValidator, QRegularExpressionValidator
import math


class Main(MainUI.MainUi):
    def __init__(self):
        super(Main, self).__init__()
        self.__operator_button_connect()
        self.__line_edit_check()

    def __operator_button_connect(self):
        for i in range(len(self.operator_button)):
            for j in range(len(self.operator_button[0])):
                if self.operator_button[i][j].text() == "clear":
                    self.operator_button[i][j].clicked.connect(self.__clear_button_connect)
                elif self.operator_button[i][j].text() == "back":
                    self.operator_button[i][j].clicked.connect(self.__back_button_connect)
                elif self.operator_button[i][j].text() in ["^", "ln", "sqrt"]:
                    self.operator_button[i][j].clicked.connect(self.__power_button_connect)
                elif self.operator_button[i][j].text() == "=":
                    self.operator_button[i][j].clicked.connect(self.__calcuate_button_connect)
                else:
                    self.operator_button[i][j].clicked.connect(self.__line_edit_show)

    # 正则表达式，仅为数字以及字母，小数点，左右括号，加减乘除，幂，百分号，开方，自然对数
    def __line_edit_check(self):
        self.result_show.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9a-zA-Z\.\(\)\+\-\*\/\^\%]*")))

    def __calcuate_button_connect(self):
        # 获取当前显示
        current_text = self.result_show.text()
        # 替换
        current_text = current_text.replace("^", "**")
        current_text = current_text.replace("ln", "math.log")
        current_text = current_text.replace("sqrt", "math.sqrt")
        current_text = current_text.replace("e", "math.e")
        # 计算
        try:
            result = eval(current_text)
        except:
            result = "Error"
        # 显示
        self.result_show.setText(str(result))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.__calcuate_button_connect()

    def __clear_button_connect(self):
        # 清空显示
        self.result_show.setText("")

    def __back_button_connect(self):
        # 获取当前显示
        current_text = self.result_show.text()
        # 删除最后一个字符，若"power", "ln", "sqrt"则删除多个字符
        if len(current_text) >= 3 and current_text[-3:] == "ln(":
            current_text = current_text[:-3]
        elif len(current_text) >= 5 and current_text[-5:] == "sqrt(":
            current_text = current_text[:-5]
        elif len(current_text) >= 6 and current_text[-6:] == "power(":
            current_text = current_text[:-6]
        elif len(current_text) == 0:
            pass
        else:
            current_text = current_text[:-1]
        self.result_show.setText(current_text)

    def __power_button_connect(self):
        # 获取当前显示
        current_text = self.result_show.text()
        # 拼接
        current_text += self.sender().text() + "("
        self.result_show.setText(current_text)

    def __line_edit_show(self):
        # 获取当前显示
        current_text = self.result_show.text()
        # 拼接
        current_text += self.sender().text()
        self.result_show.setText(current_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    # 设置样式
    file = open("main.css", "r")
    style_sheet = file.read()
    file.close()
    win.setStyleSheet(style_sheet)
    # 显示
    win.show()
    sys.exit(app.exec())
