import sys, logging
from datetime import datetime
from matplotlib import pyplot as pp
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QPixmap
import tkinter as tk
from tkinter import filedialog
from PyQt5.QtWidgets import (QCheckBox, QLabel, QLineEdit, QMainWindow, QPushButton, QApplication)
import pipeline


SAVEDFILENAME = 'modImages/temp.png'
SAVEDFILEPATH = 'modImages/temp.png'

class MainWindow(QMainWindow):
    def __init__(self, app, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mainApp = app
        self.filename = ""
        self.checkForeground = False
        self.load_main_ui()
        
        
    def load_main_ui(self):
        logging.info("Loading main ui")
        uic.loadUi('ui/Emotifier.ui', self)
        self.imageDisplayBox = self.findChild(QLabel,'displayBox')
        self.connect_buttons()
        self.pixelizeButton.setEnabled(False)
        self.cartoonButton.setEnabled(False)
        self.abstractButton.setEnabled(False)
        self.coordBox.setEnabled(False)
    def connect_buttons(self):
        self.pixelizeButton = self.findChild(QPushButton, 'pixilizeButton')
        self.pixelizeButton.clicked.connect(self.callPipelinePixelize)
        self.cartoonButton = self.findChild(QPushButton, 'cartoonButton')
        self.cartoonButton.clicked.connect(self.callPipelineCartoonify)
        self.abstractButton = self.findChild(QPushButton, 'abstractButton')
        self.abstractButton.clicked.connect(self.callPipelineAbstractify)
        
        self.foregroundDetectionCheckButton = self.findChild(QCheckBox, 'foregroundCheck')
        self.foregroundDetectionCheckButton.stateChanged.connect(self.toggle_foreground_check)
        self.coordBox = self.findChild(QLineEdit, 'coordinateEntryBox')
        
        self.uploadButton = self.findChild(QPushButton, 'uploadButton')
        self.uploadButton.clicked.connect(self.askForImg)
        self.ExitButton = self.findChild(QPushButton, 'ExitButton')
        self.ExitButton.clicked.connect(self.closeProgram)
        
    def toggle_foreground_check(self):
        if self.foregroundDetectionCheckButton.isChecked()==True:
            self.checkForeground = True
            self.coordBox.setEnabled(True)
        else:
            self.checkForeground = False
            self.coordBox.setEnabled(False)
            
    def closeProgram(self):
        exit()
    
    def getCoords(self):
        coords=[]
        coordString = self.coordBox.text()
        coordTuples = coordString.split(';')
        for coord in coordTuples:
            try:
                temp = coord.split(',')
                coords.append((int(temp[0]),int(temp[1])))
            except e:
                raise("Formatting Error")
        return coords
        
    def callPipelinePixelize(self):
        coords = []
        if self.checkForeground:
            coords = self.getCoords()
        pp.imsave(SAVEDFILEPATH,pipeline.emojiPipeline(self.filename,coords,'P',self.checkForeground,3),format = 'png')
        tempPix = QPixmap(SAVEDFILENAME)
        self.imageDisplayBox.setPixmap(tempPix.scaled(761, 331, QtCore.Qt.KeepAspectRatio))
        
    def callPipelineAbstractify(self):
        coords = []
        if self.checkForeground:
            coords = self.getCoords()
        pp.imsave(SAVEDFILEPATH,pipeline.emojiPipeline(self.filename,coords,'A',self.checkForeground,3))
        tempPix = QPixmap(SAVEDFILENAME)
        self.imageDisplayBox.setPixmap(tempPix.scaled(761, 331, QtCore.Qt.KeepAspectRatio))
        
    def callPipelineCartoonify(self):
        coords = []
        if self.checkForeground:
            coords = self.getCoords()
        pp.imsave(SAVEDFILEPATH,pipeline.emojiPipeline(self.filename,coords,'C',self.checkForeground,3))
        tempPix = QPixmap(SAVEDFILENAME)
        self.imageDisplayBox.setPixmap(tempPix.scaled(761, 331, QtCore.Qt.KeepAspectRatio))
        
    def askForImg(self):
        self.coordBox.clear()
        root = tk.Tk()
        root.withdraw()
        filetypes = (
            ('jpg files', '*.jpg'),('png files', '*.png'),('bmp files', '*.bmp'),
        )

        self.filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        if(self.filename.find('.jpg')>-1 or self.filename.find('.png')>-1 or self.filename.find('.bmp')>-1 or self.filename.find('.jpeg')>-1 ):
            self.pixelizeButton.setEnabled(True)
            self.cartoonButton.setEnabled(True)
            self.abstractButton.setEnabled(True)
            tempPix = QPixmap(self.filename)
            self.imageDisplayBox.setPixmap(tempPix.scaled(761, 331, QtCore.Qt.KeepAspectRatio))
        else:
            self.pixelizeButton.setEnabled(False)
            self.cartoonButton.setEnabled(False)
            self.abstractButton.setEnabled(False)

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