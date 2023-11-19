from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame, QApplication

from widget.component.button.kit_button import KitIconButton, KitButton
from widget.component.overlay.kit_overlay import KitOverlay
from widget.component.popup.kit_popup import KitPopup
from utils.constant import ClosePolicy, Icons, Button


class KitModal(KitPopup):
    confirm = pyqtSignal()
    cancel = pyqtSignal()

    def __init__(self, title: [str, QWidget], content: [str, QWidget]):
        super(KitModal, self).__init__()

        self.close_policy = ClosePolicy.CloseOnClicked

        self.header_layout = QHBoxLayout()
        self.content = QVBoxLayout()
        self.close_btn = KitIconButton(Icons.close)
        self.close_btn.setStyle(Button.Text)
        self.close_btn.setShape(Button.Round)

        self.overlay = KitOverlay()
        self.overlay.setClosePolicy(self.close_policy)

        if isinstance(title, str):
            self.title = QLabel(title)
            self.title.setObjectName('modal_title')
            self.header_layout.addWidget(self.title)
        elif isinstance(title, QWidget):
            self.header_layout.addWidget(title)

        if isinstance(content, QWidget):
            self.content.addWidget(content)
        elif isinstance(content, str):
            self.content.addWidget(QLabel(content))

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.header_layout.setAlignment(Qt.AlignVCenter)
        self.header_layout.addStretch(1)
        self.header_layout.addWidget(self.close_btn)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(16, 16, 16, 16)
        self.layout.addLayout(self.header_layout)
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        self.layout.addWidget(divider)
        self.layout.addLayout(self.content, stretch=1)

        self.setLayout(self.layout)

    def __init_slot(self):
        self.close_btn.clicked.connect(self.close)
        self.overlay.clicked.connect(lambda: self.close() if self.close_policy == ClosePolicy.CloseOnClicked else None)

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setClosePolicy(self, policy: [ClosePolicy.CloseOnClicked, ClosePolicy.CloseOnEscape]):
        self.close_policy = policy
        self.overlay.setClosePolicy(self.close_policy)

    def setCloseBtn(self, show: bool):
        self.close_btn.setVisible(show)

    def paintEvent(self, a0):
        super().paintEvent(a0)

    def show(self):
        self.overlay.show()
        self.raise_()
        super().show()

    def close(self):
        self.overlay.close()
        super().close()

    @classmethod
    def notice(cls, title, content):
        modal_notice = cls(title, content)
        modal_notice.setClosePolicy(ClosePolicy.CloseOnEscape)
        modal_notice.show()
        return modal_notice

    @classmethod
    def dialog(cls, title, content, confirm_slot, cancel_slot=None):
        modal_dialog = cls(title, content)
        modal_dialog.setCloseBtn(False)
        modal_dialog.setClosePolicy(ClosePolicy.CloseOnEscape)

        bottom_layout = QHBoxLayout()
        modal_dialog.layout.addLayout(bottom_layout)

        confirm_btn = KitButton("确定")
        confirm_btn.setType(Button.Primary)
        cancel_btn = KitButton("取消")
        cancel_btn.setType(Button.Danger)

        confirm_btn.clicked.connect(lambda: modal_dialog.confirm.emit())
        cancel_btn.clicked.connect(lambda: modal_dialog.cancel.emit())

        bottom_layout.addWidget(cancel_btn)
        bottom_layout.addWidget(confirm_btn)

        modal_dialog.confirm.connect(confirm_slot)
        if cancel_slot:
            modal_dialog.cancel.connect(cancel_slot)
        else:
            modal_dialog.cancel.connect(modal_dialog.close)

        modal_dialog.show()
        return modal_dialog


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QFontDatabase
    from config import config
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
    btn = KitButton('notice')
    btn2 = KitButton('dialog')
    layout.addWidget(btn)
    layout.addWidget(btn2)

    content1 = QWidget()
    content1.setLayout(QVBoxLayout())
    content1.layout().addWidget(QLabel('123'))
    content1.layout().addWidget(QLabel('456'))
    content1.layout().addWidget(KitButton('789'))

    btn.clicked.connect(lambda: KitModal.notice("title", content1))
    btn2.clicked.connect(lambda: KitModal.dialog('123', '456', lambda: print('confirm')))

    main.show()
    sys.exit(app.exec_())