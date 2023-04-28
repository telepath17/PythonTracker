import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6 import QtCore
from PySide6 import QtGui
import pickle

from ui_main_window import Ui_MainWindow
from ui_new_transaction_window import Ui_Dialog
from ui_new_category import Ui_Dialog2

class PythonTracker(QMainWindow):
    def __init__(self):
        super(PythonTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.new_window = None

        self.default_categories = [Category("Немає категорії"), Category("Продукти харчування"), Category("Морозиво")]

        self.categories = []
        filename = 'categories.pickle'
        try:
            with open(filename, 'rb') as f:
                self.categories = pickle.load(f)
        except FileNotFoundError:
            self.categories = self.default_categories
            pass

        self.transactions = []
        filename = 'transactions.pickle'
        try:
            with open(filename, 'rb') as f:
                self.transactions = pickle.load(f)
        except FileNotFoundError:
            pass

        self.ui.comboBox.addItem("Усі категорії")
        for category in self.categories:
            self.ui.comboBox.addItem(category.name)

        self.transactions_table = QtGui.QStandardItemModel()
        self.transactions_table.setHorizontalHeaderLabels(['Name', 'Date', 'Sum', 'Category'])
        for transaction in self.transactions:
            row = [
                QtGui.QStandardItem(transaction.name),
                QtGui.QStandardItem(str(transaction.date)),
                QtGui.QStandardItem(str(transaction.sum)),
                QtGui.QStandardItem(transaction.category)
            ]
            self.transactions_table.appendRow(row)
        self.ui.tableView.setSortingEnabled(True)
        self.ui.tableView.setModel(self.transactions_table)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

        self.stats_table = QtGui.QStandardItemModel()
        self.stats_table.setHorizontalHeaderLabels(['Category Name', 'Total sum'])
        for category in self.categories:
            row = [
                QtGui.QStandardItem(category.name),
                QtGui.QStandardItem(str(category.total_sum))
            ]
            self.stats_table.appendRow(row)
        self.stats_table.sort(1, Qt.DescendingOrder)
        self.ui.tableView_2.setSortingEnabled(True)
        self.ui.tableView_2.setModel(self.stats_table)
        self.ui.tableView_2.horizontalHeader().setStretchLastSection(True)

        self.ui.pushButton.clicked.connect(self.open_new_transaction_window)
        self.ui.pushButton_2.clicked.connect(self.open_new_category_window)
        self.ui.pushButton_3.clicked.connect(self.delete_transaction)

        self.ui.comboBox.currentIndexChanged.connect(self.renew)
        self.closeEvent = self.save_changes

    def open_new_transaction_window(self):
        self.transaction_window = NewTransactionWindow(self.categories, self.transactions, parent=self)
        self.transaction_window.show()

    def open_new_category_window(self):
        self.category_window = NewCategoryWindow(parent=self)
        self.category_window.show()
        self.category_window.activateWindow()

    def delete_transaction(self):
        selected = self.ui.tableView.currentIndex().row()
        self.transactions.pop(selected)
        self.renew()

    def renew(self):
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Name', 'Date', 'Sum', 'Category'])
        for transaction in self.transactions:
            row = [
                QtGui.QStandardItem(transaction.name),
                QtGui.QStandardItem(str(transaction.date)),
                QtGui.QStandardItem(str(transaction.sum)),
                QtGui.QStandardItem(transaction.category)
            ]
            if self.ui.comboBox.currentText() == "Усі категорії":
                model.appendRow(row)
            else:
                if transaction.category == self.ui.comboBox.currentText():
                    model.appendRow(row)
        self.ui.tableView.setModel(model)
        self.get_statistics()

    def get_statistics(self):
        for category in self.categories:
            category.total_sum = 0
            for transaction in self.transactions:
                if transaction.category == category.name:
                    category.total_sum += transaction.sum

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['Category Name', 'Total sum'])
        for category in self.categories:
            row = [
                QtGui.QStandardItem(category.name),
                QtGui.QStandardItem(str(category.total_sum))
            ]
            model.appendRow(row)
        self.ui.tableView_2.setModel(model)

    def save_changes(self, event):
        filename = 'transactions.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(self.transactions, f)
        filename = 'categories.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(self.categories, f)
        event.accept

class NewTransactionWindow(QMainWindow):
    def __init__(self, categories, transactions, parent=None):
        super().__init__(parent=parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.parent = parent
        self.categories = categories
        self.transactions = transactions
        for category in categories:
            self.ui.comboBox.addItem(category.name)

        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.create_new_trans)

    @QtCore.Slot()
    def create_new_trans(self):
        if self.ui.lineEdit_2.text().isdigit():
            sum = int(self.ui.lineEdit_2.text())
            if sum > 0 and len(self.ui.lineEdit.text()) > 0:
                name = self.ui.lineEdit.text()
                category = self.ui.comboBox.currentText()
                date = self.ui.dateEdit.date().toString('yyyy-MM-dd')
                new_transaction = Transaction(name, date, sum, category)

                self.parent.transactions.append(new_transaction)
                self.parent.renew()
                self.close()


class NewCategoryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)
        self.parent = parent

        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.create_new_category)

    def create_new_category(self):
        if len(self.ui.lineEdit_3.text()) > 0:
            new_category = Category(self.ui.lineEdit_3.text())
            self.parent.categories.append(new_category)
            self.parent.get_statistics()
            self.parent.ui.comboBox.addItem(new_category.name)
            self.close()
class Transaction():
    def __init__(self, name, date, sum, category):
        self.name = name
        self.date = date
        self.sum = sum
        self.category = category

class Category():
    def __init__(self, name):
        self.name = name
        self.total_sum = 0

if __name__== "__main__":
    app = QApplication(sys.argv)
    window = PythonTracker()
    window.show()

    sys.exit(app.exec())