from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport


def print_widget(widget, filename):
    printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.HighResolution)
    printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
    printer.setOutputFileName(filename)
    painter = QtGui.QPainter(printer)

    # start scale
    xscale = printer.pageRect().width() * 1.0 / widget.width()
    yscale = printer.pageRect().height() * 1.0 / widget.height()
    scale = min(xscale, yscale)
    painter.translate(printer.paperRect().center())
    painter.scale(scale, scale)
    painter.translate(-widget.width() / 2, -widget.height() / 2)
    # end scale

    widget.render(painter)
    painter.end()


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        title = "PyQt5 export pdf"
        top, left, width, height = 200, 500, 680, 480
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.createEditor()
        self.CreateMenu()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        exportpdfAction = QtWidgets.QAction(QtGui.QIcon("pdf.png"), "Export PDF", self)
        exportpdfAction.triggered.connect(self.printPDF)
        fileMenu.addAction(exportpdfAction)

    def createEditor(self):
        self.label = QtWidgets.QLabel("I would like to print this")
        self.setCentralWidget(self.label)

    def printPDF(self):
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()"
        )
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "":
                fn += ".pdf"

            print_widget(self.label, fn)


if __name__ == "__main__":
    import sys

    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    App.exec()
