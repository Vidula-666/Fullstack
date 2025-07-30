import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt

class To_do_List(QWidget):
    def __init__(self):
        super().__init__()
        self.search_input=QLineEdit(self)
        self.search_input.setPlaceholderText("Enter the username to load tasks:")
        self.search_button=QPushButton("Search",self)
        self.todo_title = QLabel("")
        self.task_display_label = QLabel("")
        self.task_input = QLineEdit(self)
        self.task_input.hide() 
        self.add_task_button = QPushButton("Add Task", self)
        self.add_task_button.hide()  
        self.delete_input = QLineEdit(self) 
        self.delete_input.setPlaceholderText("Enter task number to delete")
        self.delete_input.hide()

        self.delete_task_button = QPushButton("Delete Task", self)
        self.delete_task_button.hide()

        self.initUI()
    
    def initUI(self):

        self.users = {}
        self.current_user = None

        vbox=QVBoxLayout()

        
        vbox.addWidget(self.search_input)
        vbox.addWidget(self.search_button)
        vbox.addWidget(self.todo_title)
        vbox.addWidget(self.task_display_label)
        vbox.addWidget(self.task_input)
        vbox.addWidget(self.add_task_button)
        vbox.addWidget(self.delete_input)
        vbox.addWidget(self.delete_task_button)

        self.setLayout(vbox)

        self.search_input.setAlignment(Qt.AlignCenter)
        self.search_input.setObjectName("search_input")
        self.task_input.setAlignment(Qt.AlignCenter)
        self.todo_title.setAlignment(Qt.AlignCenter)
        self.task_display_label.setAlignment(Qt.AlignCenter)

        self.search_input.setObjectName("search_input")
        self.todo_title.setObjectName("todo_title")
        self.task_display_label.setObjectName("task_display_label")
        self.task_input.setObjectName("task_input")

        self.setStyleSheet("""
                           QWidget {
                           background-color: #f5f5f5}
                           QLabel,QPushButton{font-family:calibri;
                           padding:10px}
                           QLineEdit#search_input {
                           font-size: 40px;
                           border: 1px solid gray;
                           border-radius: 5px;
                           padding: 5px;
                           }
                           QLineEdit#task_input {
                           font-size: 30px;
                           border: 1px solid gray;
                           border-radius: 5px;
                           padding: 5px;
                           }
                           QPushButton {
                           font-size: 30px;
                           font-weight: bold;
                           background-color: #0066cc;
                           color: white;
                           border-radius: 10px;
                           }
                           QPushButton:hover {
                           background-color: #004c99;
                           }
                           QLabel#todo_title{
                           font-size:75px;}
                           QLabel#task_display_label{
                           font-size:50px;
                           font-family: Consolas;}
""")
        
        self.add_task_button.clicked.connect(self.add_task)
        self.search_button.clicked.connect(self.search_user)
        self.delete_task_button.clicked.connect(self.delete_task)


    def add_task(self):
        task = self.task_input.text().strip()
        if task and self.current_user:
            self.users[self.current_user].append(task)
            self.display_tasks()
            self.task_input.clear()

    def search_user(self):
        name = self.search_input.text().strip().lower()
        self.current_user = name
        if name not in self.users:
            self.users[name] = []

            self.todo_title.setText(f"{name.title()}'s TO-DO LISTS")
            self.task_input.show()
            self.add_task_button.show()
            self.delete_input.show()
            self.delete_task_button.show()
            self.display_tasks()


    def display_tasks(self):
        tasks = self.users[self.current_user]
        formatted_task = ""
        for i, t in enumerate(tasks, 1):
            formatted_task += f"{i}. {t}\n"
        self.task_display_label.setText(formatted_task)


    def delete_task(self):
         if self.current_user:
            try:
                index = int(self.delete_input.text()) - 1
                if 0 <= index < len(self.users[self.current_user]):
                    del self.users[self.current_user][index]
                    self.display_tasks()
                    self.delete_input.clear()
                else:
                    self.todo_title.setText("Invalid Task Number")
            except ValueError:
                self.todo_title.setText("Enter a valid number")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = To_do_List()
    window.show()
    sys.exit(app.exec_())    