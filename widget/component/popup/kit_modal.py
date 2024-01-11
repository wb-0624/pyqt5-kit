from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QFrame

from ..button import KitIconButton, KitButton
from ..overlay import KitOverlay
from ..popup import KitPopup
from app_config.constant import ClosePolicy, Icons, Button


class KitModal(KitPopup):
    confirm = pyqtSignal()
    cancel = pyqtSignal()

    def __init__(self, window, title: [str, QWidget], content: [str, QWidget]):
        super(KitModal, self).__init__(window=window)

        self.close_policy = ClosePolicy.CloseOnClicked
        self.window = window

        self.header_layout = QHBoxLayout()
        self.content = QVBoxLayout()
        self.close_btn = KitIconButton(Icons.md_close)
        self.close_btn.setStyle(Button.Text)
        self.close_btn.setShape(Button.Round)

        self.overlay = KitOverlay(window)
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
            label = QLabel(content)
            label.setWordWrap(True)
            self.content.addWidget(label)

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

    def showEvent(self, a0) -> None:
        self.adjustSize()
        self.resize(self.window.width() // 2, self.height())
        self.overlay.show()
        self.raise_()
        super().showEvent(a0)

    def close(self):
        self.overlay.close()
        super().close()

    @classmethod
    def notice(cls, parent, title, content):
        modal_notice = cls(parent, title, content)
        modal_notice.setClosePolicy(ClosePolicy.CloseOnEscape)
        modal_notice.resize(modal_notice.sizeHint())
        modal_notice.show()
        return modal_notice

    @classmethod
    def dialog(cls, parent, title, content, confirm_slot, cancel_slot=None):
        modal_dialog = cls(parent, title, content)
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
