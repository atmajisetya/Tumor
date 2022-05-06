from http.client import ImproperConnectionState
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QPixmap
from ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # untuk pindah antar stacked widget (menu fitur)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.btn_menu_proses2.clicked.connect(self.showMulProses)
        self.ui.btn_menu_proses1.clicked.connect(self.showProses)

        # event browse gambar untuk proses 1 image
        self.ui.btn_browse1.clicked.connect(self.getImage)
        # event browse gambar untuk proses multi image
        self.ui.btn_browsemul.clicked.connect(self.getImageMul)

    def show(self):
        self.main_win.show()

    # fungsi untuk menampilkan page fitur multiple proses
    def showMulProses(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_mulproses)

    # fungsi untuk menampilkan page home/fitur proses 1 gambar
    def showProses(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    # fungsi untuk mengambil gambar dari users
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self.main_win, 'Open file',
                                            'c:\\', "Image files (*.jpg *.png)")
        # print(fname)
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.ui.label_img_input.setPixmap(QPixmap(pixmap))
        self.ui.label_img_input.setScaledContents(True)

    def getImageMul(self):
        fname = QFileDialog.getOpenFileNames(self.main_win, 'Open file',
                                             'c:\\', "Image files (*.jpg *.gif)")
        print(fname)
        imagePath = fname[0][1]
        pixmap = QPixmap(imagePath)
        self.ui.label_mulimg.setPixmap(QPixmap(pixmap))
        self.ui.label_mulimg.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())