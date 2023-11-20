# 全局变量和变化
from PyQt5.QtCore import QObject


class KitRoot(QObject):

    def __init__(self):
        super().__init__()

        self.mainWindowSize = None

    def main_window_resized_slot(self, size):
        self.mainWindowSize = size


root = KitRoot()
