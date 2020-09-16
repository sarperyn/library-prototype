import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont


class SignUp(QWidget):

    def __init__(self):

        super().__init__()
        self.make_connection()
        self.init_ui()

    def make_connection(self):

        self.connection = sqlite3.connect("../Database/Database.db")

        self.cursor = self.connection.cursor()

    def init_ui(self):

        self.usernameText = QLabel("Username")
        self.usernameText.setFont(QFont('Arial',20))
        self.usernameField = QLineEdit()
        
        self.passwordText = QLabel("Password")
        self.passwordText.setFont(QFont('Arial',20))
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.Password)


        self.signUp = QPushButton("Sign up")
       

        self.back = QPushButton("Back to Menu")

        self.textField = QLabel()


        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.usernameText)
        v_box.addWidget(self.usernameField)
        v_box.addWidget(self.passwordText)
        v_box.addWidget(self.passwordField)
        v_box.addWidget(self.textField)
        v_box.addStretch()

        h_box = QHBoxLayout()
        h_box.addStretch()

        h_box.addWidget(self.signUp)
        h_box.addStretch()


        main_box = QVBoxLayout()
        main_box.addStretch()
        main_box.addLayout(v_box)
        main_box.addLayout(h_box)
        main_box.addStretch()
        main_box.addWidget(self.back)

        self.setLayout(main_box)
        self.setWindowTitle("Log in")

