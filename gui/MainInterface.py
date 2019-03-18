import sys
import calendar
from Prompt import Prompt
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class MainInterface(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'ICSPS Scheduler'
        self.month = None
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100

        self.initializeInterface()

        #self.prompt = Prompt(self, "test", "test")

    def initializeInterface(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setCentralWidget(self.horizontalGroupBox)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Month")
        layout = QGridLayout()
        # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        count = 1
        # for i in range(7):
        #     for j in range(5):
        #         layout.addWidget(QPushButton(str(count)+'\n'),i,j)
        #         count += 1
        #sundayLabel = QLabel("Sunday", self)
        layout.addWidget(QLabel("Sunday"), 0,1)
        layout.addWidget(QLabel("Requests"), 0,0)
        for i in range(5):
            for j in range(7):
                layout.addWidget(QPushButton(str(count)+'\n'),i+1,j+1)
                count += 1


        widgets = (layout.itemAt(i).widget() for i in range(layout.count()))
        # for w in widgets:
        #     if isinstance(w, QPushButton):
        #         #print(w.objectName(),w.text())

        self.horizontalGroupBox.setLayout(layout)

app = QApplication(sys.argv)
window = MainInterface()
sys.exit(app.exec_())
