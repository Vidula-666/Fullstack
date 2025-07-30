import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
        self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        hbox=QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        central_widget.setLayout(hbox)

if __name__ == 'main__':
        app=QApplication(sys.argv)
        window= MainWindow()
        window.show()
        sys.exit(app.exec_())

