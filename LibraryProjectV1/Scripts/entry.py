import sqlite3
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont




class Entry(QWidget):

    def __init__(self):

        super(Entry, self).__init__()
        self.make_connection()
        self.init_ui()

    def make_connection(self):

        self.connection = sqlite3.connect("../Database/Database.db")

        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS Members(username TEXT,password TEXT)"

        self.cursor.execute(query)
        self.connection.commit()

    def disconnect(self):
        
        self.connection.close()

    def init_ui(self):
        
        self.text = QLabel("""
        WELCOME TO THE LIBRARY APP!
        """)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setFont(QFont('Arial',40))

        self.login = QPushButton("Login")
        self.signup = QPushButton("Signup")

        v_box = QVBoxLayout()
        v_box.addWidget(self.text)
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.login)
        h_box.addWidget(self.signup)

        main_box = QVBoxLayout()
        main_box.addLayout(v_box)
        main_box.addLayout(h_box)

        self.setLayout(main_box)
        self.setWindowTitle("Welcome")
        

        

        