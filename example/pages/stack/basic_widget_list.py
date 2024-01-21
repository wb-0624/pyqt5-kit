from PyQt5.QtWidgets import QListWidget, QListWidgetItem

from widget import KitIcon
from widget.component.menu.kit_menu import KitMenu
from .demo_card import DemoCard
from ... import ProgressDemo
from ...widgets_demo.combobox_demo import ComboBoxDemo
from ...widgets_demo.button_demo import *
from ...widgets_demo.checkbox_demo import *


class BasicWidgetList(QListWidget):

    def __init__(self, parent=None):
        super(BasicWidgetList, self).__init__(parent=parent)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setSpacing(20)
        btn_card = DemoCard('简单的按钮', 'button_demo.py', 'ButtonDemo')
        btn_demo = ButtonDemo()
        btn_card.setDemoWidget(btn_demo)
        self.addDemoCard(btn_card)

        theme_btn_card = DemoCard('主题色按钮', 'button_demo.py', 'ThemeButtonDemo')
        theme_btn_demo = ThemeButtonDemo()
        theme_btn_card.setDemoWidget(theme_btn_demo)
        self.addDemoCard(theme_btn_card)

        text_btn_card = DemoCard('文字按钮', 'button_demo.py', 'TextButtonDemo')
        text_btn_demo = TextButtonDemo()
        text_btn_card.setDemoWidget(text_btn_demo)
        self.addDemoCard(text_btn_card)

        icon_btn_card = DemoCard('图标按钮', 'button_demo.py', 'IconButtonDemo')
        icon_btn_demo = IconButtonDemo()
        icon_btn_card.setDemoWidget(icon_btn_demo)
        self.addDemoCard(icon_btn_card)

        tool_btn_card = DemoCard('工具按钮', 'button_demo.py', 'ToolButtonDemo')
        tool_btn_demo = ToolButtonDemo()
        tool_btn_card.setDemoWidget(tool_btn_demo)
        self.addDemoCard(tool_btn_card)

        check_box_card = DemoCard('复选框', 'checkbox_demo.py', 'CheckBoxDemo')
        check_box_demo = CheckBoxDemo()
        check_box_card.setDemoWidget(check_box_demo)
        self.addDemoCard(check_box_card)

        combo_box_card = DemoCard('下拉框', 'combobox_demo.py', 'ComboBoxDemo')
        combo_box_demo = ComboBoxDemo()
        combo_box_card.setDemoWidget(combo_box_demo)
        self.addDemoCard(combo_box_card)

        progress_bar_card = DemoCard('进度条', 'progress_demo.py', 'ProgressDemo')
        progress_bar_demo = ProgressDemo()
        progress_bar_card.setDemoWidget(progress_bar_demo)
        self.addDemoCard(progress_bar_card)


        # slider_demo = SliderDemo()
        # self.layout.addWidget(slider_demo)
        #
        # switch_demo = SwitchDemo()
        # self.layout.addWidget(switch_demo)
        #
        # self.layout.addStretch(1)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def contextMenuEvent(self, a0) -> None:
        menu = KitMenu(self)
        menu.addAction(KitIcon(Icons.md_add).toQIcon(), '添加')
        menu.addAction('删除')
        menu.exec_(a0.globalPos())

    def addDemoCard(self, card: DemoCard):
        demo_item = QListWidgetItem(self)
        demo_item.setSizeHint(card.sizeHint())
        self.setItemWidget(demo_item, card)
