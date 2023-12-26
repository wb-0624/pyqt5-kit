from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel

from widget.component.icon.kit_icon import KitIcon
from app_config.constant import Icons


class KitFileDropArea(QWidget):
    dropped = pyqtSignal(list, list)

    def __init__(self, file_match: list = None, parent=None):
        super(KitFileDropArea, self).__init__(parent=parent)
        if file_match is None:
            file_match = []
        self.file_match = file_match
        self.drop_file_paths = []
        self.accepted_file_paths = []
        self.rejected_file_paths = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setAcceptDrops(True)
        self.setMouseTracking(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.icon = KitIcon(Icons.md_post_add, self)
        self.layout.addStretch(1)
        self.layout.addWidget(self.icon, alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel("拖拽文件到此处", self), alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel("仅支持 " + str(self.file_match) + " 文件", self), alignment=Qt.AlignCenter)
        self.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def validFile(self, file_paths: [str], file_match: list):
        self.accepted_file_paths.clear()
        self.rejected_file_paths.clear()
        if len(file_match) == 0:
            self.accepted_file_paths = file_paths

        for file_path in file_paths:
            if file_path.endswith(tuple(file_match)):
                self.accepted_file_paths.append(file_path)
            else:
                self.rejected_file_paths.append(file_path)

    def sizeHint(self):
        return QSize(100, 40)

    def dragEnterEvent(self, ev):
        if ev.mimeData().hasUrls():
            ev.accept()
        else:
            ev.ignore()

    def dropEvent(self, a0) -> None:
        self.drop_file_paths.clear()
        for url in a0.mimeData().urls():
            file_path = url.toLocalFile()
            self.drop_file_paths.append(file_path)
        self.validFile(self.drop_file_paths, self.file_match)
        self.dropped.emit(self.accepted_file_paths, self.rejected_file_paths)



