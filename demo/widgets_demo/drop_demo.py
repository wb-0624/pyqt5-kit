from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitFramelessWindow, KitFileDropArea, KitModal

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

    window = KitFramelessWindow()

    main = QWidget()
    layout = QVBoxLayout()
    main.setLayout(layout)
    file_drop = KitFileDropArea([".png", ".jpg", ".jpeg"])
    layout.addWidget(file_drop)
    file_drop.dropped.connect(lambda l1, l2: KitModal.notice('info', '接受文件' + ','.join(l1)+'\n拒绝文件' + '.'.join(l2)))
    window.setCentralWidget(main)
    window.show()
    sys.exit(app.exec_())
