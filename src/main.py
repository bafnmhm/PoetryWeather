import sys
from PyQt4 import QtCore, QtGui


class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # set base window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # shadow
        shadow = QtGui.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(26)
        shadow.setColor(QtGui.QColor(100, 100, 100))
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

        # create gird and day label
        labelDay1 = QtGui.QLabel("<p style='color: #666;font-family: arial'>Sunday</p>")
        labelDay2 = QtGui.QLabel("<p style='color: #666;font-family: arial'>Monday</p>")
        labelDay3 = QtGui.QLabel("<p style='color: #666;font-family: arial'>Tuesday</p>")

        labelTemp1 = QtGui.QLabel("<p style='color: #666;font-family: arial'>20C-21C</p>")
        labelTemp2 = QtGui.QLabel("<p style='color: #666;font-family: arial'>20C-21C</p>")
        labelTemp3 = QtGui.QLabel("<p style='color: #666;font-family: arial'>20C-21C</p>")

        vBox = QtGui.QVBoxLayout()
        vBox.setAlignment(QtCore.Qt.AlignCenter)
        vBox.addStretch(8)

        girdLayout = QtGui.QGridLayout()
        girdLayout.addItem(QtGui.QSpacerItem(180, 1), 0, 2)
        girdLayout.addWidget(labelDay1, 0, 1)
        girdLayout.addWidget(labelDay2, 1, 1)
        girdLayout.addWidget(labelDay3, 2, 1)
        girdLayout.addWidget(labelTemp1, 0, 3)
        girdLayout.addWidget(labelTemp2, 1, 3)
        girdLayout.addWidget(labelTemp3, 2, 3)
        vBox.addLayout(girdLayout)
        vBox.addStretch(1)

        self.setLayout(vBox)
        self.resize(400, 700)

    def paintEvent(self, event):
        borderRadius = 15
        winSize = self.size()
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
        qp.setPen(QtGui.QColor(255, 255, 255))
        qp.setBrush(QtGui.QColor(255, 255, 255))
        qp.drawRoundedRect(20, 20, winSize.width() - 40, winSize.height() - 40, borderRadius, borderRadius)
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
