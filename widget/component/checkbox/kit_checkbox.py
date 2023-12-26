import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFontDatabase, QPainter, QPixmap
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout, QWidget, QApplication, QStyleOptionButton, QStyle

from config import config
from app_config.constant import Icons

from ..icon import KitIcon


class CheckBoxIcon(QWidget):

    UnChecked = 0
    Checked = 1
    PartialChecked = 2

    def __init__(self, check_state: int = 1, parent=None):
        super(CheckBoxIcon, self).__init__(parent=parent)

        self.icon = KitIcon(parent=self)
        self.icon.setFixedSize(20, 20)
        self.setFixedSize(self.sizeHint())
        self.icon_check_state = check_state
        self.setCheckState(self.icon_check_state)

        self.__init_widget()
        self.__init_qss()
        self.__init_slot()

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.layout.addWidget(self.icon, alignment=Qt.AlignHCenter)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setCheckState(self, check_state: int):
        if check_state == CheckBoxIcon.Checked:
            self.setProperty('state', 'checked')
            self.icon.setIcon(Icons.md_check)
        elif check_state == CheckBoxIcon.UnChecked:
            self.setProperty('state', 'unchecked')
            self.icon.setIcon("")
        elif check_state == CheckBoxIcon.PartialChecked:
            self.setProperty('state', 'partial_checked')
            self.icon.setIcon(Icons.md_horizontal_rule)
        self.style().polish(self)

    def sizeHint(self):
        return QSize(40, 40)


class KitCheckBox(QCheckBox):
    def __init__(self, text=None, parent=None):
        super(KitCheckBox, self).__init__(text, parent)

        self.checked_icon = CheckBoxIcon(CheckBoxIcon.Checked)
        self.unchecked_icon = CheckBoxIcon(CheckBoxIcon.UnChecked)
        self.partial_checked_icon = CheckBoxIcon(CheckBoxIcon.PartialChecked)

    def sizeHint(self):
        return QSize(40, 40)

    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)

        # get the rect of indicator
        opt = QStyleOptionButton()
        opt.initFrom(self)
        rect = self.style().subElementRect(QStyle.SE_CheckBoxIndicator, opt, self)
        opt.rect = rect

        # draw indicator
        state_icon = None
        if self.checkState() == Qt.CheckState.Checked:
            state_icon = self.checked_icon
            opt.state = QStyle.State_On
        elif self.checkState() == Qt.CheckState.PartiallyChecked:
            state_icon = self.partial_checked_icon
            opt.state = QStyle.State_NoChange
        elif self.checkState() == Qt.CheckState.Unchecked:
            opt.state = QStyle.State_Off
            state_icon = self.unchecked_icon
        painter.drawPixmap(rect, QPixmap.fromImage(state_icon.grab().toImage()))


