from PyQt5.QtCore import QObject, QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QWidget

from app_config import Animation


class KitAnimationFactory(QObject):

    def __init__(self):
        super(KitAnimationFactory, self).__init__()

    @classmethod
    def make(cls, target: QWidget, aniType: Animation, startValue, endValue, duration: int = 200):
        if aniType == Animation.Opacity:
            return cls.make_opacity(target, startValue, endValue, duration)
        elif aniType == Animation.Move:
            return cls.make_move(target, startValue, endValue, duration)
        elif aniType == Animation.Geometry:
            return cls.make_geometry(target, startValue, endValue, duration)
        else:
            raise TypeError("aniType must be Animation")

    @classmethod
    def make_opacity(cls, target: QWidget, startValue, endValue, duration: int = 200):
        if not isinstance(target.graphicsEffect(), QGraphicsOpacityEffect):
            opacity_effect = QGraphicsOpacityEffect(target)
            opacity_effect.setOpacity(startValue)
            target.setGraphicsEffect(opacity_effect)
        else:
            opacity_effect = target.graphicsEffect()
            opacity_effect.setOpacity(startValue)

        ani = QPropertyAnimation(opacity_effect, b"opacity", target)
        ani.setDuration(duration)
        ani.setStartValue(startValue)
        ani.setEndValue(endValue)
        return ani

    @classmethod
    def make_geometry(cls, target: QWidget, startValue, endValue, duration: int = 200):
        ani = QPropertyAnimation(target, b"geometry", target)
        ani.setDuration(duration)
        ani.setStartValue(startValue)
        ani.setEndValue(endValue)
        return ani

    @classmethod
    def make_move(cls, target: QWidget, startValue: QPoint, endValue: QPoint, duration: int = 200):
        ani = QPropertyAnimation(target, b"pos", target)
        ani.setDuration(duration)
        ani.setStartValue(startValue)
        ani.setEndValue(endValue)
        return ani
