import os

import sass
from PyQt5.QtCore import QObject


class Theme:
    DARK = "dark"
    LIGHT = "light"


class Config(QObject):

    def __init__(self):
        super().__init__()
        # 工程根目录
        self.app_root_path = ""
        self.theme = Theme.LIGHT
        self.getAppRootPath()

    def getAppRootPath(self):
        # 获取当前文件所在的绝对路径
        current_path = os.path.abspath(__file__)
        # 获取当前文件所在的目录
        self.app_root_path = os.path.dirname(current_path)

    def init_qss(self):
        current_theme = self.theme
        theme_dir = self.app_root_path + "\\theme\\" + current_theme + "\\"
        theme_list = os.listdir(theme_dir)
        css = ""
        qss = ""
        for file in theme_list:
            if file.endswith(".scss"):
                with open(theme_dir + file, "r", encoding="utf-8") as f:
                    css += f.read()
            elif file.endswith(".qss"):
                with open(theme_dir + file, "r", encoding="utf-8") as f:
                    qss += f.read()
        css = sass.compile(string=css)
        return css + qss


config = Config()
