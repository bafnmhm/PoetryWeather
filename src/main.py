import sys
from PyQt4 import QtCore, QtGui


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 700)

        shadow = QtGui.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(26)
        shadow.setColor(QtGui.QColor(100, 100, 100))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

    def paintEvent(self, event):
        border_radius = 15
        s = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(QtGui.QColor(255, 255, 255))
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRoundedRect(20, 20, s.width() - 40, s.height() - 40, border_radius, border_radius)
        qp.end()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.__dragPosition = QtCore.QPoint(-1, -1)
            event.accept()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.__dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            if self.__dragPosition != QtCore.QPoint(-1, -1):
                self.move(event.globalPos() - self.__dragPosition)
            event.accept()

    __dragPosition = QtCore.QPoint(-1, -1)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
