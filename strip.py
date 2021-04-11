import sys
import cv2
import math
from PyQt5.QtGui import QPainter, QImage, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class Girl(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.initUI(app.arguments()[1])

    def initUI(self, path):
        vidcap = cv2.VideoCapture(path)
        _,image = vidcap.read()
        h,w,_ = image.shape
        h = int(h/2)
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        geo = self.app.desktop().screenGeometry()
        width, height = geo.width(), geo.height()

        self.setGeometry(width*2-w, height, w, h)
        self.setStyleSheet("background:transparent")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.WindowDoesNotAcceptFocus | Qt.Tool)
        self.show()
        self.playVideo(vidcap, geo)
        sys.exit(0)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        qp.drawPixmap(self.rect(), self.qpx)
        qp.end()

    def playVideo(self, vidcap, geo):
        def sigmoid(x):
            return 1 / (1 + math.exp(-x))
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        success = True
        count = 0
        length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        vis = 0
        while success:
            if count <= 31:
                vis = count/30
            elif length-count <= 31:
                vis = (length-count)/30

            success,image = vidcap.read()
            if not success:
                continue
            height, width, channel = image.shape
            girl = image[0:int(height/2), 0:width] #this line crops
            mask = image[int(height/2):height, 0:width] #this line crops
            b,g,r = cv2.split(girl)
            a,_,_ = cv2.split(mask)

            if vis <= 30:
                a = cv2.multiply(a, vis) # fade in

            img_ARGB = cv2.merge((b,g,r,a))
            h,w,c = img_ARGB.shape

            if vis > 0 and vis <= 30:
                self.setGeometry(geo.width()*2-w, geo.height()-int(h*sigmoid(vis*12-6)), w, h)

            bytesPerLine = 4 * width
            qImg = QImage(img_ARGB.data, width, int(height/2), bytesPerLine, QImage.Format_ARGB32)
            self.qpx = QPixmap.fromImage(qImg)
            count = count + 1
            self.update()
            if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Girl(app)
    sys.exit(app.exec_())
