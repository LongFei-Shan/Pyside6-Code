from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QToolBar, QStatusBar, QTextEdit, QPlainTextEdit, QLabel, QPushButton
from PySide6 import QtCore
from PySide6 import QtGui
import sys


class MainUI(QMainWindow):
	def __init__(self):
		super(MainUI, self).__init__()
		self.resize(900, 650)
		self.setObjectName("main_ui")
		self.setStyleSheet("QMainWindow#main_ui{background-color:#ffffff;}")
		# 初始化
		self.__init_centralWidget()
		self.__init_toolBar()
		self.__init_statusBar()
		self.__init_side_bar()

	def __init_centralWidget(self):
		# add edittext
		self.plain_text_edit = QPlainTextEdit()
		self.setCentralWidget(self.plain_text_edit)
		self.plain_text_edit.setObjectName("plain_text_edit")
		self.setStyleSheet("QPlainTextEdit#plain_text_edit{border-width:2px; border-style: solid; border-color: #696969; margin:5px 5px 1px 5px;"
						   "color:black;}")

	def __init_side_bar(self):
		# 添加侧边栏
		self.side_bar = QToolBar()
		self.side_bar_area = QtCore.Qt.ToolBarArea.RightToolBarArea
		self.side_bar.setMovable(False)
		self.addToolBar(self.side_bar_area, self.side_bar)
		self.side_bar.setFixedWidth(35)
		# 添加功能
		self.font_action = QtGui.QAction(QtGui.QPixmap(r"C:\Users\31843\Documents\文件\图标\font.png"), "Font")
		self.side_bar.addAction(self.font_action)

	def __init_toolBar(self):
		# add toolbar
		self.toolBarArea = QtCore.Qt.ToolBarArea(QtCore.Qt.ToolBarArea.TopToolBarArea)
		self.toolbar = QToolBar()
		self.addToolBar(self.toolBarArea, self.toolbar)
		self.toolbar.setMovable(False)
		self.back_action = QtGui.QAction(QtGui.QPixmap(r"C:\Users\31843\Documents\文件\图标\arrow-180.png"), "Back")
		self.forward_action = QtGui.QAction(QtGui.QPixmap(r"C:\Users\31843\Documents\文件\图标\arrow-000.png"), "Forward")
		self.save_action = QtGui.QAction(QtGui.QPixmap(r"C:\Users\31843\Documents\文件\图标\disk--arrow.png"), "Save As")
		self.open_action = QtGui.QAction(QtGui.QPixmap(r"C:\Users\31843\Documents\文件\图标\folder_open_doc.png"), "Open")
		self.toolbar.addAction(self.back_action)
		self.toolbar.addAction(self.forward_action)
		self.toolbar.addAction(self.save_action)
		self.toolbar.addAction(self.open_action)
		# change toolbar color
		self.toolbar.setObjectName("tool_bar")
		self.toolbar.setStyleSheet("QToolBar#tool_bar{background-color:#f0f0f0}")

	def __init_statusBar(self):
		# add statusbar
		self.status_bar = QStatusBar()
		self.status_bar.setObjectName("status_bar")
		self.setStatusBar(self.status_bar)
		self.status_bar.showMessage("开始运行", 1000)
		self.status_bar.setStyleSheet("QStatusBar#status_bar{background-color:#f0f0f0; border-top:1px solid ##e5e5e5;}")
		# add show column number label
		self.column_number_label = QLabel()
		self.column_number_label.setText("0:0")
		self.status_bar.addPermanentWidget(self.column_number_label)
		# add show character number label
		self.character_number_label = QLabel()
		self.character_number_label.setText("0字符")
		self.status_bar.addPermanentWidget(self.character_number_label)
		# change encoding button
		self.encoding_button = QPushButton()
		self.encoding_button.setText("utf-8")
		self.status_bar.addPermanentWidget(self.encoding_button)
		self.encoding_button.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
		self.encoding_button.setObjectName("encoding_button")
		self.encoding_button.setStyleSheet("QPushButton#encoding_button{background-color:#f0f0f0; border:none;}")

		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	windows = MainUI()
	windows.show()
	sys.exit(app.exec())