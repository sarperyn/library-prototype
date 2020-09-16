import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from homePage import HomePage
from addBook import AddBook
from deleteBook import DeleteBook
from listAllBooks import ListAllBooks
from queryBook import  QueryBook
from calculatePages import CalculatePages
from eraseData import EraseData
from logIn import LogIn
from entry import Entry
from signUp import SignUp



class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self)
        self.setGeometry(100,100,1280,836)
        oImage = QImage("../Image/schoolOfAtheneV2.jpg")
        sImage = oImage.scaled(QSize(1280,836))                   # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))                        
        self.setPalette(palette) 
        self.init_ui()

    def init_ui(self):
        self.window = Entry()
        self.window.setGeometry(600,300,1280,836)
        self.setCentralWidget(self.window)
        self.window.login.clicked.connect(self.login)
        self.window.signup.clicked.connect(self.signup)

    def main(self):
        self.window = HomePage()
        self.window.setGeometry(600,300,1280,836)
        self.setCentralWidget(self.window)
        self.window.add_book.clicked.connect(self.addingBook)
        self.window.delete_book.clicked.connect(self.deleteBook)
        self.window.list_of_books.clicked.connect(self.listAllBooks)
        self.window.query_book.clicked.connect(self.searchBook)
        self.window.total_pages.clicked.connect(self.sumPages)
        self.window.eraseData.clicked.connect(self.eraseData)
        self.window.logOut.clicked.connect(self.logOut)


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

    def eraseData(self):
        self.window = EraseData()
        self.setCentralWidget(self.window)
        self.window.no.clicked.connect(self.back)
        self.window.back.clicked.connect(self.back)
    
    def login(self):
        self.window = LogIn()
        self.setCentralWidget(self.window)
        self.window.logIn.clicked.connect(self.wayToMainPage)
        self.window.back.clicked.connect(self.backToEntracePage)

    def signup(self):
        self.window = SignUp()
        self.setCentralWidget(self.window)
        self.window.signUp.clicked.connect(self.accountCreate)
        self.window.back.clicked.connect(self.backToEntracePage)

    def accountCreate(self):
        username = self.window.usernameField.text()
        password = self.window.passwordField.text()

        self.window.cursor.execute("INSERT INTO Members Values(?,?)",(username,password))
        self.window.connection.commit()
        self.init_ui()

    def wayToMainPage(self):
        username = self.window.usernameField.text()
        password = self.window.passwordField.text()

        self.window.cursor.execute("SELECT * FROM Members WHERE username = ? and password = ?",(username,password))

        data = self.window.cursor.fetchall()
    
        if len(data) == 0:
            self.window.textField.setText("We couldn't find you\nMake sure your username and password are correct.")
        else:
            self.main()

    def logOut(self):
        self.init_ui()


    def back(self):
        self.main()

    def backToEntracePage(self):
        self.init_ui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())