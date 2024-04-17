import json

from config import config

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineSettings
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QApplication


class KitEcharts(QWebEngineView):

    def __init__(self, parent=None):
        super(KitEcharts, self).__init__(parent=parent)
        self.opts = ""

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        # 使用相对路径
        url_string = config.app_root_path.replace('\\', '/') + "/assets/html/echarts/echarts.html"
        self.load(QUrl(url_string))
        web_settings = QWebEngineProfile.defaultProfile().settings()
        web_settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        web_settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        web_settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def setOptions(self, opts: dict):
        self.opts = opts
        self.page().runJavaScript(f"setOptions({json.dumps(opts)})")


if __name__ == "__main__":
    import sys
    from widget import KitFramelessWindow

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()
    window = KitFramelessWindow()
    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    echarts = KitEcharts()
    layout.addWidget(echarts)

    s = [150, 230, 224, 218, 135, 147, 260]
    opt = {
        'xAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [
            {
                'data': [150, 230, 224, 218, 135, 147, 260],
                'type': 'line'
            }
        ]
    }
    echarts.loadFinished.connect(lambda: echarts.setOptions(opt))

    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
