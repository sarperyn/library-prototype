from library import Library
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont



class DeleteBook(QWidget):

    def __init__(self,parent=None):

        super(DeleteBook,self).__init__(parent)
        self.library = Library()
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):

        self.textField = QLabel("Book Name")
        self.textField.setAlignment(Qt.AlignCenter)
        self.textField.setFont(QFont('Arial',25))
        self.book = QLineEdit()
        self.delete = QPushButton("Delete")
        self.back   = QPushButton("Back to Menu")

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.textField)
        v_box.addWidget(self.book)
        v_box.addWidget(self.delete)
        v_box.addWidget(self.back)
        v_box.addStretch()

        self.setLayout(v_box)
        self.delete.clicked.connect(self.delete_book)
        self.setWindowTitle("Delete")

    def delete_book(self):
        book = self.book.text()
        self.library.delete_book(name=book) 
        self.book.clear()
        self.setGeometry(100,100,1280,837)
