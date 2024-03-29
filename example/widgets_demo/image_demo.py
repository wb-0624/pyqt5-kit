import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

from config import config
from widget import KitFramelessWindow, KitImage

class ImageDemo(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        image = KitImage()
        image.setImage("assets/img/radio_button_checked.svg", KitImage.Fit)
        layout.addWidget(image)
        image_2 = KitImage()
        image_2.setImage("assets/img/radio_button_checked.svg", KitImage.Fit)
        image_2.setFixedHeight(100)
        layout.addWidget(image_2)
        image_3 = KitImage()
        image_3.setImage("assets/img/radio_button_checked.svg", KitImage.Fill)
        layout.addWidget(image_3)

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    config.init()



    window = KitFramelessWindow()
    # window = KitWindow()

    demo = ImageDemo()
    window.setCentralWidget(demo)
    window.show()
    sys.exit(app.exec_())
