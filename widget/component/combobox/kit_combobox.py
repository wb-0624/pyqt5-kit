from PyQt5.QtCore import Qt, QSize, QVariant, QRect
from PyQt5.QtWidgets import QComboBox, QListView, QStyle, QStyleOptionComboBox

from widget.component.button import KitButton
from widget.component.icon.kit_icon import KitIcon
from utils.constant import Icons
from utils.kit_property import KitNotifyProperty


class KitComboBox(QComboBox):

    currentId = KitNotifyProperty(QVariant)
    """
    [{'id': 1, 'name': 'test1'}, {'id': 2, 'name': 'test2'}}]
    """

    def __init__(self, parent=None):
        super(KitComboBox, self).__init__(parent=parent)
        self.content_list = []
        self.indicator_size = 16

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setView(QListView(self))
        self.view().setTextElideMode(Qt.ElideRight)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setContentList(self, content_list):
        self.content_list = content_list
        self.clear()
        for content in content_list:
            self.addItem(content['name'], content)

    def setCurrentId(self, id):
        self.currentId = id
        if self.content_list is None or len(self.content_list) == 0:
            self.setCurrentIndex(-1)
            return
        for i in self.content_list:
            try:
                if i.get('id') == self.currentId():
                    self.setCurrentText(i.get('name'))
                    return
            except Exception as e:
                print(e)

        self.setCurrentIndex(-1)

    def setIndicatorSize(self, size):
        self.indicator_size = size
        self.update()

    def sizeHint(self):
        return QSize(80, 32)

    def paintEvent(self, e) -> None:
        super().paintEvent(e)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        opt = QStyleOptionComboBox()
        opt.initFrom(self)
        arrow_rect = self.style().subControlRect(QStyle.CC_ComboBox, opt, QStyle.SC_ComboBoxArrow, self)

        rect = QRect(arrow_rect.center().x() - self.indicator_size // 2, arrow_rect.center().y() - self.indicator_size // 2, self.indicator_size, self.indicator_size)
        opt.rect = rect

        if self.view().isVisible():
            icon = KitIcon(Icons.expand_more)
            icon.setObjectName('combobox_icon')
            painter.drawPixmap(rect, icon.toPixmap())
        else:
            icon = KitIcon(Icons.chevron_right)
            icon.setObjectName('combobox_icon')
            painter.drawPixmap(rect, icon.toPixmap())


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
    from PyQt5.QtGui import QFontDatabase, QPainter
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
    combo = KitComboBox()
    combo.setContentList([{'id': 1, 'name': 'test1213512351'}, {'id': 2, 'name': 'test2'}, {'id': 3, 'name': 'test3'}, {'id': 4, 'name': 'test4'}, {'id': 5, 'name': 'test5'}])

    btn1 = KitButton("set1")
    btn1.clicked.connect(lambda: combo.setCurrentId(1))
    btn2 = KitButton("set2")
    btn2.clicked.connect(lambda: combo.setCurrentId(2))

    layout.addWidget(combo)
    layout.addWidget(btn1)
    layout.addWidget(btn2)
    main.show()
    sys.exit(app.exec_())
