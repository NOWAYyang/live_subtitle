import sys
import threading
from PyQt5 import QtWidgets, QtCore

class SubtitleGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Live Subtitle')
        self.setGeometry(100, 100, 800, 200)
        self.layout = QtWidgets.QVBoxLayout()
        self.subtitle_label = QtWidgets.QLabel('...')
        self.subtitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_label.setStyleSheet('font-size: 32px; color: white; background: black;')
        self.layout.addWidget(self.subtitle_label)
        self.setLayout(self.layout)

    def update_subtitle(self, text):
        self.subtitle_label.setText(text)

# 示例用法：
# app = QtWidgets.QApplication(sys.argv)
# gui = SubtitleGUI()
# gui.show()
# gui.update_subtitle('Hello world!')
# sys.exit(app.exec_())
