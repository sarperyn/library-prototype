from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit, QTableView, QDialog
from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5 import QtSql, QtCore

#List of the books
class ListAllBooks(QWidget):

    def __init__(self,parent=None):

        super(ListAllBooks,self).__init__(parent)
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):
        

        self.listAllBooks = QPushButton("List All Books")
        self.back = QPushButton("Back to Menu")

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.listAllBooks)
        v_box.addStretch()
        v_box.addWidget(self.back)
    

        self.setLayout(v_box)
        self.listAllBooks.clicked.connect(self.listbooks)
        self.setWindowTitle("Book's List")

    #Initialize the page which we created for the books list
    def initializeModel(self,model):
        self.model.setTable('Library')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "    Author Name    ")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "    Book Name    ")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "    Total Pages    ")
    
    #Creating the book's list page
    def createView(self,title, model):
        self.view = QTableView()
        self.view.setModel(model)
        self.view.setWindowTitle(title)
        return self.view


    #Button's function that lead us to book's list
    def listbooks(self):
        
        #Connecting our database
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('../DataBase/Library.db')

        #Sending our query
        self.query = QtSql.QSqlQuery()
        self.query.exec_("SELECT * FROM Library")
        self.model = QtSql.QSqlTableModel()

        self.initializeModel(self.model)
        self.view = self.createView("Table Model",model=self.model)

        self.dlg = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.view)

        self.dlg.setLayout(self.layout)
        self.dlg.setWindowTitle("Books List")
        self.dlg.setGeometry(600,300,400,400)
        self.dlg.show()