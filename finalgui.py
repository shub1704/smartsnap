from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from img2text import imagetotext
from img2voice import imagetovoice
from snap22 import takesnap2
import webbrowser
from edit import Paint


class mywindow():
    def connectwindow(self):
        self.win=QtWidgets.QDialog()
        self.ui=takesnap2()
        self.ui.__init_subclass__()
        #self.win.show()

    # mainwindow
    def setupUi(self, Dialog):
        Dialog.setObjectName("Smartsnap")
        Dialog.setStyleSheet("background-color:rgb(0, 0, 0);\n""border-radius:20px")
        Dialog.resize(700, 650)

        # buttons
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(40, 20, 93, 28))
        self.b1.setText("New")
        self.b1.setObjectName("b1")
        self.b1.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b1.clicked.connect(self.connectwindow)

        self.b2 = QtWidgets.QPushButton(Dialog)
        self.b2.setGeometry(QtCore.QRect(40, 70, 93, 28))
        self.b2.setText("Text")
        self.b2.setObjectName("b2")
        self.b2.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b2.clicked.connect(self.text)

        self.b3 = QtWidgets.QPushButton(Dialog)
        self.b3.setGeometry(QtCore.QRect(40, 120, 93, 28))
        self.b3.setText("Voice")
        self.b3.setObjectName("b3")
        self.b3.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b3.clicked.connect(self.voice)

        self.b4 = QtWidgets.QPushButton(Dialog)
        self.b4.setGeometry(QtCore.QRect(40, 170, 93, 28))
        self.b4.setText("Search")
        self.b4.setObjectName("b4")
        self.b4.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b4.clicked.connect(self.search)

        self.b5 = QtWidgets.QPushButton(Dialog)
        self.b5.setGeometry(QtCore.QRect(40, 220, 93, 28))
        self.b5.setText("Edit")
        self.b5.setObjectName("b5")
        self.b5.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b5.clicked.connect(self.edit)

        self.b6 = QtWidgets.QPushButton(Dialog)
        self.b6.setGeometry(QtCore.QRect(40, 270, 93, 28))
        self.b6.setText("Exit")
        self.b6.setObjectName("b6")
        self.b6.setStyleSheet(
            "background-color:rgb(0, 191, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.b6.clicked.connect(self.exit)

        # making label
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("take a snap")
        self.label.setStyleSheet("background-color:rgb(253, 91, 0);\n""color:rgb(255, 255, 255);\n""border-radius:10px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.move(300, 350)
        self.label.setGeometry(QtCore.QRect(180, 350, 500, 250)) # start end width

        # display_photosnap
        self.photo = QtWidgets.QLabel(Dialog)
        self.photo.setGeometry(QtCore.QRect(180, 20, 500, 300))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("snip1.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SmartSnap"))


        '''----------------------------to show output---------------------------'''

    #take a new screenshot
    def new(self):
        self.label.setText("function yet to add")
        self.event=takesnap2()
        event.show()


    # imgtotext
    def text(self):
        pic = Image.open("snip1.png")
        output = tess.image_to_string(pic)
        # print(type(text)) #to check type of output
        self.label.setText(output)

    # imgtovoice
    def voice(self):
        sound=imagetovoice(imagetotext("snip1.png"))
        self.label.setText(sound)

    # imgtosearch
    def search(self):
        query = imagetotext("snip1.png")
        self.label.setText("searching results ....")
        webbrowser.open('https://www.google.com/search?q=' + query)
        self.label.setText()

    # edit the snap
    def edit(self):
        self.label.setText("edit")
        Paint()

    # exit from window
    def exit(self):
        self.label.setText("exit")
        sys.exit(app.exec_())

    def update(self):
        self.label.adjustSize()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    win = mywindow()
    win.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
