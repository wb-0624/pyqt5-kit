from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie

from widget.component.icon.kit_icon import KitIcon


class KitMovieIcon(KitIcon):

    def __init__(self, gif_url: str = 'assets/gif/loading_annular.gif', parent=None):
        super(KitMovieIcon, self).__init__(parent=parent)

        self.movie_gif = QMovie(gif_url)

        self.__init_widget()
        self.__init_slot()
        self.__init_qss()

    def __init_widget(self):
        self.setMovie(self.movie_gif)
        self.movie().start()
        self.movie().setSpeed(200)

    def __init_slot(self):
        pass

    def __init_qss(self):
        self.setAttribute(Qt.WA_StyledBackground, True)

    def resizeEvent(self, a0):
        self.movie_gif.setScaledSize(self.size())

    def sizeHint(self):
        return QSize(60, 60)
