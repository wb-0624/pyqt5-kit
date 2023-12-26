from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QWidget, QScrollArea, QVBoxLayout

from demo.widgets_demo import ButtonDemo, InputDemo, CheckBoxDemo, ProgressDemo, SliderDemo, SwitchDemo

class BasicStack(QScrollArea):

    def __init__(self, parent=None):
        super(BasicStack, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.content = QWidget()
        self.content.resize(500, 1000)
        self.setWidget(self.content)
        self.layout = QVBoxLayout()
        self.content.setLayout(self.layout)

        btn_demo = ButtonDemo()
        self.layout.addWidget(btn_demo)

        input_demo = InputDemo()
        self.layout.addWidget(input_demo)

        check_demo = CheckBoxDemo()
        self.layout.addWidget(check_demo)

        progress_demo = ProgressDemo()
        self.layout.addWidget(progress_demo)

        slider_demo = SliderDemo()
        self.layout.addWidget(slider_demo)

        switch_demo = SwitchDemo()
        self.layout.addWidget(switch_demo)

        self.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def eventFilter(self, a0, a1) -> bool:
        if a1.type() == QEvent.DynamicPropertyChange:
            self.update()
        elif a1.type() == QEvent.Wheel:
            self.update()
        return super().eventFilter(a0, a1)


