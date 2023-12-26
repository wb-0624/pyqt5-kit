import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QLabel

from widget.component.button.kit_button import KitIconButton
from widget.component.input.kit_line_edit import KitLineEdit
from config import config
from app_config.constant import Button, Icons


class TablePagination(QWidget):

    currentPageChanged = pyqtSignal(int, list)

    def __init__(self, parent=None):
        super(TablePagination, self).__init__(parent=parent)

        self.all_page = None
        self.all_data = None
        self.page_data = None
        self.current_page = None
        self.page_sum = 20

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.all_data_label = QLabel()
        self.all_page_label = QLabel()
        self.page_input = KitLineEdit()
        self.page_input.setAlignment(Qt.AlignCenter)
        self.page_input.setTextMargins(0, 0, 0, 0)
        self.page_input.setFixedSize(40, 20)
        self.previous_btn = KitIconButton(Icons.md_chevron_left)
        self.previous_btn.setObjectName('page_icon')
        self.previous_btn.setFixedSize(20, 20)
        self.previous_btn.setType(Button.Text)
        self.next_btn = KitIconButton(Icons.md_chevron_right)
        self.next_btn.setObjectName('page_icon')
        self.next_btn.setFixedSize(20, 20)
        self.next_btn.setType(Button.Text)

        self.layout.addStretch(1)
        self.layout.addWidget(self.all_data_label)
        self.layout.addWidget(self.previous_btn)
        self.layout.addWidget(self.page_input)
        self.layout.addWidget(self.next_btn)
        self.layout.addWidget(self.all_page_label)
        self.layout.addStretch(1)

    def __init_slot(self):

        self.previous_btn.clicked.connect(self.previousPage)
        self.next_btn.clicked.connect(self.nextPage)

        self.page_input.editingFinished.connect(self.__page_input_finished)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setAllData(self, all_data):
        self.all_data = all_data
        self.__fresh_page_info()

    def setPageSum(self, page_sum):
        if self.page_sum <= 0:
            raise ValueError('pageSum must be greater than 0')
        self.page_sum = page_sum
        self.__fresh_page_info()

    def setCurrentPage(self, current_page):
        if self.current_page == current_page:
            return
        self.current_page = current_page
        self.__fresh_page_info()

    def __fresh_page_info(self):

        """
        根据all_data和page_sum计算出 总页数 和 总条目数
        :return:
        """
        if self.all_data is None or self.page_sum is None:
            return

        if len(self.all_data) == 0:
            self.all_data_label.setText('共0条')
            self.all_page_label.setText('共1页')
            self.pageSum = 1
            self.page_input.setText('1')
            self.previous_btn.setEnabled(False)
            self.next_btn.setEnabled(False)
            return

        all_data_count = len(self.all_data)
        self.all_data_label.setText(f'共{all_data_count}条')
        all_page = all_data_count // self.page_sum
        if all_data_count % self.page_sum != 0:
            all_page += 1
        self.all_page = all_page
        self.all_page_label.setText(f'共{all_page}页')

        if self.current_page is None or self.current_page < 1:
            self.current_page = 1
        else:
            self.setCurrentPage(self.current_page)

        self.__fresh_current_page()

    def nextPage(self):
        self.setCurrentPage(int(self.current_page) + 1)

    def previousPage(self):
        self.setCurrentPage(int(self.current_page) - 1)

    def __page_input_finished(self):
        self.setCurrentPage(int(self.page_input.text()))

    def __fresh_current_page(self):
        self.previous_btn.setEnabled(True)
        self.next_btn.setEnabled(True)

        if self.current_page >= self.all_page:
            self.current_page = self.all_page
            self.next_btn.setEnabled(False)
        if self.current_page <= 1:
            self.current_page = 1
            self.previous_btn.setEnabled(False)

        self.page_data = self.all_data[(self.current_page - 1) * self.page_sum: self.current_page * self.page_sum]
        self.page_input.setText(str(self.current_page))

        self.currentPageChanged.emit(self.current_page, self.page_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qss = config.init_qss()
    app.setStyleSheet(qss)
    main = QWidget()
    main.setLayout(QVBoxLayout())
    fontId = QFontDatabase.addApplicationFont("assets/font/iconfont.ttf")
    fontName = QFontDatabase.applicationFontFamilies(fontId)[0]

    page = TablePagination()
    page.setAllData([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    page.setPageSum(3)
    main.layout().addWidget(page)
    btn = QPushButton()
    main.layout().addWidget(btn)

    main.show()
    sys.exit(app.exec_())