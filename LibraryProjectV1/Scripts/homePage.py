import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
class HomePage(QWidget):

    def __init__(self, parent=None):
        super(HomePage, self).__init__(parent)
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):

        self.hello_message = QLabel("""
            Hello, this is my first ui project. So it could be little absurd. Also I'm doing it with Python.
            Do not get me wrong but making a user interface with Python, it's kinda lame. There are so powerful tools for this job.
            However, in the end of the day they all have the same logic. If you make a bread with wheat flour. 
            Then you can make a bread with rye flour too. 
        """)
        self.hello_message.setAlignment(Qt.AlignCenter)
        self.hello_message.setFont(QFont('Arial',25))

        self.add_book = QPushButton("Add A Book")
        self.delete_book = QPushButton("Delete A Book")
        self.list_of_books = QPushButton("List of Books")
        self.query_book = QPushButton("Search For A Book")
        self.total_pages = QPushButton("Calculate How Many Page You Read")
        self.eraseData = QPushButton("Erase Database")
        self.logOut = QPushButton("Log Out")

        v_box = QVBoxLayout()
        v_box.addWidget(self.hello_message)
        v_box.addWidget(self.add_book)
        v_box.addWidget(self.delete_book)
        v_box.addWidget(self.list_of_books)
        v_box.addWidget(self.query_book)
        v_box.addWidget(self.total_pages)
        v_box.addWidget(self.eraseData)
        v_box.addWidget(self.logOut)

        self.setLayout(v_box)
        self.setWindowTitle("Homepage")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    homepage = HomePage()
    sys.exit(app.exec_())
