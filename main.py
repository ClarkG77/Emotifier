import sys, logging
from datetime import datetime
from ibm_cloud_sdk_core.api_exception import ApiException
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QPushButton, QLineEdit, 
    QScrollArea, QVBoxLayout, QApplication, QSizePolicy, QComboBox, QSpinBox, QCheckBox, QTextEdit,QTextBrowser)
from PyQt5.QtGui import QPixmap, QMovie, QPixmapCache

class MainWindow(QMainWindow):
    def __init__(self, app, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mainApp = app
        self.load_main_ui()

    def load_main_ui(self):
            logging.info("Loading main ui")
            uic.loadUi('ui/Emotifier.ui', self)


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