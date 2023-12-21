import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QColor

class MaskedDialog(QDialog):
    def __init__(self):
        super().__init__()

        # 创建一个半透明的背景遮罩
        self.mask = QLabel(self)
        self.mask.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.mask.setGeometry(0, 0, 800, 600)  # 设置遮罩大小与窗口大小一致
        self.mask.hide()  # 初始时隐藏遮罩

        # 创建弹窗内容
        layout = QVBoxLayout()
        self.setLayout(layout)
        btn = QPushButton("关闭弹窗")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)

    def showEvent(self, event):
        super().showEvent(event)
        self.mask.show()  # 当弹窗显示时显示遮罩

    def closeEvent(self, event):
        super().closeEvent(event)
        self.mask.hide()  # 当弹窗关闭时隐藏遮罩

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MaskedDialog()
    dialog.show()
    sys.exit(app.exec_())