from library import *
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from time import sleep


class EraseData(QWidget):

    def __init__(self,parent=None):

        super(EraseData,self).__init__(parent)
        self.library = Library()
        self.init_ui()

    
    def init_ui(self):

        
        self.textField = QLabel("Are you really sure about this?")
        self.textField.setAlignment(Qt.AlignCenter)
        self.textField.setFont(QFont('Arial',25))
        self.yes = QPushButton("Yes")
        self.no  = QPushButton("No")
        self.back = QPushButton("Back to Menu")
        self.message = QLabel()
        self.message.setAlignment(Qt.AlignCenter)
        self.message.setFont(QFont('Arial',20))
        self.lastMessage = QLabel()


        v_box = QVBoxLayout()
        v_box.addWidget(self.textField)
        
        h_box = QHBoxLayout()
        h_box.addWidget(self.yes)
        h_box.addWidget(self.no)


        self.v_box2 = QVBoxLayout()
        self.v_box2.addStretch()
        self.v_box2.addLayout(v_box)
        self.v_box2.addLayout(h_box)
        self.v_box2.addWidget(self.message)
        self.v_box2.addStretch()
        


        self.setLayout(self.v_box2)
        self.setWindowTitle("Erase Data")
        self.yes.clicked.connect(self.erase)
        

    def erase(self):
        self.message.setText("A message has received from the database. Do you want to open it?")
        self.yes2 = QPushButton("Yeah, why not?")
        self.no2  = QPushButton("Nah, keep erasing...")
        self.v_box2.addWidget(self.yes2)
        self.v_box2.addWidget(self.no2)
        self.v_box2.addStretch()
        self.yes2.clicked.connect(self.sokrates)
        self.no2.clicked.connect(self.justno)
        self.yes.close()
        self.no.close()
        self.textField.clear()
        self.setGeometry(100,100,1280,838)

    def sokrates(self):
        self.message.setText("""
        True wisdom comes to each of us when we realize
        how little we understand about life, ourselves and
        the world around us.
        May we meet again.
        """)
        self.library.erase_data()
        self.lastMessage.setText("Datas have been deleted")
        self.lastMessage.setAlignment(Qt.AlignCenter)
        self.lastMessage.setFont(QFont('Arial',25))
        self.v_box2.addWidget(self.lastMessage)
        self.v_box2.addWidget(self.back)
        self.yes2.close()
        self.no2.close()
        self.setGeometry(100,100,1281,838)

    def justno(self):

        self.library.erase_data()
        self.lastMessage.setText("Datas have been deleted")
        self.v_box2.addStretch()
        self.lastMessage.setAlignment(Qt.AlignCenter)
        self.lastMessage.setFont(QFont('Arial',25))
        self.v_box2.addWidget(self.lastMessage)
        self.v_box2.addWidget(self.back)
        self.yes2.close()
        self.no2.close()
        self.message.clear()
        self.setGeometry(100,100,1281,838)

        


    
        



        


