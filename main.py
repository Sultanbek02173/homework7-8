from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QTableWidget, QTableWidgetItem, QGridLayout
from PyQt5.QtCore import QSize, Qt
from PyQt5.uic import loadUi
import sys 
import sqlite3

connect = sqlite3.connect('dodo_pizza.db')
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    surname VARCHAR(255),
    number VARCHAR(255),
    address VARCHAR(255),
    food VARCHAR(255)
    );
    """)    
connect.commit()


class MenuWindow(QWidget):
    def __init__(self):
        super(MenuWindow, self).__init__()
        loadUi('menu.ui', self)
        # print("Ok")
        self.pizza_window = PizzaWindow()
        self.pizza.clicked.connect(self.show_pizza_window)
        self.dessert_window = DessertWindow()
        self.desserts.clicked.connect(self.show_dessert_window)
        self.drinks_window = DrinksWindow()
        self.drinks.clicked.connect(self.show_drinks_window)


    def show_pizza_window(self):
        self.pizza_window.show()

    def show_dessert_window(self):
        self.dessert_window.show()

    def show_drinks_window(self):
        self.drinks_window.show()

class PizzaWindow(QWidget):
    def __init__(self):
        super(PizzaWindow, self).__init__()
        loadUi('pizza.ui', self)

class DessertWindow(QWidget):
    def __init__(self):
        super(DessertWindow, self).__init__()
        loadUi('desserts.ui', self)

class DrinksWindow(QWidget):
    def __init__(self):
        super(DrinksWindow, self).__init__()
        loadUi('drinks.ui', self)

class AdminWindow(QWidget):
    def __init__(self):
        super(AdminWindow, self).__init__()
        loadUi('admin.ui', self)
        self.confirm.clicked.connect(self.check_password)
        self.database_window = DatabaseWindow()


    def check_password(self):
        get_password = self.password.text()
        if get_password == "geeks":
            self.result.setText("Good")
            self.result.setStyleSheet("QLabel {""color:rgb(225, 225, 225);""}")
            self.database_window.show()
        else:
            self.result.setText("Incorrect")
            self.result.setStyleSheet("QLabel {""color:rgb(225, 0, 0);""}")


class DatabaseWindow(QWidget):
    def __init__(self):
        super(DatabaseWindow, self).__init__()
        loadUi('database.ui', self)

        sqlite_select_query = """SELECT id from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        num = len(records)
        connect.commit()

        # self.setMinimumSize(QSize(480, 80))         # Set sizes 
        # self.setWindowTitle("Работа с QTableWidget")    # Set the window title
        # central_widget = QWidget(self)              # Create a central widget
        # self.setCentralWidget(central_widget)       # Install the central widget
 
        grid_layout = QGridLayout(self)         # Create QGridLayout
        # central_widget.setLayout(grid_layout)   # Set this layout in central widget
 
        table = QTableWidget(self)  # Create a table
        table.setColumnCount(5)     #Set three columns
        table.setRowCount(num)        # and one row
 
        # Set the table headers
        table.setHorizontalHeaderLabels(["Имя", "Фамилия", "Номер", "Адрес", "Еда"])
 
        #Set the tooltips to headings
        table.horizontalHeaderItem(0).setToolTip("Column 1 ")
        table.horizontalHeaderItem(1).setToolTip("Column 2 ")
        table.horizontalHeaderItem(2).setToolTip("Column 3 ")
        table.horizontalHeaderItem(3).setToolTip("Column 4 ")
        table.horizontalHeaderItem(4).setToolTip("Column 5 ")

 
        # Set the alignment to the headers
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(3).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(4).setTextAlignment(Qt.AlignHCenter)

        sqlite_select_query = """SELECT name from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        rec = list(records)
        for i in range(len(rec)):
            print(i, type(str(rec[i])))
            table.setItem(i, 0, QTableWidgetItem(str(rec[i])))
        connect.commit()

        sqlite_select_query = """SELECT surname from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        rec = list(records)
        for i in range(len(rec)):
            print(i, type(str(rec[i])))
            table.setItem(i, 1, QTableWidgetItem(str(rec[i])))
      
        connect.commit()

        sqlite_select_query = """SELECT number from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        rec = list(records)
        for i in range(len(rec)):
            print(i, type(str(rec[i])))
            table.setItem(i, 2, QTableWidgetItem(str(rec[i])))
             
        connect.commit()

        sqlite_select_query = """SELECT address from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        rec = list(records)
        for i in range(len(rec)):
            print(i, type(str(rec[i])))
            table.setItem(i, 3, QTableWidgetItem(str(rec[i])))
             
        connect.commit()

        sqlite_select_query = """SELECT food from orders"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        rec = list(records)
        for i in range(len(rec)):
            print(i, type(str(rec[i])))
            table.setItem(i, 4, QTableWidgetItem(str(rec[i])))
                   
        connect.commit()


        # Fill the first line

 
        # Do the resize of the columns by content
        table.resizeColumnsToContents()
 
        grid_layout.addWidget(table, 0, 0)   # Adding the table to the grid

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi('main.ui', self)
        self.menu_window = MenuWindow()
        self.admin_window = AdminWindow()
        self.hide_input_order()
        self.order.clicked.connect(self.show_input_order)
        self.send.clicked.connect(self.send_order)
        self.menu.clicked.connect(self.show_menu_window)
        self.admin.clicked.connect(self.show_admin_window)



    def show_menu_window(self):
        self.menu_window.show()

    def show_admin_window(self):
        self.admin_window.show()

    def hide_input_order(self):
        self.name.hide()
        self.surname.hide()
        self.number.hide()
        self.address.hide()
        self.food.hide()
        self.send.hide()

    def show_input_order(self):
        self.name.show()
        self.surname.show()
        self.number.show()
        self.address.show()
        self.food.show()
        self.send.show()

    def send_order(self):
        self.show_input_order()
        get_name = self.name.text()
        get_surname = self.surname.text()
        get_number = self.number.text()
        get_address = self.address.text()
        get_food = self.food.text()
        cursor.execute(f"""INSERT INTO orders (name, surname, number, address, food) VALUES ('{get_name}', '{get_surname}', '{get_number}','{get_address}', '{get_food}')""")
        connect.commit()

        

        print(get_name, get_surname, get_number, get_address, get_food)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()