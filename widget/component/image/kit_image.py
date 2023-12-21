from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy


class KitImage(QWidget):

    Fit = 0
    Fill = 1

    def __init__(self, img_url=None, mode=Fit, parent=None):
        super(KitImage, self).__init__(parent=parent)

        self.image = None
        self.origin_image_size = None
        self.target_image_size = None
        self.mode = KitImage.Fit

        self.img_label = QLabel(self)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

        self.setImage(img_url, mode)

    def __init_widget(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        self.img_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.img_label.setMinimumSize(1, 1)
        self.layout.addWidget(self.img_label, alignment=Qt.AlignCenter)

    def __init_slot(self):
        pass

    def __init_qss(self):
        pass

    def setImage(self, img_url, mode):
        if img_url is None:
            return
        self.mode = mode
        self.image = QPixmap(img_url)
        if self.image.isNull():
            raise Exception("图片加载失败, 请检查图片路径是否正确")
        self.origin_image_size = self.image.size()

    def freshImageSize(self):
        origin_radio = self.origin_image_size.width() / self.origin_image_size.height()
        # 不同的模式，图片的大小计算方式不同
        if self.mode == KitImage.Fill:
            self.target_image_size = self.size()
        elif self.mode == KitImage.Fit:
            current_radio = self.size().width() / self.size().height()
            if current_radio >= origin_radio:
                self.target_image_size = QSize(int(self.size().height() * origin_radio), self.size().height())
            else:
                self.target_image_size = QSize(self.size().width(), int(self.size().width() / origin_radio))

        self.img_label.resize(self.target_image_size)
        # 使用 QPainter 对缩放后的图片进行绘制，以启用平滑的图像缩放
        # 会在一定程度上消耗性能
        new_pixmap = self.image.scaled(self.target_image_size)
        painter = QPainter(new_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        painter.setRenderHint(QPainter.NonCosmeticDefaultPen)
        painter.drawPixmap(new_pixmap.rect(), self.image, self.image.rect())
        painter.end()
        self.img_label.setPixmap(new_pixmap)

    def resizeEvent(self, event):
        self.freshImageSize()
        super(KitImage, self).resizeEvent(event)


