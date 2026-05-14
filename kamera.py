from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import sys

class Ui_Form(object):
    def setupUi(self, Form): 
        Form.setObjectName("Form")
        Form.resize(917, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 40, 401, 281))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("kamerakonum")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 400, 93, 51))
        self.pushButton.setObjectName("kameraacbtn")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 410, 101, 51))
        self.pushButton_2.setObjectName("kamerakptbtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Kamera işlemleri
        self.timer = QtCore.QTimer()
        self.cap = None

        self.pushButton.clicked.connect(self.kamerayi_ac)
        self.pushButton_2.clicked.connect(self.kamerayi_kapat)
        self.timer.timeout.connect(self.goruntuyu_guncelle)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "kamera aç"))
        self.pushButton_2.setText(_translate("Form", "kamera kapat"))

    def kamerayi_ac(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(30)

    def goruntuyu_guncelle(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytesPerLine = ch * w
            qImg = QtGui.QImage(frame.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(qImg)
            self.label.setPixmap(pix.scaled(self.label.width(), self.label.height(), QtCore.Qt.KeepAspectRatio))

    def kamerayi_kapat(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.label.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
