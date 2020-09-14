from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTextEdit
from PyQt5.QtWidgets import QApplication, QLineEdit, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from library import Library


#Search a book and get the books data
class QueryBook(QWidget):

    def __init__(self, parent=None):

        super(QueryBook,self).__init__(parent)
        self.library = Library()
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):

        self.textField = QLabel("Book Name")
        self.textField.setAlignment(Qt.AlignCenter)
        self.textField.setFont(QFont('Arial',25))
        self.book  = QLineEdit()
        self.query = QPushButton("Query")
        self.back   = QPushButton("Back to Menu")
        self.result = QLabel()
        self.information = QLabel()

        #Creating vertical box to put widgets in
        v_box1 = QVBoxLayout()
        v_box1.addStretch()
        v_box1.addWidget(self.textField)
        v_box1.addWidget(self.book)
        v_box1.addWidget(self.query)
        v_box1.addStretch()
        
        #Creating vertical box to put widgets in
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.result)
        v_box2.addStretch()
        v_box2.addWidget(self.information)
        v_box2.addWidget(self.back)
        v_box2.addStretch()

        #Creating Vertical Box for other vertical boxes to put them in
        v_box3 = QVBoxLayout()
        v_box3.addLayout(v_box1)
        v_box3.addLayout(v_box2)


        #Inserting the main vertical box to the main window
        self.setLayout(v_box3)
        self.query.clicked.connect(self.query_book)
        self.setWindowTitle("Book")

    # Get the books datas
    def query_book(self):

        self.output = self.library.search_book(name=self.book.text())
        
        self.result.setText(f"""
        Author              : {self.output[0][0]}
        Name               : {self.output[0][1]}
        Total Pages      :  {self.output[0][2]}        
        
        """)
        self.result.setFont(QFont('Arial',20))
        self.information.setText("""
        The main purpose of this part of the program is summarize the book. 
        This place will be replaced with the book's summary in the real version of the program""")







        
        
        
        