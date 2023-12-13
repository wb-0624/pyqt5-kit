from typing import List

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QHBoxLayout, QRadioButton, QStackedWidget, QStyle, \
    QStyleOptionButton

from app_config.constant import Icons, Orientation
from ..button import KitButton
from ..icon import KitIcon


class KitTab(QRadioButton):

    def __init__(self, text: str, icon: Icons, orientation: Orientation = Orientation.Vertical, parent=None):
        super(KitTab, self).__init__(text=text, parent=parent)

        self._orientation = orientation
        self._checked = False
        self._tab_width_fit = False

        self.icon = KitIcon(icon, self)
        self.text = text

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setCheckable(True)
        self.setFixedHeight(32)

        self.indicator_widget = QWidget(self)
        self.indicator_widget.setObjectName('indicator')
        self.indicator_widget.setVisible(False)

    def __init_slot(self):
        self.toggled.connect(lambda checked: self.indicator_widget.setVisible(checked))

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setTabWidthFit(self, tab_width_fit: bool):
        """
        函数“setTabWidthFit”设置“_tab_width_fit”属性的值。
        @param tab_width_fit bool True 时，标签只保留内容长度。
        """
        self._tab_width_fit = tab_width_fit

    def setTabName(self, text: str):
        self.text = text
        self.setText(self.text)

    def getTabName(self):
        return self.text

    def paintEvent(self, a0) -> None:
        if self._tab_width_fit:
            self.adjustSize()
        super().paintEvent(a0)
        self.icon.move(4, (self.height() - self.icon.height()) // 2)
        if self._orientation == Orientation.Vertical:
            self.indicator_widget.resize(4, int(self.height() * 0.6))
            self.indicator_widget.move(0, (self.height() - self.indicator_widget.height()) // 2)
        elif self._orientation == Orientation.Horizontal:
            self.indicator_widget.resize(int(self.width() * 0.8), 4)
            self.indicator_widget.move((self.width() - self.indicator_widget.width()) // 2,
                                       self.height() - self.indicator_widget.height())


class KitTabBar(QWidget):
    currentIndexChanged = pyqtSignal(int)

    def __init__(self, orientation: Orientation = Orientation.Vertical, parent=None):
        super(KitTabBar, self).__init__(parent=parent)

        self._orientation = orientation
        self._currentIndex = -1
        self._stackedWidget = None
        self.tab_list: List[KitTab] = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QVBoxLayout() if self._orientation == Orientation.Vertical else QHBoxLayout()
        self.layout.setSpacing(4)
        self.setLayout(self.layout)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addTab(self, text: str = '', icon: Icons = ''):
        tab = KitTab(text, icon, self._orientation)
        tab.toggled.connect(lambda checked: self.setCurrentIndex(self.tab_list.index(tab)))
        self.tab_list.append(tab)
        self.layout.addWidget(tab)

    def setCurrentIndex(self, currentIndex: int):
        if self._currentIndex != currentIndex:
            self._currentIndex = currentIndex
            if isinstance(self._stackedWidget, QStackedWidget):
                self._stackedWidget.setCurrentIndex(self._currentIndex)

    def removeTab(self, text):
        remove_tab = None
        for tab in self.tab_list:
            if tab.getTabName() == text:
                remove_tab = tab
        if remove_tab is None:
            raise ValueError('no tab named' + text)
        self.tab_list.remove(remove_tab)
        self.layout.removeWidget(remove_tab)
        remove_tab.deleteLater()

    def setTabsWidthFit(self, tabs_width_fit: bool):
        for tab in self.tab_list:
            tab.setTabWidthFit(tabs_width_fit)

    def connectStackedWidget(self, stacked_widget: QStackedWidget):
        self._stackedWidget = stacked_widget


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)

    tab_bar = KitTabBar()
    tab_bar.addTab('Tab 1', Icons.home)
    tab_bar.addTab('Tab 2', Icons.home)
    tab_bar.addTab('Tab 312341235123', Icons.home)

    stacked = QStackedWidget()
    stacked.addWidget(KitButton('1'))
    stacked.addWidget(KitButton('2'))
    stacked.addWidget(KitButton('3'))

    tab_bar.connectStackedWidget(stacked)

    layout.addWidget(tab_bar)
    layout.addWidget(stacked)

    main.show()
    sys.exit(app.exec_())
