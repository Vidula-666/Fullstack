import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(0,0,500,500)
        label=QLabel("Vidula",self)
        label.setFont(QFont("Arial",40))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color:blue;"
                            "background-color:pink;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;")
        #label.setAlignment(Qt.AlignTop)
        #label.setAlignment(Qt.AlignBottom)
        #label.setAlignment(Qt.AlignCenter)
        #label.setAlignment(Qt.AlignVCenter)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()


