from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIntValidator
from PyQt5.QtWidgets import QLineEdit, QApplication, QWidget, QVBoxLayout

from config import config
from ..icon import KitIcon
from app_config.constant import Icons


class KitLineEdit(QLineEdit):

    def __init__(self, parent=None):
        super(KitLineEdit, self).__init__(parent=parent)

        self.validator_icon = KitIcon(parent=self)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setTextMargins(4, 0, 24, 0)

    def __init_slot(self):
        self.textChanged.connect(self.__fresh_validator_icon)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def __fresh_validator_icon(self):
        self.validator_icon.move(self.width() - 24, (self.height() - self.validator_icon.height()) // 2)
        if self.text() == "" or not self.validator():
            self.validator_icon.setVisible(False)
            return

        self.validator_icon.setVisible(True)
        if self.hasAcceptableInput():
            self.validator_icon.setProperty('type', 'success')
            self.validator_icon.setIcon(Icons.check_circle)
        else:
            self.validator_icon.setProperty('type', 'danger')
            self.validator_icon.setIcon(Icons.info)
        self.validator_icon.style().polish(self.validator_icon)

    def sizeHint(self):
        return QSize(100, 40)

    def paintEvent(self, event) -> None:
        super().paintEvent(event)
        self.__fresh_validator_icon()

    def valid(self):
        """
        判断输入是否有效
        :return:
        """
        return self.hasAcceptableInput()


if __name__ == '__main__':
    app = QApplication([])
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]
    main = QWidget()
    main.resize(800, 600)
    layout = QVBoxLayout()
    line1 = KitLineEdit()
    validator = QIntValidator(1, 10)
    line1.setValidator(validator)
    line1.setToolTip("请输入1-10的数字")
    main.setLayout(layout)
    layout.addWidget(line1)
    main.show()
    app.exec_()
