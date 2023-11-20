from PyQt5.QtCore import Qt, QSize, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel

from widget.component.icon.kit_icon import KitIcon
from widget.component.popup.kit_modal import KitModal
from app_config.constant import Icons


class KitFileDropArea(QWidget):
    filePathsChanged = pyqtSignal(list)

    def __init__(self, file_match: list = None, parent=None):
        super(KitFileDropArea, self).__init__(parent=parent)
        if file_match is None:
            file_match = []
        self.file_match = file_match
        self.file_paths = []

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setAcceptDrops(True)
        self.setMouseTracking(True)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.icon = KitIcon(Icons.post_add, self)
        self.layout.addStretch(1)
        self.layout.addWidget(self.icon, alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel("拖拽文件到此处", self), alignment=Qt.AlignCenter)
        self.layout.addWidget(QLabel("仅支持 " + str(self.file_match) + " 文件", self), alignment=Qt.AlignCenter)
        self.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def addFilePaths(self, file_path: str, file_match: list):
        if len(file_match) == 0:
            self.file_paths.append(file_path)

        for match in file_match:
            if match in file_path:
                self.file_paths.append(file_path)
                return

        KitModal.notice("类型错误", "仅支持 " + str(file_match) + " 文件")

    def sizeHint(self):
        return QSize(100, 40)

    def dragEnterEvent(self, ev):
        if ev.mimeData().hasUrls():
            ev.accept()
        else:
            ev.ignore()

    def dropEvent(self, a0) -> None:
        self.file_paths.clear()
        for url in a0.mimeData().urls():
            file_path = url.toLocalFile()
            self.addFilePaths(file_path, self.file_match)
        self.filePathsChanged.emit(self.file_paths)


if __name__ == "__main__":
    from PyQt5.QtGui import QFontDatabase
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)

    fontId = QFontDatabase.addApplicationFont("assets/font/Material-Icons.ttf")

    qss = config.init_qss()
    app.setStyleSheet(qss)

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    file_drop = KitFileDropArea([".png", ".jpg", ".jpeg"])
    layout.addWidget(file_drop)
    main.show()
    sys.exit(app.exec_())
