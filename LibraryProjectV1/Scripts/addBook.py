from library import *
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class AddBook(QWidget):

    def __init__(self,parent=None):
        
        super(AddBook, self).__init__(parent)
        self.library = Library()
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):

        
        self.textField1 = QLabel("Author")
        self.textField1.setAlignment(Qt.AlignCenter)
        self.textField1.setFont(QFont('Arial',25))

        self.textField2 = QLabel("Book Name")
        self.textField2.setAlignment(Qt.AlignCenter)
        self.textField2.setFont(QFont('Arial',25))
        
        self.textField3 = QLabel("Total Pages")
        self.textField3.setAlignment(Qt.AlignCenter)
        self.textField3.setFont(QFont('Arial',25))

        self.author = QLineEdit()
        self.book   = QLineEdit()
        self.total_pages = QLineEdit()

        self.save = QPushButton("Save")
        self.back = QPushButton("Back to Menu")
        
        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.textField1)
        h_box1.addWidget(self.textField2)
        h_box1.addWidget(self.textField3)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.author)
        h_box2.addWidget(self.book)
        h_box2.addWidget(self.total_pages)

        h_box3 = QHBoxLayout()
        h_box3.addWidget(self.save)

        h_box4 = QHBoxLayout()
        h_box4.addWidget(self.back)

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addLayout(h_box4)
        v_box.addStretch()


        self.setLayout(v_box)
        self.save.clicked.connect(self.save_book)
        
        self.setWindowTitle("Add Book")
        self.show()
        

    def save_book(self):
        author = self.author.text()
        book   = self.book.text()
        total_pages = self.total_pages.text()

        book = Book(author=author,name=book,totalpages=total_pages)

        self.library.add_book(book=book)
        self.author.clear()
        self.book.clear()
        self.total_pages.clear()
        self.setGeometry(100,100,1280,835)

