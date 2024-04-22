from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMessageBox, QPushButton , QDialog , QHBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import sys



class ResultWindow(QDialog):
    def __init__(self , label , prob,model_type ):
        super().__init__()
        self.title = "Result"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 400
        self.button_Test_again = QPushButton("Test Again", self)
        self.button_quit = QPushButton("Quit", self)
        label = label
        prob = prob
        self.model_type = model_type
        self.init_window(label , prob)
    def init_window(self,label , prob):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon("icons8-cbs-512.ico"))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        m = PlotCanvas(self, width=5, height=4, dpi=80,label=label ,prob=prob)
        m.move(0,0)

        self.button_Test_again.setToolTip("<h5>To test Another image just Click Test button<h5>")
        self.button_Test_again.setIcon(QtGui.QIcon("698827-icon-101-folder-search-512.png"))
        self.button_Test_again.setIconSize(QtCore.QSize(15, 15))
        self.button_Test_again.clicked.connect(self.test_again)
        hbox.addWidget(self.button_Test_again)

        self.button_quit.setToolTip("<h5>Close the program<h5>")
        self.button_quit.setIcon(QtGui.QIcon("cancel-symbol-transparent-9.png"))
        self.button_quit.setIconSize(QtCore.QSize(15, 15))
        self.button_quit.clicked.connect(self.close_main_window)
        hbox.addWidget(self.button_quit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.show()

    def test_again(self):
        from Test_window_Final import Test_window
        self.Main_window = Test_window()
        self.Main_window.show()
        self.close()

    def close_main_window(self):
        """
           Generate 'question' dialog on clicking 'X' button in title bar.
           Reimplement the closeEvent() event handler to include a 'Question'
           dialog with options on how to proceed - Save, Close, Cancel buttons
        """
        reply = QMessageBox.question(self, "Quit", "Are you sure you want to quit?",
                                     QMessageBox.Cancel | QMessageBox.Close)

        if reply == QMessageBox.Close:
            self.close()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=80 , label = "Forged" , prob = 0.1, model_type="VGG16"):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.label = label
        self.prob = prob
        self.model_type = model_type
        self.plotpie(self.label , self.prob , self.model_type)

    def plotpie(self, label, prob, model_type):
        ax = self.figure.add_subplot(111)
        if model_type == "Error Level Analysis":
            if label == "Forged":
                labels = ["Forged", "Not Forged"]
                colors = ['red', 'blue']
                ax.text(0.25, 0.95, f'Decision: {label}', transform=ax.transAxes)
                ax.axis("equal")
                ax.pie([prob, 1 - prob], autopct='%1.1f%%', shadow=True, colors=colors, radius=1, counterclock=True)
               # ax.legend(labels, loc='upper right')
                self.draw()
            elif label == "Not_Forged":
                labels = ["Not Forged", "Forged"]
                colors = ['blue', 'red']
                ax.text(0.25, 0.95, f'Decision: {label}', transform=ax.transAxes)
                ax.axis("equal")
                ax.pie([1 - prob, prob], autopct='%1.1f%%', shadow=True, colors=colors, radius=1, counterclock=True)
               # ax.legend(labels, loc='upper right')
                self.draw()
        elif model_type in ["VGG16", "VGG19"]:
            if label == "Forged":
                labels = ["Forged", "Not Forged"]
                probs = [1-prob, prob]
                colors = ['red', 'blue']  # Correct colors for VGG models
                ax.text(0.25, 0.95, f'Decision: {label}', transform=ax.transAxes)
                ax.axis("equal")
                ax.pie(probs, autopct='%1.1f%%', shadow=True, colors=colors, radius=1, counterclock=True)
                #ax.legend(labels, loc='upper right')
                self.draw()
            elif label == "Not_Forged":
                labels = ["Not Forged", "Forged"]
                probs = [ prob,1- prob]
                colors = ['blue', 'red']  # Correct colors for VGG models
                ax.text(0.25, 0.95, f'Decision: {label}', transform=ax.transAxes)
                ax.axis("equal")
                ax.pie(probs, autopct='%1.1f%%', shadow=True, colors=colors, radius=1, counterclock=True)
                #ax.legend(labels, loc='upper right')
                self.draw()








if __name__ == "__main__":
    App = QApplication(sys.argv)
    App.setStyle('Fusion')
    window = ResultWindow(label = "Test" , prob = 50)
    sys.exit(App.exec())