from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QColorDialog, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6 import QtCore
from PySide6 import QtGui
import sys


class FontInfo(QtCore.QObject):
    font_signal = QtCore.Signal(str, str, str)

    def __init__(self):
        super(FontInfo, self).__init__()

    def run(self, font_family, font_size, font_color):
        self.font_signal.emit(font_family, font_size, font_color)


class FontUI(QWidget):
    def __init__(self, FontInfo: FontInfo):
        super(FontUI, self).__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.__init_ui()
        self.font_info = FontInfo
        self.font_color = "black"

    def __get_font_familaies(self):
        font_database = QtGui.QFontDatabase()
        font_families = font_database.families()
        return font_families

    def __get_font_size(self):
        font_database = QtGui.QFontDatabase()
        font_sizes = font_database.standardSizes()
        font_sizes_str = [str(i) for i in font_sizes]
        return font_sizes_str

    def __select_color(self):
        win_color = QColorDialog()
        color = win_color.getColor()
        if color.isValid():
            self.font_color = color.name()
            self.font_color_button.setStyleSheet("QPushButton#font_color_button{background-color:%s;}" %(color.name(),))

    def __init_ui(self):
        # 字体
        self.family_hlayout = QHBoxLayout()
        self.font_familay_label = QLabel()
        self.font_familay_label.setText("字体：")
        self.font_familay_combox = QComboBox()
        self.font_familay_combox.addItems(self.__get_font_familaies())
        self.family_hlayout.addWidget(self.font_familay_label)
        self.family_hlayout.addWidget(self.font_familay_combox)
        # 字体大小
        self.size_hlayout = QHBoxLayout()
        self.font_size_label = QLabel()
        self.font_size_label.setText("字体大小：")
        self.font_size_combox = QComboBox()
        self.font_size_combox.addItems(self.__get_font_size())
        self.font_size_combox.setCurrentText("16")
        self.size_hlayout.addWidget(self.font_size_label)
        self.size_hlayout.addWidget(self.font_size_combox)
        # 字体颜色
        self.color_hlayout = QHBoxLayout()
        self.font_color_label = QLabel()
        self.font_color_label.setText("字体颜色：")
        self.font_color_button = QPushButton()
        self.font_color_button.setObjectName("font_color_button")
        self.font_color_button.setStyleSheet("QPushButton#font_color_button{background-color:#000000;}")
        self.font_color_button.clicked.connect(self.__select_color)
        self.color_hlayout.addWidget(self.font_color_label)
        self.color_hlayout.addWidget(self.font_color_button)
        # 确认
        self.ok_button = QPushButton()
        self.ok_button.setText("确认")
        self.ok_button.clicked.connect(lambda:self.font_info.run(self.font_familay_combox.currentText(), self.font_size_combox.currentText(), self.font_color))
        # 布局
        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(self.family_hlayout)
        self.vlayout.addLayout(self.size_hlayout)
        self.vlayout.addLayout(self.color_hlayout)
        self.vlayout.addWidget(self.ok_button)
        self.setLayout(self.vlayout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = FontUI()
    windows.show()
    sys.exit(app.exec())