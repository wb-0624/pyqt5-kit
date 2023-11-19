from PyQt5.QtCore import QObject, pyqtSignal, QSize


# 全局信号中心
class SignalCenter(QObject):

    # 很重要，因为有些组件会根据窗口大小变化而变化
    # message位置
    mainWindowResized = pyqtSignal(QSize)


signal_center = SignalCenter()
