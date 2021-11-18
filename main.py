import sys, logging
from datetime import datetime
from PyQt5 import uic    
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QApplication)

class MainWindow(QMainWindow):
    def __init__(self, app, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mainApp = app
        self.load_main_ui()
        self.filename = ""
        
    def load_main_ui(self):
            logging.info("Loading main ui")
            uic.loadUi('ui/Emotifier.ui', self)
            self.connect_buttons()
            self.pixelizeButton.setEnabled(False)
            self.cartoonButton.setEnabled(False)
    def connect_buttons(self):
        self.pixelizeButton = self.findChild(QPushButton, 'pixilizeButton')
        #self.pixelizeButton.clicked.connect(self.pixelize)
        self.cartoonButton = self.findChild(QPushButton, 'cartoonButton')
        #self.cartoonButton.clicked.connect(self.cartoonify)
        
        self.uploadButton = self.findChild(QPushButton, 'uploadButton')
        self.uploadButton.clicked.connect(self.askForImg)
        self.ExitButton = self.findChild(QPushButton, 'ExitButton')
        self.ExitButton.clicked.connect(self.closeProgram)

    def closeProgram(self):
        exit()

    def askForImg(self):
        root = tk.Tk()
        root.withdraw()
        filetypes = (
            ('jpg files', '*.jpg'),('png files', '*.png'),('bmp files', '*.bmp'),
        )

        self.filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        print(self.filename)
        if(self.filename.find('.jpg')>-1 or self.filename.find('.png')>-1 or self.filename.find('.bmp')>-1):
            self.pixelizeButton.setEnabled(True)
            self.cartoonButton.setEnabled(True)
        else:
            self.pixelizeButton.setEnabled(False)
            self.cartoonButton.setEnabled(False)

def main():
    app = QApplication(sys.argv)
    main = MainWindow(app)
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    logging.root.handlers = []

    now = datetime.now()
    filename = now.strftime('%y-%m-%d-%H-%M-%S')

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("logs/{}.log".format(filename)),
            logging.StreamHandler()
        ]
    )

    try:
        main()
    except Exception as e:
        logging.exception(e)