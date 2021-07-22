
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(r"C:\Users\arunkumar.j06\Desktop\ContactBook.ui", self)

        #self.path()
        self.show()

    def path(self):
        self.controls = QWidget()  # Controls container widget.
        self.controlsLayout = QVBoxLayout()  # Controls container layout.

        # List of names, widgets are stored in a dictionary by these keys.
        widget_names = [
            "Heater", "Stove", "Living Room Light", "Balcony Light",
            "Fan", "Room Light", "Oven", "Desk Light",
            "Bedroom Heater", "Wall Switch"
        ]
        self.widgets = []

        # Iterate the names, creating a new OnOffWidget for
        # each one, adding it to the layout and
        # and storing a reference in the `self.widgets` dict
        for name in widget_names:
            item = QLabel(name)
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)

        # Scroll Area Properties.
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        # Search bar.
        self.searchbar = QLineEdit()
        self.searchbar.textChanged.connect(self.update_display)

        # Adding Completer.
        self.completer = QCompleter(widget_names)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)

        # Add the items to VBoxLayout (applied to container widget)
        # which encompasses the whole window.
        container = QWidget()
        containerLayout = QVBoxLayout()
        containerLayout.addWidget(self.searchbar)
        containerLayout.addWidget(self.scroll)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Control Panel')


    def update_display(self, text):
        for widget in self.widgets:
            if text.lower() in widget.name.lower():
                widget.show()
            else:
                widget.hide()


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()

'''
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Contacts")

        # setting geometry
        self.setGeometry(200, 200, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    def UiComponents(self):
        # creating head label
        head = QLabel("Contact Book", self)
        name = QLabel("Name ", self)
        namef = QLineEdit(self)
        surname = QLabel("Surname ", self)
        surnamef = QLineEdit(self)
        phone = QLabel("Phone ", self)
        phonef = QLineEdit(self)
        mobile = QLabel("Mobile ", self)
        mobilef = QLineEdit(self)
        address = QLabel("Address ", self)
        addressf = QLineEdit(self)
        email = QLabel("Email ", self)
        emailf = QLineEdit(self)
        github = QLabel("Github ", self)
        githubf = QLineEdit(self)
        insta = QLabel("Instagram Id ", self)
        instaf = QLineEdit(self)
        twitter = QLabel("Twitter Id ",self)
        twitterf = QLineEdit(self)
        fb = QLabel("Facebook Id ", self)
        fbf = QLineEdit(self)

        # setting geometry to the head
        head.setGeometry(270, 7, 200, 20)
        name.setGeometry(30, 40, 60, 20)
        namef.setGeometry(130, 40, 100, 20)
        surname.setGeometry(30, 70, 60, 20)
        surnamef.setGeometry(130, 70, 100, 20)
        phone.setGeometry(30, 100, 60, 20)
        phonef.setGeometry(130, 100, 100, 20)
        mobile.setGeometry(30, 130, 60, 20)
        mobilef.setGeometry(130, 130, 100, 20)
        address.setGeometry(30, 160, 60, 20)
        addressf.setGeometry(130, 160, 100, 20)
        email.setGeometry(30, 190, 60, 20)
        emailf.setGeometry(130, 190, 100, 20)
        github.setGeometry(30, 220, 60, 20)
        githubf.setGeometry(130, 220, 100, 20)
        insta.setGeometry(30, 250, 70, 20)
        instaf.setGeometry(130, 250, 100, 20)
        twitter.setGeometry(30, 280, 60, 20)
        twitterf.setGeometry(130, 280, 100, 20)
        fb.setGeometry(30, 310, 60, 20)
        fbf.setGeometry(130, 310, 100, 20)

        # font
        font = QFont('Times', 14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # setting font to the head
        head.setFont(font)

        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)

        # setting color effect to the head
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.darkCyan)
        head.setGraphicsEffect(color)


# create pyqt5 app
App = QApplication(sys.argv)
App.setStyle('Fusion')

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

'''