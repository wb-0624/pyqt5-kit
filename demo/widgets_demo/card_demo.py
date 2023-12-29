from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from widget import KitCard, KitFramelessWindow

class CardDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        card = KitCard()
        layout.addWidget(card)
        card_2 = KitCard()
        layout.addWidget(card_2)
        card_3 = KitCard()
        layout.addWidget(card_3)

if __name__ == "__main__":
    from config import config
    import sys

    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    config.init()




    window = KitFramelessWindow()
    # window = KitWindow()

    demo = CardDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
