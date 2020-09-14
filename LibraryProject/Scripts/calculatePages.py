from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from library import Library





class CalculatePages(QWidget):

    def __init__(self, parent=None):

        super(CalculatePages, self).__init__(parent)
        self.library = Library()
        self.init_ui()

    #Initialize the user interface
    def init_ui(self):
        self.sum = self.library.sum_of_pages()
        self.textField = QLabel(f"You have read {self.sum} page until this time")
        self.textField.setAlignment(Qt.AlignCenter)
        self.textField.setFont(QFont('Arial',50))
        self.back = QPushButton("Back to Menu")

        v_box = QVBoxLayout()
        v_box.addStretch()
        v_box.addWidget(self.textField)
        v_box.addStretch()
        v_box.addWidget(self.back)

        self.setLayout(v_box)
        self.setWindowTitle("Total Pages")

