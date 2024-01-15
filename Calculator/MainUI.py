# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QVBoxLayout


class MainUi(QWidget):
    def __init__(self):
        super(MainUi,self).__init__()
        self.__init_ui()

    def __init_ui(self):
        # 运算符
        operator = [
                ["clear", "back", "^", "%", "ln"],
                ["7", "8", "9", "+", "sqrt"],
                ["4", "5", "6", "-", "("],
                ["1", "2", "3", "*", ")"],
                ["e", "0", ".", "/", "="]
              ]
        self.operator_button = []
        for i in range(len(operator)):
            temp_button = []
            for j in range(len(operator[0])):
                temp_button.append(QPushButton(f"{operator[i][j]}"))
            self.operator_button.append(temp_button)
        # 显示
        self.result_show = QLineEdit()
        self.result_show.setObjectName("result_show")
        self.result_show.setReadOnly(False)
        self.result_show.setFixedHeight(50)
        # 布局
        self.grid_layout = QGridLayout()
        for i in range(5):
            for j in range(5):
                self.grid_layout.addWidget(self.operator_button[i][j], i, j)
        self.vlayout = QVBoxLayout()
        self.vlayout.addWidget(self.result_show)
        self.vlayout.addLayout(self.grid_layout)
        self.setLayout(self.vlayout)

