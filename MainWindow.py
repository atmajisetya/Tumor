from http.client import ImproperConnectionState
import sys
import os
import PyQt5
from fpdf import FPDF
from PIL import Image

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from ui_MainWindow import Ui_MainWindow
from detect import *


class MainWindow:
    img_path = ""
    result_folder_path = ""
    folder_path = ""

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        # set the title
        # self.ui.setWindowTitle("BrainTumorDetector")

        # untuk pindah antar stacked widget (menu fitur)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        self.ui.btn_menu_proses2.clicked.connect(self.showMulProses)
        self.ui.btn_menu_proses1.clicked.connect(self.showProses)
        self.ui.btn_menu_bantuan.clicked.connect(self.showHelp)
        self.ui.btn_menu_tentang.clicked.connect(self.showAbout)

        # event browse gambar untuk proses 1 image
        self.ui.btn_browse1.clicked.connect(self.getImage)
        # event browse gambar untuk proses multi image
        self.ui.btn_browsemul.clicked.connect(self.getImageMul)
        # event detect 1 image
        self.ui.btn_proses1.clicked.connect(self.predict1)
        # event detect multi image
        self.ui.btn_prosesmul.clicked.connect(self.multiPredict)

        # event donwload pdf 1 citra
        self.ui.btn_pdf1.clicked.connect(self.downloadPdf)

        # event donwload pdf multi citra
        self.ui.btn_pdf2.clicked.connect(self.downloadMultiPdf)

    def show(self):
        self.main_win.show()

    # fungsi untuk menampilkan page fitur multiple proses
    def showMulProses(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_mulproses)

    # fungsi untuk menampilkan page home/fitur proses 1 gambar
    def showProses(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    # fungsi untuk menampilkan page help
    def showHelp(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_bantuan)

    # fungsi untuk menampilkan page about us
    def showAbout(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_tentang)

    # fungsi untuk mengambil gambar dari users
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self.main_win, 'Open file',
                                            'c:\\', "Image files (*.jpg *.png)")
        # print(fname)
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        mid_rez = QSize(300, 300)
        pixmap = pixmap.scaled(mid_rez)
        self.ui.label_img_input.setPixmap(QPixmap(pixmap))
        self.ui.label_img_input.setScaledContents(True)
        self.img_path = imagePath
        # return imagePath

    def getImageMul(self):
        # fname = QFileDialog.getOpenFileNames(self.main_win, 'Open file',
        #                                      'c:\\', "Image files (*.jpg *.png)")
        # print(list_img_path)
        # print(fname)
        file = str(QFileDialog.getExistingDirectory())
        print(file)
        self.folder_path = file
        list_img_path = []
        list_img = os.listdir(file)
        for x in list_img:
            list_img_path.append(self.folder_path + "\\" + x)

        print(list_img_path)
        pixmap = QPixmap(list_img_path[0])
        mid_rez = QSize(500, 500)
        pixmap = pixmap.scaled(mid_rez)
        # imagePath = fname[0][1]
        # pixmap = QPixmap(imagePath)
        self.ui.label_mulimg.setPixmap(QPixmap(pixmap))
        self.ui.label_mulimg.setScaledContents(True)

    # melakukan deteksi untuk 1 image
    def predict1(self):
        weight_path = "C:\Capstone\Tumor\model_epoch300_yolov5s_augmented.pt"
        self.result_folder_path = run(weights=weight_path, source=self.img_path)
        self.result_folder_path = str(self.result_folder_path)
        # print(self.result_folder_path)
        list_img_path = []
        list_img = os.listdir(self.result_folder_path)
        for x in list_img:
            list_img_path.append(self.result_folder_path + "\\" + x)

        # print(list_img_path[0])
        pixmap = QPixmap(list_img_path[0])
        mid_rez = QSize(300, 300)
        pixmap = pixmap.scaled(mid_rez)
        self.ui.label_img_result.setPixmap(QPixmap(pixmap))
        self.ui.label_img_result.setScaledContents(True)
        # self.ui.label_img_result
        # print(self.img_path)

    # melakukan deteksi untuk multiple image
    def multiPredict(self):
        weight_path = "C:\Capstone\Tumor\model_epoch300_yolov5s_augmented.pt"
        self.result_folder_path = run(weights=weight_path, source=self.folder_path)
        self.result_folder_path = str(self.result_folder_path)

        list_img_path = []
        list_img = os.listdir(self.result_folder_path)
        for x in list_img:
            list_img_path.append(self.result_folder_path + "\\" + x)

        pixmap = QPixmap(list_img_path[0])
        mid_rez = QSize(500, 500)
        pixmap = pixmap.scaled(mid_rez)
        self.ui.label_mulimg.setPixmap(QPixmap(pixmap))
        self.ui.label_mulimg.setScaledContents(True)

    # download 1 citra pdf
    def downloadPdf(self):
        pdf_path = QFileDialog.getSaveFileName(self.main_win,
                                               "Save pdf file", "", ("PDF files (*.pdf)"))
        pdf_path = str(pdf_path[0])

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # create a cell
        pdf.cell(200, 10, txt="Diagnostic Result",
                 ln=1, align='C')
        pdf.cell(200, 10, txt="Patient's Name: " + self.ui.lineEditPasien.text(),
                 ln=2, align='L')
        # add another cell
        pdf.cell(200, 10, txt="Patient Gender: " + self.ui.lineEditKelamin.text(),
                 ln=3, align='L')

        # path image harus relative path
        list_img_path = []
        list_img = os.listdir(self.result_folder_path)
        for x in list_img:
            list_img_path.append(self.result_folder_path + "\\" + x)

        # add image
        pdf.image(list_img_path[0], w=100, h=100)
        # save the pdf with name .pdf

        # save the pdf
        pdf.output(name=pdf_path)
        pdf_path_internal = self.result_folder_path + "\HasilTumor.pdf"
        print(pdf_path_internal)
        pdf.output(name=pdf_path_internal)

    # download multi citra pdf
    def downloadMultiPdf(self):
        pdf_path = QFileDialog.getSaveFileName(self.main_win,
                                               "Save pdf file", "", ("PDF files (*.pdf)"))
        pdf_path = str(pdf_path[0])

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        # create a cell
        pdf.cell(200, 10, txt="Diagnostic Results",
                 ln=1, align='C')

        list_img_path = []
        list_img = os.listdir(self.result_folder_path)
        for x in list_img:
            list_img_path.append(self.result_folder_path + "\\" + x)

        for i in list_img_path:
            pdf.image(i, w=100, h=100)

        # save the pdf
        pdf.output(name=pdf_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
