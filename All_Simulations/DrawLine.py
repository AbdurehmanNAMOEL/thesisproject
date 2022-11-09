
import sys
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QImage
from demoDrawLine import *

class MyDrawLine(QMainWindow):

      def __init__(self):

        # super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.first =  False
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.backup_image = self.image.copy()
        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.show()

      def paintEvent(self, event):

          qp = QPainter(self)
          qp.drawImage(self.rect(), self.backup_image, self.backup_image.rect())

      def mousePressEvent(self, event):

          if event.buttons() & QtCore.Qt.LeftButton:
              # self.first = True
              self.pos1[0], self.pos1[1] = event.pos().x(), event.pos().y()

      def mouseMoveEvent(self, event):
          self.backup_image = self.image.copy()
          self.pos2[0], self.pos2[1] = event.pos().x(), event.pos().y()
          qp = QPainter(self.backup_image)
          #self.image.fill(Qt.white)
          qp.setPen(QPen(Qt.red, 5 ,Qt.SolidLine))

          qp.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
          self.update()

      def mouseReleaseEvent(self, event):
          self.image = self.backup_image

if __name__ == "__main__":
   app = QApplication(sys.argv)
   w = MyDrawLine()
   w.show()
   sys.exit(app.exec_())
