import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush
from homePage import HomePage
from addBook import AddBook
from deleteBook import DeleteBook
from listAllBooks import ListAllBooks
from queryBook import  QueryBook
from calculatePages import CalculatePages



class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.setGeometry(100,100,1280,836)
        oImage = QImage("../Image/schoolOfAthene.jpg")
        sImage = oImage.scaled(QSize(1280,836))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette) 
                        
        self.init_ui()
        
    
    def init_ui(self):
        self.window = HomePage()
        self.window.setGeometry(600,300,1280,836)
        self.setCentralWidget(self.window)
        self.window.add_book.clicked.connect(self.addingBook)
        self.window.delete_book.clicked.connect(self.deleteBook)
        self.window.list_of_books.clicked.connect(self.listAllBooks)
        self.window.query_book.clicked.connect(self.searchBook)
        self.window.total_pages.clicked.connect(self.sumPages)



    def addingBook(self):
        self.window = AddBook()
        self.setCentralWidget(self.window)
        self.window.back.clicked.connect(self.back)    

    def deleteBook(self):
        self.window = DeleteBook()
        self.setCentralWidget(self.window)
        self.window.back.clicked.connect(self.back)


    def listAllBooks(self):
        self.window = ListAllBooks()
        self.setCentralWidget(self.window)
        self.window.back.clicked.connect(self.back)


    def searchBook(self):
        self.window = QueryBook()
        self.setCentralWidget(self.window)
        self.window.back.clicked.connect(self.back)

    def sumPages(self):
        self.window = CalculatePages()
        self.setCentralWidget(self.window)
        self.window.back.clicked.connect(self.back)

    def back(self):
        self.init_ui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())