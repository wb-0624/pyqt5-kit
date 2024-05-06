import os

import sass
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication

from app_config import Theme


class Config(QObject):
    theme_dir_list = ["component"]

    def __init__(self):
        super().__init__()
        # 工程根目录
        self.app_root_path = ""
        self.theme = Theme.LIGHT
        self.get_app_root_path()

    def get_app_root_path(self):
        # 获取当前文件所在的绝对路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件所在的目录
        self.app_root_path = os.path.dirname(current_path)

    def set_theme(self, theme: Theme):
        self.theme = theme

    def init(self):
        self.init_qss()
        self.init_font()

    def addThemeDir(self, theme_dir: str):
        """
        添加主题文件夹
        :param theme_dir: 主题文件夹名称，例如：custom
        :return: 主题目录列表
        """
        self.theme_dir_list.append(theme_dir)
        return self.theme_dir_list

    def init_qss(self):
        app = QApplication.instance()
        # 读取主题文件下的组件样式部分
        css = ""
        qss = ""
        for theme_dir in self.theme_dir_list:
            theme_component_dir = self.app_root_path + "\\theme\\" + theme_dir + "\\"
            theme_component_list = os.listdir(theme_component_dir)
            for file in theme_component_list:
                if file.endswith(".scss"):
                    with open(theme_component_dir + file, "r", encoding="utf-8") as f:
                        css += f.read()
                elif file.endswith(".qss"):
                    with open(theme_component_dir + file, "r", encoding="utf-8") as f:
                        qss += f.read()

        # 读取主题文件下的通用样式变量 例如：颜色，字体
        theme_common_dir = self.app_root_path + "\\theme\\common\\"
        theme_common_list = os.listdir(theme_common_dir)
        theme_common = ''
        for file in theme_common_list:
            if file.endswith(".scss"):
                theme_common += f'@import "theme/common/{file}";\n'

        # 读取主题文件下的当前主题样式变量
        current_theme = f'@import "theme/{self.theme}.scss";\n'

        # 给组件 scss 导入通用变量和当前主题变量
        css = theme_common + current_theme + css
        css = sass.compile(string=css)
        app.setStyleSheet(css + qss)

    def init_font(self):
        QFontDatabase.addApplicationFont(self.app_root_path + "\\assets\\font\\Ubuntu-Regular.ttf")
        QFontDatabase.addApplicationFont(self.app_root_path + "\\assets\\font\\Material-Icons.ttf")
        QFontDatabase.addApplicationFont(self.app_root_path + "\\assets\\font\\FluentSystemIcons-Regular.ttf")
        QFontDatabase.addApplicationFont(self.app_root_path + "\\assets\\font\\FluentSystemIcons-Filled.ttf")


config = Config()
